import random
import json
from datetime import datetime

users = ["Ivan", "Anna", "Sergey", "Maria", "Alex"]
materials = ["Plastic", "Glass", "Paper", "Metal", "Cardboard"]
actions = ["deposit", "reject"]

def generate_recycling_event():
    """
    Генерирует событие для пункта приема вторсырья.
    """
    data = {
        "user": random.choice(users),
        "material": random.choice(materials),
        "action": random.choice(actions),
        "weight_kg": round(random.uniform(0.1, 20.0), 2),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return json.dumps(data)
