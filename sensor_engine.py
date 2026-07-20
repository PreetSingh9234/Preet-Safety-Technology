import random
from datetime import datetime

FACTORY_ZONES = [
    "Chemical Processing Unit",
    "Steel Furnace Zone",
    "Mining Area",
    "Assembly Line",
    "Power Plant",
    "Storage Area"
]

WORKERS = [
    "Worker-001",
    "Worker-002",
    "Worker-003",
    "Worker-004",
    "Worker-005",
    "Worker-006",
    "Worker-007",
    "Worker-008"
]

def generate_live_sensor():
    temperature = round(random.uniform(30, 95), 2)
    gas = round(random.uniform(10, 150), 2)
    humidity = round(random.uniform(30, 95), 2)
    vibration = round(random.uniform(1, 10), 2)
    noise = round(random.uniform(50, 120), 2)
    fatigue = round(random.uniform(10, 95), 2)
    ppe = random.choice(["Available", "Missing"])
    worker = random.choice(WORKERS)
    zone = random.choice(FACTORY_ZONES)

    return {
        "Worker": worker,
        "Zone": zone,
        "Temperature": temperature,
        "Gas_Level": gas,
        "Humidity": humidity,
        "Machine_Vibration": vibration,
        "Noise_Level": noise,
        "Worker_Fatigue": fatigue,
        "PPE_Status": ppe,
        "Timestamp": datetime.now().strftime("%H:%M:%S")
    }

def sensor_status(value):
    if value >= 80:
        return "CRITICAL"
    elif value >= 60:
        return "WARNING"
    else:
        return "SAFE"