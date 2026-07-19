# ==========================================================
# PREET SAFETY TECHNOLOGY
# AI COMPUTER VISION SAFETY INTELLIGENCE AGENT
# ==========================================================


import random
from datetime import datetime



# ==========================================================
# AI CAMERA DATABASE
# ==========================================================


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





# ==========================================================
# PPE DETECTION ENGINE
# ==========================================================


def detect_ppe():


    helmet = random.choice(

        [
            "Detected",
            "Missing"
        ]

    )


    safety_vest = random.choice(

        [
            "Detected",
            "Missing"
        ]

    )


    shoes = random.choice(

        [
            "Detected",
            "Missing"
        ]

    )



    return {


        "Helmet":

        helmet,


        "Safety Vest":

        safety_vest,


        "Safety Shoes":

        shoes

    }





# ==========================================================
# UNSAFE ACTIVITY DETECTION
# ==========================================================


def detect_unsafe_activity():


    activity = random.choice(

        [

        "Normal Operation",

        "Worker Near Hazard Zone",

        "Unauthorized Entry",

        "Unsafe Posture"

        ]

    )


    return activity





# ==========================================================
# AI VISION RISK ANALYSIS
# ==========================================================


def vision_risk_analysis():



    camera=random.choice(CAMERAS)


    zone=random.choice(ZONES)



    ppe=detect_ppe()


    activity=detect_unsafe_activity()



    risk_score=0



    if "Missing" in ppe.values():

        risk_score +=40



    if activity != "Normal Operation":

        risk_score +=40



    if zone=="Chemical Processing Unit":

        risk_score +=20




    if risk_score >=70:

        risk="CRITICAL"


    elif risk_score >=40:

        risk="WARNING"


    else:

        risk="SAFE"





    return {


        "Camera":

        camera,


        "Zone":

        zone,


        "PPE Status":

        ppe,


        "Activity":

        activity,


        "Vision Risk Score":

        risk_score,


        "Risk":

        risk,


        "Timestamp":

        datetime.now().strftime(

            "%H:%M:%S"

        )

    }





# ==========================================================
# TEST
# ==========================================================


if __name__=="__main__":


    result=vision_risk_analysis()


    print("\n===== AI VISION REPORT =====\n")


    for key,value in result.items():

        print(

            key,

            ":",

            value

        )
