# ==========================================================
# PREET SAFETY TECHNOLOGY
# RAG SAFETY INTELLIGENCE AGENT
# ==========================================================


from datetime import datetime



SAFETY_DATABASE={


"gas":

{

"hazard":

"Industrial Gas Leakage",


"action":

[
"Stop nearby operation",
"Activate ventilation",
"Evacuate affected zone",
"Inspect gas source"
]

},



"temperature":

{

"hazard":

"High Temperature Risk",


"action":

[
"Reduce equipment load",
"Activate cooling system",
"Monitor thermal sensors"
]

},



"ppe":

{

"hazard":

"PPE Compliance Failure",


"action":

[
"Stop worker entry",
"Provide safety equipment",
"Verify compliance"
]

},



"vibration":

{

"hazard":

"Machine Failure Risk",


"action":

[
"Inspect machinery",
"Reduce operating speed",
"Schedule maintenance"
]

}

}




def generate_safety_advice(

    hazard,

    risk_level

):


    hazard=hazard.lower()



    result={


        "Risk Level":

        risk_level,


        "Hazard":

        hazard,


        "AI Advice":

        [],


        "Generated":

        datetime.now().strftime(

            "%H:%M:%S"

        )

    }



    for key,value in SAFETY_DATABASE.items():


        if key in hazard:


            result["AI Advice"]=value["action"]

            break



    if len(result["AI Advice"])==0:


        result["AI Advice"]=[

        "Continue monitoring",

        "Notify safety supervisor"

        ]



    return result
