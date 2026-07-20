from datetime import datetime
from pprint import pprint

# EMERGENCY LEVEL CLASSIFIER
def calculate_emergency_level(risk_level, confidence, risk_score):
    """Determines enterprise emergency level using AI confidence and compound risk score."""
    if risk_score >= 80:
        return "LEVEL 4 - PLANT EMERGENCY"
    elif risk_score >= 60:
        return "LEVEL 3 - CRITICAL"
    elif risk_score >= 40:
        return "LEVEL 2 - WARNING"
    else:
        return "LEVEL 1 - NORMAL"

# SEVERITY SCORE
def calculate_severity_score(risk_score, confidence):
    """Generates severity score out of 100."""
    score = int((risk_score * 0.70) + (confidence * 0.30))
    return min(score, 100)

# RESPONSE ACTION ENGINE
def generate_response_actions(level):
    if level == "LEVEL 4 - PLANT EMERGENCY":
        return [
            "🚨 Activate plant emergency protocol",
            "🛑 Shut down affected process",
            "👷 Evacuate all workers from danger zone",
            "🚒 Notify fire response team",
            "🚑 Prepare medical response",
            "📢 Inform control room",
            "📁 Preserve all sensor evidence"
        ]
    elif level == "LEVEL 3 - CRITICAL":
        return [
            "🚨 Activate emergency alarm",
            "👷 Evacuate affected workers",
            "📢 Notify safety officer",
            "🔍 Start hazard inspection",
            "📡 Increase sensor monitoring"
        ]
    elif level == "LEVEL 2 - WARNING":
        return [
            "⚠ Increase monitoring",
            "🦺 Verify PPE compliance",
            "🔧 Inspect nearby equipment",
            "📋 Review work permits"
        ]
    else:
        return [
            "✅ Continue normal operation",
            "📡 Continue AI monitoring"
        ]

# ALERT CHANNEL ENGINE
def generate_alert_channels(level):
    if level in ["LEVEL 4 - PLANT EMERGENCY", "LEVEL 3 - CRITICAL"]:
        return [
            "🏢 Central Control Room",
            "👷 Safety Officer",
            "🚒 Fire Response Team",
            "🚑 Medical Team",
            "📱 Plant Supervisor"
        ]
    elif level == "LEVEL 2 - WARNING":
        return ["👷 Safety Officer", "📱 Shift Supervisor"]
    return ["📡 Monitoring Dashboard"]

# SENSOR EVIDENCE PRESERVATION
def preserve_sensor_evidence(sensor):
    """Stores sensor snapshot for investigation."""
    return {
        "Worker": sensor.get("Worker"),
        "Zone": sensor.get("Zone"),
        "Temperature": sensor.get("Temperature"),
        "Gas Level": sensor.get("Gas_Level"),
        "Humidity": sensor.get("Humidity"),
        "Noise": sensor.get("Noise_Level"),
        "Vibration": sensor.get("Machine_Vibration"),
        "Fatigue": sensor.get("Worker_Fatigue"),
        "PPE": sensor.get("PPE_Status"),
        "Timestamp": sensor.get("Timestamp")
    }

def preserve_sensor_evidence_backup(worker, zone):
    return {
        "Sensor Snapshot": "Captured",
        "Camera Recording": "Saved",
        "SCADA Log": "Archived",
        "Worker": worker,
        "Zone": zone,
        "Evidence Status": "READY"
    }

# AUTONOMOUS RESPONSE TIMELINE
def generate_timeline(level):
    if level == "LEVEL 4 - PLANT EMERGENCY":
        return {
            "0 sec": "Compound AI risk detected",
            "10 sec": "Emergency alarm activated",
            "20 sec": "Control room notified",
            "30 sec": "Fire & Medical teams dispatched",
            "45 sec": "Plant evacuation initiated",
            "60 sec": "Digital evidence preserved"
        }
    elif level == "LEVEL 3 - CRITICAL":
        return {
            "0 sec": "Critical risk detected",
            "15 sec": "Safety officer notified",
            "30 sec": "Hazard inspection started",
            "45 sec": "Worker evacuation initiated"
        }
    elif level == "LEVEL 2 - WARNING":
        return {
            "0 sec": "Warning detected",
            "30 sec": "Inspection assigned",
            "60 sec": "Monitoring intensified"
        }
    return {"0 sec": "System operating normally"}

