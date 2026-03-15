from kafka import KafkaProducer
from generator import generate_recycling_event
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: v.encode("utf-8")
)

topic = "recycling"

while True:
    message = generate_recycling_event()
    print("Produced:", message)
    producer.send(topic, message)
    time.sleep(2)
