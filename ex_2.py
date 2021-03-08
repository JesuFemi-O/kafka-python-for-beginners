#sending messages to a broker with 1 topic and 2 partitions
# we will have a single publisher/producer
#we will have a single topic
# our topic will have two partitions
#the message will be published to the pertions in a random manner 

from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from data import get_registered_user
import json
import time


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092" 
    #client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="example_topic", num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)


#with this code we can create a topic and give it as many partition as we so desire
#after that we can now send messages to the topic

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        print("sending a new message")
        producer.send("example_topic", registered_user)
        print("sent: ", registered_user)
        time.sleep(4)


# although messages are randomly sent to different partitons of a topic we can decide to send to a particular partition

#when we define a producer we can use a partitioner method to decide what patition the producer should send to.

#