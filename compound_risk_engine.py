# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE COMPOUND RISK INTELLIGENCE ENGINE
# Version 2.0
# ==========================================================


from datetime import datetime
import random



# ==========================================================
# INDUSTRIAL SAFETY WEIGHTS
# ==========================================================


RISK_WEIGHTS = {


    "Gas Hazard":30,

    "Temperature Hazard":20,

    "Maintenance Conflict":20,

    "Permit Conflict":15,

    "Worker Exposure":10,

    "Shift Risk":5


}





# ==========================================================
# GAS INTELLIGENCE
# ==========================================================


def analyze_gas(sensor):


    risk=0

    reason=[]


    gas=sensor["Gas_Level"]



    if gas>=120:


        risk=30


        reason.append(

            "☣ Critical gas concentration detected"

        )


    elif gas>=80:


        risk=20


        reason.append(

            "⚠ Abnormal gas accumulation detected"

        )


    else:


        reason.append(

            "✅ Gas level normal"

        )



    return risk,reason





# ==========================================================
# TEMPERATURE INTELLIGENCE
# ==========================================================



def analyze_temperature(sensor):


    temp=sensor["Temperature"]


    risk=0

    reason=[]



    if temp>=85:


        risk=20


        reason.append(

            "🔥 Extreme temperature condition"

        )


    elif temp>=70:


        risk=10


        reason.append(

            "🌡 Temperature above safe range"

        )


    else:


        reason.append(

            "✅ Temperature normal"

        )


    return risk,reason





# ==========================================================
# MAINTENANCE RISK
# ==========================================================


def analyze_maintenance(status):


    if status=="ACTIVE":


        return (

            20,

            [

            "🛠 Active maintenance operation detected"

            ]

        )


    return (

        0,

        [

        "✅ No maintenance conflict"

        ]

    )





# ==========================================================
# PERMIT INTELLIGENCE
# ==========================================================



def analyze_permit(permit):


    if permit=="CONFLICT":


        return (

            15,

            [

            "🚧 Permit conflict detected"

            ]

        )



    return (

        0,

        [

        "✅ Permit status normal"

        ]

    )





# ==========================================================
# WORKER EXPOSURE ANALYSIS
# ==========================================================


def analyze_worker_exposure(sensor):


    fatigue=sensor["Worker_Fatigue"]


    if fatigue>=85:


        return (

            10,

            [

            "😴 High fatigue worker exposure"

            ]

        )


    elif fatigue>=70:


        return (

            5,

            [

            "⚠ Worker fatigue increasing"

            ]

        )


    return (

        0,

        [

        "✅ Worker condition normal"

        ]

    )





# ==========================================================
# SHIFT CHANGE INTELLIGENCE
# ==========================================================


def analyze_shift():


    current=datetime.now().hour



    if current in range(6,8) or current in range(18,20):


        return (

            5,

            [

            "🔄 Shift transition risk detected"

            ]

        )



    return (

        0,

        [

        "✅ Normal operation period"

        ]

    )





# ==========================================================
# MAIN COMPOUND RISK ENGINE
# ==========================================================



def calculate_compound_risk(

    sensor,

    maintenance_status="NORMAL",

    permit_status="VALID"

):



    total_score=0


    explanations=[]




    modules=[


        analyze_gas(sensor),


        analyze_temperature(sensor),


        analyze_maintenance(

            maintenance_status

        ),


        analyze_permit(

            permit_status

        ),


        analyze_worker_exposure(sensor),


        analyze_shift()


    ]




    for score,reasons in modules:


        total_score += score


        explanations.extend(

            reasons

        )





    total_score=min(

        total_score,

        100

    )




    # Incident prediction window


    if total_score>=80:


        level="CRITICAL"

        prediction="Incident probability high within 15-60 minutes"



    elif total_score>=50:


        level="WARNING"

        prediction="Potential hazard developing"



    else:


        level="SAFE"

        prediction="No immediate threat detected"






    return {


        "Compound_Risk_Score":

        total_score,


        "Risk_Level":

        level,


        "Prediction_Window":

        prediction,


        "AI_Reasoning":

        explanations,


        "Generated":

        datetime.now().strftime(

            "%H:%M:%S"

        )

    }






# ==========================================================
# TEST MODE
# ==========================================================


if __name__=="__main__":



    test_sensor={


        "Temperature":92,


        "Gas_Level":140,


        "Worker_Fatigue":90


    }



    result=calculate_compound_risk(

        test_sensor,

        "ACTIVE",

        "CONFLICT"

    )


    print(result)