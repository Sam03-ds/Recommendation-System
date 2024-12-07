# Project Description
This project focuses on developing a content-based recommendation system to suggest articles to social network users, determining which posts are most relevant to them based on their interests. A microservice was developed using Fast API to provide top personalized recommendations for users. The system leverages a machine learning model (Catboost) trained on user interaction data and content features. Recommendations are generated based on the similarity of post features and user preferences. The service integrates with a PostgreSQL database to fetch real-time data about users and posts.

## How to Launch the Project
Follow these steps to build and run the project using the Dockerfile provided:
1. Ensure Docker is Installed
   ```shell
   docker --version
2. Build the Docker Image
   ```shell
   docker build -t my-microservice .
3. Run the Docker Container
   ```shell
   docker run my-microservice

## Example of an Application Query
 ```shell
http://localhost:5000/post/recommendations/?id=1001&time=2021-12-06T15:30:00&limit=5
```
Result
 ```shell
[
    {
        "id": 6768,
        "text": "This is by far and away the stupidest thing I have ever seen on celluloid. I mean, we started watching it assuming it was a skinemax T&A flick, but aside from a couple boobs, that was it. I mean, I get the point of making stupid movies in order to show some sex scenes, as they are the sole reason for a movie of that kind to be made. This movie, however, has no sex scenes, and really has no point at all. There is no linear time, the scenes travel around like a fart in the wind, people show up for no reason, then leave, and it is never explained, the plot is never advanced, and nothing happens. I have never been as flabbergasted at how bad a movie was until I saw this. Has the director even been to a film school? Has he ever seen a movie? I dont know, but from the looks of it, he seems to have made some moron proud with this piece of crap, as he is still working. I literally walked away from this movie dumber, but I still recommend watching it, as it should be shown in every film school of the country as an example in what not to do when making a film. Move over PLan 9 from Outer Space, you have a new contender for worst movie ever made.",
        "topic": "movie"
    },
    {
        "id": 5373,
        "text": "This movie is one of the worst movies I have ever seen. There is absolutely no storyline, the gags are only for retards and there is absolutely nothing else that would make this movie worth watching. In the whole movie Fredi (oh my god what a funny name. ha ha) doesnt ask himself ONCE how he came from a plane to middle earth. There are plenty of stupid and totally unfunny characters whose names should sound funny. e.g. : Gandalf is called Almghandi, Sam is called Pupsi ... and so on. I didnt even smile once during the whole movie. The gags seem like they were made by people whose IQ is negative. If you laugh when someones coat is trapped in the door (this happens about 5 times) then this movie is perhaps for you. Another funny scene: They try to guess the code word for a closed door (dont ask why- dont ever ask why in this movie) and the code word is (ha ha): dung. So if you laughed at this examples you might like this movie. For everybody else: Go to Youtube and watch Lord of the Weed: its a lot, lot more fun.",
        "topic": "movie"
    },
    {
        "id": 4610,
        "text": "You have to see this. I could not stop laughing about the stupidities I saw in this movie even late after the event. There is maybe a million of individual mistakes and stupidities in this movie. The acting is bad. The story is so predictable and flat. The effects are like 50 years old. The supposed thriller is nowhere. You will not enjoy the movie, but you will laugh at it and enjoy laughing at it a long time after it. We had a great time AFTER the movie. Truly. Me and my friend spent entire 40mins long bus trip home chatting about this movie like we have seen next Oscar winner. Sadly we were talking about all those bad things we had just seen.",
        "topic": "movie"
    },
    {
        "id": 5155,
        "text": "I watched this movie at 3o clock in the morning, a time in the day where I am usually very open when it comes to movies. But still I think it wasnt good, this movie wasnt good at all. The reasons why are many.The acting isnt all that good, and time after time situations occurring in it reminded me of a poor 90s Chevy Chase comedy. I mean, come on, like the handcuff situation, and the poker situation amongst the servants... This movie was so obviously based very much on the first one, and thats OK. But if I hadnt seen the first one before seeing this, it would have sucked even worse. Like the ending, it came very suddenly, and I felt like I got no closure what so ever... Sebastian changed very suddenly, and this This movie seems like it was made solely to explain nr 1, and like no time or effort was used on making anything else good. The score is the same as in the first one, and it didnt feel like a movie at all...They should have handled the situations with more style and class, but they didnt, and therefore, this movie turned out bad...",
        "topic": "movie"
    },
    {
        "id": 4545,
        "text": "I believe that this is one of Elizabeth Montgomerys best performances in a movie, and I have seen most of her movies.I saw this for the first time on television when I was around fourteen, and I was so scared.I watch this movie every now and then, and I still enjoy it very much.I know that these days that this movie would probably not scare people too much.That just goes to show that the public movie and television audience has seen too much graphic violence in the last thirty years or so.I love movies that do not show the graphic details, you let your imagination do the work for you. The cast in this movie was top notch. Jess Walton, who played the sister in the story was very good, even though her part was rather small. She also played in a terrific made for television thriller around the same time called Youll Never See Me Again with David Hartman.I got the biggest kick out of Eileen Heckarts performance as the housekeeper. Eileen was so good as a lady with a very bad disposition.George Maharis who played the husband was quite effective.This story obviously had a lot of so called mistakes in the plot, but I love the movie anyway. I highly recommend this movie to people who love a good thriller without graphic violence.I gave this movie a vote of seven.",
        "topic": "movie"
    }
]
