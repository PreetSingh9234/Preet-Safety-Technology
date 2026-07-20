from datetime import datetime

COMPLIANCE_DATABASE = {
    "gas": {
        "hazard": "Industrial Gas Leakage",
        "standards": [
            "OISD Process Safety Standard",
            "Factory Act 1948"
        ],
        "risk": "CRITICAL",
        "score": 92,
        "actions": [
            "Verify gas detection system",
            "Check emergency isolation valves",
            "Review ventilation status",
            "Perform hazard assessment"
        ]
    },
    "temperature": {
        "hazard": "Extreme Temperature Risk",
        "standards": [
            "Factory Act Thermal Safety Rules"
        ],
        "risk": "HIGH",
        "score": 88,
        "actions": [
            "Inspect thermal control system",
            "Reduce equipment load",
            "Monitor temperature sensors"
        ]
    },
    "ppe": {
        "hazard": "PPE Compliance Failure",
        "standards": [
            "PPE Safety Regulations",
            "Factory Act Worker Protection"
        ],
        "risk": "MEDIUM",
        "score": 75,
        "actions": [
            "Verify PPE availability",
            "Stop unsafe entry",
            "Conduct worker briefing"
        ]
    },
    "machine": {
        "hazard": "Equipment Safety Risk",
        "standards": [
            "DGMS Equipment Safety Guidelines"
        ],
        "risk": "HIGH",
        "score": 82,
        "actions": [
            "Perform preventive maintenance",
            "Review equipment history",
            "Inspect vibration trends"
        ]
    }
}

def compliance_analysis(hazard):
    hazard = hazard.lower()

    result = {
        "Detected Hazard": hazard,
        "Compliance Standards": [],
        "Risk Category": "LOW",
        "Compliance Score": 100,
        "AI Recommendations": [],
        "Corrective Action": "No deviation detected",
        "Generated": datetime.now().strftime("%H:%M:%S")
    }

    for key, value in COMPLIANCE_DATABASE.items():
        if key in hazard:
            result["Detected Hazard"] = value["hazard"]
            result["Compliance Standards"] = value["standards"]
            result["Risk Category"] = value["risk"]
            result["Compliance Score"] = value["score"]
            result["AI Recommendations"] = value["actions"]
            result["Corrective Action"] = "Immediate corrective workflow initiated"
            break

    if not result["AI Recommendations"]:
        result["AI Recommendations"] = [
            "Continue monitoring",
            "Perform periodic safety audit"
        ]

    return result