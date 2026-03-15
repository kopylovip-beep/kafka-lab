from kafka import KafkaConsumer
import json
from config import KAFKA_SERVER, TOPIC_NAME

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda m: m.decode("utf-8")
)

print("Consumer started")

def validate_message(message):
    try:
        data = json.loads(message)
        required_fields = [
            "flight_number",
            "destination",
            "departure_time",
            "status"
        ]
        for field in required_fields:
            if field not in data:
                return False

        return True
    except:
        return False

for msg in consumer:
    message = msg.value
    if validate_message(message):
        print("VALID MESSAGE:", message)
    else:
        print("NOT VALID:", message)
