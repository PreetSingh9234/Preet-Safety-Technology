from datetime import datetime

RISK_PATTERNS = {
    "gas_maintenance": {
        "conditions": ["high_gas", "maintenance"],
        "risk": "EXPLOSION POSSIBILITY",
        "severity": "CRITICAL",
        "action": ["Stop maintenance activity", "Isolate affected zone", "Check gas source", "Evacuate nearby workers"]
    },
    "hot_work_gas": {
        "conditions": ["hot_work", "high_gas"],
        "risk": "FIRE / EXPLOSION HAZARD",
        "severity": "CRITICAL",
        "action": ["Suspend hot work permit", "Increase gas monitoring", "Notify safety officer"]
    },
    "fatigue_machine": {
        "conditions": ["high_fatigue", "high_vibration"],
        "risk": "OPERATOR ERROR + MACHINE FAILURE",
        "severity": "WARNING",
        "action": ["Rotate worker", "Inspect machinery", "Reduce workload"]
    },
    "ppe_hazard": {
        "conditions": ["missing_ppe", "hazard_zone"],
        "risk": "WORKER EXPOSURE RISK",
        "severity": "HIGH",
        "action": ["Stop worker entry", "Provide PPE", "Verify compliance"]
    }
}

def detect_compound_risk(data):
    detected = []
    risk_score = 0

    if data.get("Gas_Level", 0) > 80:
        detected.append("high_gas")
        risk_score += 30

    if data.get("Temperature", 0) > 85:
        detected.append("high_temperature")
        risk_score += 20

    if data.get("Machine_Vibration", 0) > 7:
        detected.append("high_vibration")
        risk_score += 20

    if data.get("Worker_Fatigue", 0) > 80:
        detected.append("high_fatigue")
        risk_score += 15

    if data.get("PPE_Status") == "Missing":
        detected.append("missing_ppe")
        risk_score += 20

    if data.get("Maintenance_Status") == "ACTIVE":
        detected.append("maintenance")
        risk_score += 15

    if data.get("Permit_Type") == "HOT_WORK":
        detected.append("hot_work")
        risk_score += 20

    if data.get("Zone_Risk") == "HIGH":
        detected.append("hazard_zone")
        risk_score += 10

    final_risk = []

    for name, pattern in RISK_PATTERNS.items():
        match = True
        for condition in pattern["conditions"]:
            if condition not in detected:
                match = False

        if match:
            final_risk.append({
                "Pattern": name,
                "Risk": pattern["risk"],
                "Severity": pattern["severity"],
                "Actions": pattern["action"]
            })

    if risk_score >= 70:
        level = "CRITICAL"
    elif risk_score >= 40:
        level = "WARNING"
    else:
        level = "SAFE"

    return {
        "Compound Risk Level": level,
        "Risk Score": min(risk_score, 100),
        "Detected Conditions": detected,
        "AI Findings": final_risk,
        "Generated": datetime.now().strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    sample = {
        "Gas_Level": 120,
        "Temperature": 90,
        "Machine_Vibration": 8,
        "Worker_Fatigue": 85,
        "PPE_Status": "Missing",
        "Maintenance_Status": "ACTIVE",
        "Permit_Type": "HOT_WORK",
        "Zone_Risk": "HIGH"
    }

    result = detect_compound_risk(sample)
    print(result)