import json
import random
from datetime import datetime

flights = ["LH123", "AF431", "SU221", "BA912"]
destinations = ["Berlin", "Paris", "Rome", "Madrid"]
statuses = ["boarding", "departing", "delayed"]

def generate_message():

    message = {
        "flight_number": random.choice(flights),
        "destination": random.choice(destinations),
        "departure_time": datetime.now().strftime("%H:%M:%S"),
        "status": random.choice(statuses)
    }
    return json.dumps(message)
