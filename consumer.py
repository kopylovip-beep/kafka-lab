from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "recycling",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: m.decode("utf-8")
)

def validate(data):
    required_fields = ["user", "material", "action", "weight_kg", "time"]
    for field in required_fields:
        if field not in data:
            return False
    if data["action"] not in ["deposit", "reject"]:
        return False
    if not isinstance(data["weight_kg"], (int, float)):
        return False
    return True

for message in consumer:
    msg = message.value
    try:
        data = json.loads(msg)
        if validate(data):
            print("VALID:", data)
        else:
            print("NOT VALID:", msg)
    except Exception:
        print("NOT VALID:", msg)
