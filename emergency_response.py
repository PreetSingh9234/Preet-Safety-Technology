from datetime import datetime

# EMERGENCY LEVEL CALCULATOR
def calculate_emergency_level(risk, confidence):
    if risk == "CRITICAL" and confidence >= 85:
        return "LEVEL 3 - EMERGENCY"
    elif risk == "WARNING":
        return "LEVEL 2 - WARNING"
    else:
        return "LEVEL 1 - NORMAL"

# EMERGENCY ACTION GENERATOR
def generate_response_actions(level):
    if level == "LEVEL 3 - EMERGENCY":
        return [
            "🚨 Activate emergency alarm",
            "🛑 Stop affected machinery",
            "👷 Evacuate worker from danger zone",
            "📢 Notify safety officer immediately",
            "🔍 Start hazard inspection",
            "🏥 Prepare medical assistance"
        ]
    elif level == "LEVEL 2 - WARNING":
        return [
            "⚠ Increase monitoring frequency",
            "🦺 Verify worker PPE",
            "🔧 Inspect equipment condition",
            "📡 Continue sensor tracking"
        ]
    else:
        return [
            "✅ Continue normal operation",
            "📡 Maintain regular monitoring"
        ]

# RESPONSE TIMELINE GENERATOR
def generate_timeline(level):
    if level == "LEVEL 3 - EMERGENCY":
        return {
            "0 sec": "Risk detected by AI",
            "10 sec": "Emergency alert generated",
            "30 sec": "Safety team notified",
            "60 sec": "Evacuation protocol started"
        }
    elif level == "LEVEL 2 - WARNING":
        return {
            "0 sec": "Abnormal condition detected",
            "30 sec": "Safety inspection started"
        }
    else:
        return {
            "0 sec": "Environment safe"
        }

# COMPLETE EMERGENCY REPORT
def create_emergency_report(worker, zone, risk, confidence):
    level = calculate_emergency_level(risk, confidence)

    report = {
        "Worker": worker,
        "Zone": zone,
        "Risk": risk,
        "AI Confidence": round(confidence, 2),
        "Emergency Level": level,
        "Actions": generate_response_actions(level),
        "Timeline": generate_timeline(level),
        "Generated At": datetime.now().strftime("%H:%M:%S")
    }

    return report

# TEST MODE
if __name__ == "__main__":
    emergency = create_emergency_report(
        "Worker-003",
        "Chemical Plant",
        "CRITICAL",
        95.4
    )

    print("\n===== EMERGENCY REPORT =====\n")
    for key, value in emergency.items():
        print(key, ":", value)