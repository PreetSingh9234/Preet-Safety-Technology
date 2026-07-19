# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE EXPLAINABLE AI ENGINE (XAI)
# AI Decision Transparency Layer v2.0
# ==========================================================


from datetime import datetime



# ==========================================================
# SAFETY LIMITS
# ==========================================================


SAFETY_THRESHOLDS = {


    "Temperature":

    70,


    "Gas_Level":

    80,


    "Machine_Vibration":

    7,


    "Noise_Level":

    100,


    "Worker_Fatigue":

    75


}






# ==========================================================
# FEATURE CONTRIBUTION ANALYZER
# ==========================================================



def analyze_feature_contribution(sensor):


    factors=[]



    score={}



    # Temperature


    if sensor["Temperature"] > SAFETY_THRESHOLDS["Temperature"]:


        value=min(

            35,

            int(

            (sensor["Temperature"]

            /

            100)

            *

            40

            )

        )


        score["Temperature"]=value


        factors.append(

        "🔥 High temperature condition detected"

        )





    else:


        score["Temperature"]=0





    # Gas


    if sensor["Gas_Level"] > SAFETY_THRESHOLDS["Gas_Level"]:


        value=min(

            40,

            int(

            (sensor["Gas_Level"]

            /

            150)

            *

            45

            )

        )



        score["Gas Leakage"]=value



        factors.append(

        "☣ Hazardous gas concentration detected"

        )


    else:


        score["Gas Leakage"]=0






    # Vibration


    if sensor["Machine_Vibration"] > SAFETY_THRESHOLDS["Machine_Vibration"]:


        score["Machine Health"]=15



        factors.append(

        "⚙ Abnormal machine vibration detected"

        )


    else:


        score["Machine Health"]=0






    # Noise


    if sensor["Noise_Level"] > SAFETY_THRESHOLDS["Noise_Level"]:


        score["Noise Exposure"]=10



        factors.append(

        "🔊 Excessive industrial noise exposure"

        )


    else:


        score["Noise Exposure"]=0







    # Fatigue


    if sensor["Worker_Fatigue"] > SAFETY_THRESHOLDS["Worker_Fatigue"]:


        score["Worker Fatigue"]=15



        factors.append(

        "😴 Worker fatigue risk detected"

        )


    else:


        score["Worker Fatigue"]=0






    # PPE


    if sensor.get("PPE_Status")=="Missing":


        score["PPE Violation"]=20



        factors.append(

        "🦺 PPE compliance failure"

        )


    else:


        score["PPE Violation"]=0




    return score,factors







# ==========================================================
# RISK EXPLANATION GENERATOR
# ==========================================================



def explain_prediction(

    sensor,

    risk,

    confidence

):



    contributions,factors = analyze_feature_contribution(

        sensor

    )





    total=sum(

        contributions.values()

    )




    if len(factors)==0:


        factors.append(

        "✅ All safety parameters within normal range"

        )






    return {



        "Prediction":

        risk,



        "Confidence":

        round(

            confidence,

            2

        ),



        "Risk Contribution":

        contributions,



        "Detected Factors":

        factors,



        "AI Reason":

        generate_reason(

            factors,

            risk

        ),



        "Generated":

        datetime.now().strftime(

            "%H:%M:%S"

        )


    }









# ==========================================================
# HUMAN READABLE AI REASON
# ==========================================================



def generate_reason(

    factors,

    risk

):


    if risk=="CRITICAL":


        return (

        "Multiple hazardous indicators "

        "combined to create a critical "

        "industrial safety condition."

        )



    elif risk=="WARNING":


        return (

        "Early warning signals detected. "

        "Preventive action recommended."

        )



    else:


        return (

        "Environmental parameters are "

        "within safe operating limits."

        )








# ==========================================================
# COMPLETE AI REPORT
# ==========================================================



def generate_ai_explanation(

    worker,

    zone,

    sensor,

    risk,

    confidence

):



    explanation=explain_prediction(

        sensor,

        risk,

        confidence

    )



    explanation.update(



    {


    "Worker":

    worker,


    "Zone":

    zone


    }



    )



    return explanation







# ==========================================================
# TEST
# ==========================================================


if __name__=="__main__":



    sensor={


    "Temperature":92,

    "Gas_Level":140,

    "Machine_Vibration":8,

    "Noise_Level":115,

    "Worker_Fatigue":90,

    "PPE_Status":"Missing"


    }



    result=generate_ai_explanation(

        "Worker-007",

        "Chemical Unit",

        sensor,

        "CRITICAL",

        97.8

    )



    print(result)