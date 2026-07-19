# ==========================================================
# PREET SAFETY TECHNOLOGY
# EMERGENCY RESPONSE ORCHESTRATOR
# ENTERPRISE AUTONOMOUS RESPONSE ENGINE
# ==========================================================


from datetime import datetime



def calculate_emergency_level(risk, confidence):

    if risk == "CRITICAL" and confidence >= 85:

        return "LEVEL 3 - EMERGENCY"


    elif risk == "WARNING":

        return "LEVEL 2 - WARNING"


    else:

        return "LEVEL 1 - NORMAL"





def generate_response_actions(level):


    if level == "LEVEL 3 - EMERGENCY":

        return [

            "🚨 Activate emergency alarm",

            "🛑 Stop affected machinery",

            "👷 Evacuate affected worker",

            "📢 Notify safety officer",

            "🔍 Start hazard inspection",

            "🏥 Prepare medical response"

        ]


    elif level == "LEVEL 2 - WARNING":

        return [

            "⚠ Increase monitoring",

            "🦺 Verify PPE compliance",

            "🔧 Inspect equipment",

            "📡 Continue tracking"

        ]


    else:

        return [

            "✅ Normal operation",

            "📡 Continue monitoring"

        ]





def generate_timeline(level):


    if level=="LEVEL 3 - EMERGENCY":


        return {


        "0 sec":"AI risk detected",

        "10 sec":"Emergency alert triggered",

        "30 sec":"Safety team notified",

        "60 sec":"Evacuation started"

        }


    elif level=="LEVEL 2 - WARNING":


        return {


        "0 sec":"Warning detected",

        "30 sec":"Inspection started"

        }


    else:


        return {


        "0 sec":"Environment safe"

        }






def create_emergency_report(

        worker,

        zone,

        risk,

        confidence

):


    level = calculate_emergency_level(

        risk,

        confidence

    )


    return {


        "Worker":worker,


        "Zone":zone,


        "Risk":risk,


        "AI Confidence":round(confidence,2),


        "Emergency Level":level,


        "Actions":generate_response_actions(level),


        "Timeline":generate_timeline(level),


        "Generated At":

        datetime.now().strftime("%H:%M:%S")


    }