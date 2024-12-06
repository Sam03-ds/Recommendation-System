import pandas as pd
from typing import List
from catboost import CatBoostClassifier
from fastapi import FastAPI
from schema import PostGet
from datetime import datetime
from sqlalchemy import create_engine
from loguru import logger
import uvicorn
import warnings
warnings.filterwarnings("ignore")

model_path = "models/catboost_model"
app = FastAPI()


def batch_load_sql(query: str):
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
    )

    conn = engine.connect().execution_options(
        stream_results=True
    )
    chunks = []
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=200000):
        chunks.append(chunk_dataframe)
        logger.info(f"Got chunk: {len(chunk_dataframe)}")
    conn.close()
    return pd.concat(chunks, ignore_index=True)


def load_features():
    # download posts, which weren't liked yet
    logger.info('loading liked posts')
    liked_posts_query = """
        SELECT distinct post_id, user_id
        FROM public.feed_data
        WHERE action='like'
    """
    liked_posts = batch_load_sql(liked_posts_query)

    # download tf-idf features
    logger.info('loading posts features')
    posts_features = pd.read_sql(
        """SELECT * FROM public.posts_info_features_table""",

        con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
            "postgres.lab.karpov.courses:6432/startml"
    )

    # download users features
    logger.info("loading users features")
    user_features = pd.read_sql(
        """SELECT * FROM public.user_data""",

        con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
            "postgres.lab.karpov.courses:6432/startml"
    )

    return [liked_posts, posts_features, user_features]


def load_models(model_path: str):

    # download Catboost model
    loaded_model = CatBoostClassifier()
    loaded_model.load_model(model_path)

    return loaded_model


logger.info("loading model")
model = load_models(model_path=model_path)
logger.info("loading features")
features = load_features()
logger.info("service is up and running")


def ger_recommended_feed(id: int, time: datetime, limit: int):
    # getting recommendations for a user

    # download users features
    logger.info(f"user_id: {id}")
    logger.info("reading features")
    user_features = features[2].loc[features[2].user_id == id]
    user_features = user_features.drop('user_id', axis = 1)

    logger.info("dropping columns")
    posts_features = features[1].drop(['index', 'text'], axis = 1)
    content = features[1][['post_id', 'text', 'topic']]

    # merge features

    logger.info("zipping everything")
    add_user_features = dict(zip(user_features.columns, user_features.values[0]))

    logger.info("assigning everything")
    user_posts_features = posts_features.assign(**add_user_features)
    user_posts_features = user_posts_features.set_index("post_id")

    # add info about date of recommendation
    logger.info("add time info")
    user_posts_features['hour'] = time.hour
    user_posts_features['month'] = time.month

    # make a prediction
    logger.info("predicting")
    predicts = model.predict_proba(user_posts_features)[:, 1]
    user_posts_features["predict"] = predicts

    # drop posts which user has already liked
    logger.info("deleting liked posts")
    liked_posts = features[0]
    liked_posts = liked_posts[liked_posts.user_id == id].post_id.values
    filtered_ = user_posts_features[~user_posts_features.index.isin(liked_posts)]

    # recommend top 5 posts
    recommended_posts = filtered_.sort_values('predict')[-limit:].index

    return [
        PostGet(**{
            "id": i,
            "text": content[content.post_id == i].text.values[0],
            "topic": content[content.post_id == i].topic.values[0]
        }) for i in recommended_posts
    ]


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(id: int, time: datetime, limit: int = 10) -> List[PostGet]:
    return ger_recommended_feed(id, time, limit)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)