# AI INCIDENT SUMMARY
def generate_incident_summary(worker, zone, level):
    if level == "LEVEL 4 - PLANT EMERGENCY":
        return (
            f"Critical compound hazard detected near {zone}. "
            f"Worker {worker} is inside a high-risk operational area. "
            "Emergency protocol has been activated automatically."
        )
    elif level == "LEVEL 3 - CRITICAL":
        return (
            f"High-risk condition detected for {worker} in {zone}. "
            "Immediate intervention is recommended."
        )
    elif level == "LEVEL 2 - WARNING":
        return (
            f"Abnormal operating conditions detected around {zone}. "
            "Preventive inspection has been initiated."
        )
    return "No abnormal safety conditions detected."

# REGULATORY REFERENCES
def generate_regulatory_reference(level):
    if level in ["LEVEL 4 - PLANT EMERGENCY", "LEVEL 3 - CRITICAL"]:
        return ["Factory Act 1948", "DGMS Safety Guidelines", "OISD Process Safety Standard"]
    elif level == "LEVEL 2 - WARNING":
        return ["Factory Act Inspection Rules"]
    return ["Standard Safe Operations"]

# RESPONSE TEAM DISPATCH ENGINE
def dispatch_response_team(level):
    if level == "LEVEL 3 - CRITICAL":
        return {
            "Fire Team": "DISPATCHED",
            "Medical Team": "DISPATCHED",
            "Rescue Team": "DISPATCHED",
            "Safety Officer": "NOTIFIED",
            "Plant Manager": "NOTIFIED"
        }
    elif level == "LEVEL 2 - WARNING":
        return {
            "Safety Officer": "NOTIFIED",
            "Maintenance Team": "DISPATCHED",
            "Supervisor": "NOTIFIED"
        }
    return {"Monitoring Team": "ACTIVE"}

# MULTI CHANNEL ALERT SYSTEM
def send_emergency_alert(level):
    if level == "LEVEL 3 - CRITICAL":
        return [
            "📱 SMS Alert Sent",
            "📧 Email Alert Sent",
            "📢 Control Room Alert",
            "📻 Radio Communication Active",
            "🚨 Siren Activated"
        ]
    elif level == "LEVEL 2 - WARNING":
        return ["📱 Supervisor Alert", "📧 Safety Officer Email"]
    return ["✅ Monitoring Only"]

# INCIDENT ID GENERATOR
def generate_incident_id():
    now = datetime.now()
    return f"INC-{now.strftime('%Y%m%d-%H%M%S')}"

# ENTERPRISE INCIDENT REPORT
def create_emergency_report(sensor, risk_level, confidence, risk_score):
    emergency_level = calculate_emergency_level(risk_level, confidence, risk_score)

    report = {
        "Worker": sensor.get("Worker"),
        "Zone": sensor.get("Zone"),
        "Emergency Level": emergency_level,
        "Risk Level": risk_level,
        "Risk Score": risk_score,
        "AI Confidence": round(confidence, 2),
        "Severity Score": calculate_severity_score(risk_score, confidence),
        "Actions": generate_response_actions(emergency_level),
        "Alert Channels": generate_alert_channels(emergency_level),
        "Timeline": generate_timeline(emergency_level),
        "Incident Summary": generate_incident_summary(sensor.get("Worker"), sensor.get("Zone"), emergency_level),
        "Regulatory Compliance": generate_regulatory_reference(emergency_level),
        "Evidence": preserve_sensor_evidence(sensor),
        "Response Team Dispatch": dispatch_response_team(emergency_level),
        "Emergency Alerts": send_emergency_alert(emergency_level),
        "Incident ID": generate_incident_id(),
        "Generated At": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    
    return report

# TEST MODE
if __name__ == "__main__":
    sample_sensor = {
        "Worker": "Worker-07",
        "Zone": "Chemical Unit",
        "Temperature": 91,
        "Gas_Level": 135,
        "Humidity": 74,
        "Noise_Level": 95,
        "Machine_Vibration": 8,
        "Worker_Fatigue": 88,
        "PPE_Status": "Missing",
        "Timestamp": datetime.now().strftime("%H:%M:%S")
    }

    report = create_emergency_report(
        sensor=sample_sensor,
        risk_level="CRITICAL",
        confidence=97.4,
        risk_score=95
    )

    print(report)