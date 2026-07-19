# ==========================================================
# PREET SAFETY TECHNOLOGY
# AI REGULATORY COMPLIANCE INTELLIGENCE AGENT
# ==========================================================


from datetime import datetime



COMPLIANCE_DATABASE = {


"gas leakage":

{
"standard":
"OISD Safety Guidelines",

"risk":
"High",

"recommendation":[

"Verify gas detection system",

"Check emergency isolation valves",

"Review ventilation status",

"Conduct hazard assessment"

]

},



"confined space":

{
"standard":
"Factory Act Safety Rules",

"risk":
"Critical",

"recommendation":[

"Verify permit-to-work",

"Check gas testing certificate",

"Assign standby supervisor",

"Maintain rescue equipment"

]

},



"machine":

{
"standard":
"DGMS Equipment Safety",

"risk":
"Medium",

"recommendation":[

"Perform preventive maintenance",

"Check vibration level",

"Review machine history"

]

},



"ppe":

{
"standard":
"Industrial Safety Compliance",

"risk":
"Medium",

"recommendation":[

"Verify PPE availability",

"Conduct worker safety training"

]

}

}





def compliance_analysis(hazard):


    hazard = hazard.lower()


    result = {


    "Detected Hazard":

    hazard,


    "Compliance Standard":

    "General Safety Practice",


    "Risk Category":

    "Low",


    "AI Recommendations":

    [],


    "Generated":

    datetime.now().strftime("%H:%M:%S")


    }



    for key,value in COMPLIANCE_DATABASE.items():


        if key in hazard:


            result["Compliance Standard"] = value["standard"]

            result["Risk Category"] = value["risk"]

            result["AI Recommendations"] = value["recommendation"]

            break



    if not result["AI Recommendations"]:


        result["AI Recommendations"]=[

        "Continue monitoring",

        "Perform safety inspection"

        ]



    return result
