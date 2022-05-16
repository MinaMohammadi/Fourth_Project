from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "input",
        bootstrap_servers='kafka.kafka.svc:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print(msg)
        
