import random
from datetime import datetime

CAMERAS = [
    "CAM-001",
    "CAM-002",
    "CAM-003",
    "CAM-004"
]

ZONES = [
    "Chemical Processing Unit",
    "Steel Furnace Zone",
    "Mining Area",
    "Assembly Line"
]

def detect_ppe():
    items = {
        "Helmet": random.choice(["Detected", "Missing"]),
        "Safety Vest": random.choice(["Detected", "Missing"]),
        "Safety Shoes": random.choice(["Detected", "Missing"])
    }

    detected = sum(1 for x in items.values() if x == "Detected")
    score = int((detected / 3) * 100)

    return items, score

def detect_worker_behavior():
    return random.choice([
        "Normal Operation",
        "Worker Near Hazard Zone",
        "Unauthorized Entry",
        "Unsafe Posture"
    ])

def calculate_vision_risk(ppe_score, activity, zone):
    score = 0

    if ppe_score < 100:
        score += 30

    if activity != "Normal Operation":
        score += 40

    if zone == "Chemical Processing Unit":
        score += 20

    if activity == "Unauthorized Entry":
        score += 20

    return min(score, 100)

def vision_risk_analysis():
    camera = random.choice(CAMERAS)
    zone = random.choice(ZONES)

    ppe, ppe_score = detect_ppe()
    activity = detect_worker_behavior()

    risk_score = calculate_vision_risk(ppe_score, activity, zone)

    if risk_score >= 70:
        risk = "CRITICAL"
    elif risk_score >= 40:
        risk = "WARNING"
    else:
        risk = "SAFE"

    recommendations = []

    if ppe_score < 100:
        recommendations.append("Verify missing PPE compliance")

    if activity != "Normal Operation":
        recommendations.append("Inspect worker activity immediately")

    if zone == "Chemical Processing Unit":
        recommendations.append("Increase camera monitoring")

    if not recommendations:
        recommendations.append("Continue visual monitoring")

    return {
        "Camera": camera,
        "Zone": zone,
        "PPE Status": ppe,
        "PPE Compliance Score": ppe_score,
        "Activity": activity,
        "Risk": risk,
        "Vision Risk Score": risk_score,
        "AI Recommendations": recommendations,
        "Confidence": random.randint(90, 98),
        "Timestamp": datetime.now().strftime("%H:%M:%S")
    }