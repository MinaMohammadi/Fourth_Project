##!/usr/bin/env python
from kafka import KafkaProducer
import json, time
from data import get_users


def json_serializer(data):
    return json.dumps(data).encode("utf-8")
  
##KAFKA PRODUCER
producer = KafkaProducer(bootstrap_servers=['kafka.kafka.svc:9092'],
                         value_serializer=json_serializer)
##wirte message into input topic
if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_users()
        print(registered_user)
        producer.send("input", registered_user)
        time.sleep(4)
