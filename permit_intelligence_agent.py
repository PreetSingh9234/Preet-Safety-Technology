from datetime import datetime

PERMIT_RISK_WEIGHT = {
    "HOT_WORK": 30,
    "CONFINED_SPACE": 25,
    "ELECTRICAL_WORK": 20,
    "NORMAL": 0
}

def analyze_permit_conflict(permit_type="NORMAL", gas_level=0, maintenance_active=False, temperature=0, zone="Unknown", ppe="Available"):
    risk_score = 0
    reasons = []
    actions = []

    # Permit Risk
    permit_risk = PERMIT_RISK_WEIGHT.get(permit_type, 0)
    risk_score += permit_risk
    
    if permit_type != "NORMAL":
        reasons.append(f"📄 Active {permit_type} permit detected")

    # Gas Conflict Detection
    if gas_level >= 80 and permit_type == "HOT_WORK":
        risk_score += 40
        reasons.append("🔥 Hot work + Gas accumulation conflict detected")
        actions.append("🛑 Suspend hot work permit immediately")

    # Maintenance Conflict
    if maintenance_active and gas_level >= 80:
        risk_score += 20
        reasons.append("🛠 Maintenance activity during hazardous gas condition")
        actions.append("👷 Remove workers from affected zone")

    # Temperature Conflict
    if temperature >= 85 and permit_type == "HOT_WORK":
        risk_score += 15
        reasons.append("🌡 Extreme temperature during hot work activity")
        actions.append("🔥 Stop ignition source")

    # Zone Intelligence

    if zone in ["Chemical Unit","Chemical Processing Unit","Gas Plant"] and permit_type=="HOT_WORK":
        risk_score += 25
        reasons.append("☣ Hazard zone + Hot Work permit conflict detected")
        actions.append("🚨 Stop permit in hazardous zone")


    # PPE Intelligence

    if ppe=="Missing" and permit_type!="NORMAL":
        risk_score += 15
        reasons.append("🦺 PPE violation during permitted activity")
        actions.append("👷 Enforce PPE compliance")


    # Classification
    risk_score = min(risk_score, 100)

    if risk_score >= 80:
        status = "CRITICAL"
        decision = "Permit automatically blocked"
    elif risk_score >= 40:
        status = "WARNING"
        decision = "Permit requires safety review"
    else:
        status = "SAFE"
        decision = "Permit approved"

    if len(actions) == 0:
        actions.append("✅ Continue permit monitoring")

    return {
        "Permit Type": permit_type,
        "Permit Risk Score": risk_score,
        "Permit Status": status,
        "AI Decision": decision,
        "Risk Reasoning": reasons,
        "Recommended Actions": actions,
        "Generated Time": datetime.now().strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    result = analyze_permit_conflict(
        permit_type="HOT_WORK",
        gas_level=135,
        maintenance_active=True,
        temperature=92
    )
    print(result)