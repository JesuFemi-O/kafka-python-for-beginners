# Getting started with Kafka in Python

## About Project

this repo holds diferent scripts explaining in simple examples how to create producers and consumers using kafka-python and is built to help people looking to get started in using apache kafka for writing evernt driven services with python.

## Getting Started

[Daily code buffer](https://www.youtube.com/watch?v=EUzH9khPYgs) Youtube Channel explains in easy to follow steps how to setup an apache kafka server on your windows machine and is a recommended prerequisite for windows user.

for linux/mac user's [this video](https://www.youtube.com/watch?v=jY5fzVCkABg&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=3&t=18s) comes in handy

## Starting The server 

- navigate to kafka folder on your machine
~~~
    cd c:/kafka (replace with your own path)
~~~

- start apache zookeper (windows command)
~~~
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
~~~

- start apache kafka server in another  terminal
~~~
    .\bin\windows\kafka-server-start.bat .\config\server.properties
~~~


## Running your consumer and producer scripts:

- open new terminal and navigate to the code folder on your machine

- create a viirutal env
~~~
    python -m venv venv
~~~

- start virtual env
~~~
    .\venv\scripts\activate
~~~

- install requirements
~~~
    pip install -r requirements.txt
~~~

- run a script
~~~
    python ex_1.py
~~~

## monitoring the published messages in terminal

- to see the messages that are being published to a topic you can open a new terminal, navigate to the kafka directory and run:
~~~
    .\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic TestTopic --from-beginning
~~~

Good resource to learn the theory can be found [here](https://youtube.com/playlist?list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4)