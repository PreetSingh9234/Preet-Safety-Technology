import pandas as pd
import numpy as np
import random
import os


# ==============================
# PREET SAFETY TECHNOLOGY
# AI Industrial Safety Dataset Generator
# ==============================


np.random.seed(42)
random.seed(42)


# Number of records
TOTAL_RECORDS = 5000


# Industrial zones
zones = [
    "Chemical Plant",
    "Steel Furnace",
    "Mining Area",
    "Assembly Line",
    "Power Station",
    "Refinery Zone"
]


# PPE options
ppe_status = [
    "Available",
    "Missing"
]


data = []


# ==============================
# Risk Intelligence Engine
# ==============================

def calculate_risk(
    temperature,
    gas,
    humidity,
    vibration,
    noise,
    fatigue,
    ppe
):

    risk_score = 0


    if temperature > 55:
        risk_score += 25

    if gas > 70:
        risk_score += 25

    if humidity > 85:
        risk_score += 10

    if vibration > 7:
        risk_score += 15

    if noise > 90:
        risk_score += 10

    if fatigue > 75:
        risk_score += 10

    if ppe == "Missing":
        risk_score += 20



    if risk_score >= 60:
        return "CRITICAL"

    elif risk_score >= 30:
        return "WARNING"

    else:
        return "SAFE"



# ==============================
# Generate Synthetic Workers
# ==============================


for i in range(TOTAL_RECORDS):


    worker_id = f"Worker-{str(i+1).zfill(4)}"


    zone = random.choice(zones)


    temperature = round(
        np.random.normal(45,15),
        2
    )


    gas_level = round(
        np.random.normal(45,25),
        2
    )


    humidity = round(
        np.random.normal(60,20),
        2
    )


    vibration = round(
        np.random.uniform(1,10),
        2
    )


    noise = round(
        np.random.normal(75,20),
        2
    )


    fatigue = round(
        np.random.uniform(10,95),
        2
    )


    ppe = random.choice(ppe_status)



    # Keep values realistic

    temperature = max(20,min(90,temperature))
    gas_level = max(0,min(150,gas_level))
    humidity = max(10,min(100,humidity))
    noise = max(40,min(120,noise))


    risk = calculate_risk(
        temperature,
        gas_level,
        humidity,
        vibration,
        noise,
        fatigue,
        ppe
    )


    data.append([

        worker_id,
        zone,
        temperature,
        gas_level,
        humidity,
        vibration,
        noise,
        fatigue,
        ppe,
        risk

    ])



# ==============================
# Save Dataset
# ==============================


df = pd.DataFrame(

    data,

    columns=[

        "Worker_ID",
        "Zone",
        "Temperature",
        "Gas_Level",
        "Humidity",
        "Machine_Vibration",
        "Noise_Level",
        "Worker_Fatigue",
        "PPE_Status",
        "Risk_Level"

    ]

)



# Create data folder if missing

os.makedirs(
    "data",
    exist_ok=True
)



file_path = "data/safety_data.csv"


df.to_csv(
    file_path,
    index=False
)



print("="*50)
print("PREET SAFETY TECHNOLOGY")
print("AI Safety Dataset Generated Successfully")
print("="*50)

print(f"Total Workers Data : {len(df)}")
print(f"Saved Location     : {file_path}")

print("\nRisk Distribution:")
print(df["Risk_Level"].value_counts())

print("="*50)