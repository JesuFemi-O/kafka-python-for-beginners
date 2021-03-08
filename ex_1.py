#single broker - 1 partition
#all the messages are published to a single partition
# here we demonstrate how a single producer can send message to a broker with just one topic and partition
from kafka import KafkaProducer
import json
from data import get_registered_user
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        print("sending a new message")
        producer.send("newTopic", registered_user)
        print("sent: ", registered_user)
        time.sleep(4)

#print(type(producer))