from datetime import datetime

class CompoundRiskEngine:
    def analyze(self, sensor, maintenance="NORMAL", permit="VALID"):
        score = 0
        reasons = []

        gas = sensor["Gas_Level"]
        if gas >= 120:
            score += 35
            reasons.append("☣ Critical gas accumulation detected")
        elif gas >= 80:
            score += 20
            reasons.append("⚠ Abnormal gas level detected")

        temp = sensor["Temperature"]
        if temp >= 85:
            score += 25
            reasons.append("🔥 Extreme temperature condition")
        elif temp >= 70:
            score += 10
            reasons.append("🌡 High temperature warning")

        vibration = sensor["Machine_Vibration"]
        if vibration >= 7:
            score += 15
            reasons.append("⚙ Machine vibration abnormal")

        fatigue = sensor["Worker_Fatigue"]
        if fatigue >= 85:
            score += 15
            reasons.append("😴 Worker fatigue critical")

        if sensor["PPE_Status"] == "Missing":
            score += 20
            reasons.append("🦺 PPE compliance failure")

        if permit == "CONFLICT":
            score += 15
            reasons.append("🚧 Permit conflict detected")

        if maintenance == "ACTIVE":
            score += 15
            reasons.append("🛠 Maintenance operation active")

        score = min(score, 100)

        if score >= 80:
            level = "CRITICAL"
            prediction = "High incident probability within 15-60 minutes"
        elif score >= 50:
            level = "WARNING"
            prediction = "Risk developing, preventive action required"
        else:
            level = "SAFE"
            prediction = "No immediate threat"

        return {
            "Compound_Score": score,
            "Risk_Level": level,
            "Prediction_Window": prediction,
            "Reasons": reasons,
            "Generated": datetime.now().strftime("%H:%M:%S")
        }