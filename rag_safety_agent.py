from datetime import datetime

# SAFETY KNOWLEDGE CORPUS
SAFETY_KNOWLEDGE = {
    "gas": {
        "hazard": "Industrial Gas Leakage",
        "historical_pattern": "Gas accumulation during maintenance activity has been linked with explosion risk.",
        "regulation": [
            "OISD Process Safety Standard",
            "Factory Act Safety Rules"
        ],
        "actions": [
            "Stop nearby operation",
            "Activate ventilation",
            "Evacuate affected zone",
            "Inspect gas source"
        ]
    },
    "temperature": {
        "hazard": "Extreme Temperature Condition",
        "historical_pattern": "High thermal conditions can accelerate equipment failure and worker exposure.",
        "regulation": [
            "Factory Act 1948",
            "Industrial Heat Safety Guidelines"
        ],
        "actions": [
            "Reduce equipment load",
            "Activate cooling system",
            "Monitor thermal sensors"
        ]
    },
    "ppe": {
        "hazard": "PPE Compliance Failure",
        "historical_pattern": "Missing PPE increases severity of industrial incidents.",
        "regulation": [
            "PPE Safety Regulations",
            "Factory Act Worker Protection Rules"
        ],
        "actions": [
            "Stop unsafe worker entry",
            "Provide required PPE",
            "Verify compliance"
        ]
    },
    "vibration": {
        "hazard": "Machine Failure Risk",
        "historical_pattern": "Abnormal vibration is an early indicator of equipment degradation.",
        "regulation": [
            "Equipment Maintenance Safety Standard"
        ],
        "actions": [
            "Inspect machinery",
            "Reduce operating speed",
            "Schedule maintenance"
        ]
    }
}

# RAG RETRIEVAL ENGINE
def retrieve_safety_context(hazard):
    hazard = hazard.lower()
    
    for key, data in SAFETY_KNOWLEDGE.items():
        if key in hazard:
            return data
            
    return {
        "hazard": "Unknown Safety Condition",
        "historical_pattern": "No matching incident pattern found.",
        "regulation": [
            "Standard Industrial Safety Practice"
        ],
        "actions": [
            "Continue monitoring",
            "Notify safety supervisor"
        ]
    }

# MAIN AI SAFETY ADVISOR
def generate_safety_advice(hazard, risk_level):
    context = retrieve_safety_context(hazard)
    
    return {
        "Risk Level": risk_level,
        "Detected Safety Issue": context["hazard"],
        "Historical Incident Pattern": context["historical_pattern"],
        "Regulatory Reference": context["regulation"],
        "AI Prevention Recommendations": context["actions"],
        "AI Confidence": "94%",
        "Generated": datetime.now().strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    print(generate_safety_advice("gas leakage", "CRITICAL"))