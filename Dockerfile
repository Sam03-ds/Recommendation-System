FROM python:3.10

RUN mkdir /main
COPY . /main/

WORKDIR /main

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Command to run the application
CMD ["sh", "-c", "python service.py"]