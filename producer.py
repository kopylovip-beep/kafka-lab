from kafka import KafkaProducer
import time
from generator import generate_message
from config import KAFKA_SERVER, TOPIC_NAME

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: v.encode("utf-8")
)

print("Producer started")

while True:

    message = generate_message()

    print("Generated message:", message)

    producer.send(TOPIC_NAME, message)

    time.sleep(2)
