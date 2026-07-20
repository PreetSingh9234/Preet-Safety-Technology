from datetime import datetime
import random

HAZARD_ZONES = {
    "Chemical Unit": 30,
    "Gas Plant": 25,
    "Furnace Area": 20,
    "Maintenance Area": 15,
    "Storage Area": 10,
    "Assembly Area": 5,
    "Unknown": 0
}

def analyze_gas(sensor):
    gas = sensor.get("Gas_Level", 0)
    if gas >= 120:
        return 30, ["☣ Critical gas concentration detected"]
    elif gas >= 80:
        return 20, ["⚠ Abnormal gas accumulation detected"]
    return 0, ["✅ Gas parameter normal"]

def analyze_temperature(sensor):
    temp = sensor.get("Temperature", 0)
    if temp >= 85:
        return 20, ["🔥 Extreme temperature condition"]
    elif temp >= 70:
        return 10, ["🌡 Temperature above safe limit"]
    return 0, ["✅ Temperature normal"]

def analyze_maintenance(status):
    if status == "ACTIVE":
        return 20, ["🛠 Active maintenance operation detected"]
    return 0, ["✅ No maintenance conflict"]

def analyze_permit(status):
    if status == "CONFLICT":
        return 20, ["🚧 Dangerous permit conflict detected"]
    return 0, ["✅ Permit status valid"]

def analyze_worker(sensor):
    fatigue = sensor.get("Worker_Fatigue", 0)
    if fatigue >= 85:
        return 10, ["😴 Critical worker fatigue detected"]
    elif fatigue >= 70:
        return 5, ["⚠ Increasing worker fatigue"]
    return 0, ["✅ Worker condition normal"]

def analyze_zone(sensor):
    zone = sensor.get("Zone", "Unknown")
    risk = HAZARD_ZONES.get(zone, 0)
    if risk > 0:
        return risk, [f"📍 Worker located in {zone} hazard zone"]
    return 0, ["📍 Normal operation zone"]

def analyze_equipment(status):
    if status == "FAILURE":
        return 25, ["⚙ Critical equipment failure detected"]
    return 0, ["✅ Equipment operating normally"]

def analyze_shift():
    hour = datetime.now().hour
    if hour in range(6, 8) or hour in range(18, 20):
        return 5, ["🔄 Shift changeover risk detected"]
    return 0, ["✅ Normal shift period"]

def detect_compound_patterns(sensor, maintenance, permit):
    patterns = []
    gas = sensor.get("Gas_Level", 0)
    zone = sensor.get("Zone", "Unknown")

    if gas >= 80 and maintenance == "ACTIVE":
        patterns.append("🔥 Gas accumulation + Maintenance activity combination detected")
    if gas >= 80 and permit == "CONFLICT":
        patterns.append("🚨 Hazardous gas + Permit conflict detected")
    if zone == "Chemical Unit" and gas >= 80:
        patterns.append("☣ Chemical zone exposure risk detected")
    
    return patterns

def predict_incident(score):
    if score >= 85:
        return ("CRITICAL", "Incident probability high within 5-15 minutes", 95)
    elif score >= 60:
        return ("HIGH", "Potential incident escalation within 15-45 minutes", 80)
    elif score >= 40:
        return ("WARNING", "Continuous monitoring required", 60)
    
    return ("SAFE", "No immediate threat detected", 10)

def calculate_compound_risk(sensor, maintenance_status="NORMAL", permit_status="VALID", equipment_status="NORMAL"):
    score = 0
    reasons = []

    modules = [
        analyze_gas(sensor),
        analyze_temperature(sensor),
        analyze_maintenance(maintenance_status),
        analyze_permit(permit_status),
        analyze_worker(sensor),
        analyze_zone(sensor),
        analyze_equipment(equipment_status),
        analyze_shift()
    ]

    for value, reason in modules:
        score += value
        reasons.extend(reason)

    compound_patterns = detect_compound_patterns(sensor, maintenance_status, permit_status)
    reasons.extend(compound_patterns)

    score = min(score, 100)
    level, prediction, probability = predict_incident(score)

    single_sensor = "SAFE"
    if sensor.get("Gas_Level", 0) >= 80:
        single_sensor = "WARNING"

    return {
        "Compound_Risk_Score": score,
        "Risk_Level": level,
        "Incident_Probability": f"{probability}%",
        "Prediction_Window": prediction,
        "Single_Sensor_Result": single_sensor,
        "AI_Advantage": "Multi-factor AI detected hidden compound risk",
        "AI_Reasoning": reasons,
        "Generated_Time": datetime.now().strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    test_sensor = {
        "Temperature": 92,
        "Gas_Level": 140,
        "Worker_Fatigue": 90,
        "Zone": "Chemical Unit"
    }

    result = calculate_compound_risk(
        test_sensor,
        maintenance_status="ACTIVE",
        permit_status="CONFLICT",
        equipment_status="FAILURE"
    )
    
    print(result)