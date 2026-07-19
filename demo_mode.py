# ==========================================================
# PREET SAFETY TECHNOLOGY
# PHASE 5 - HACKATHON DEMO MODE
# INDUSTRIAL ACCIDENT SIMULATOR
# ==========================================================


from datetime import datetime

from explain_ai import (
    generate_ai_explanation
)


from emergency_response import (
    create_emergency_report
)



# ==========================================================
# INDUSTRIAL ACCIDENT SCENARIOS
# ==========================================================


def generate_accident_scenario():



    scenario = {


        "Worker":

        "Worker-007",



        "Zone":

        "Chemical Processing Unit",



        "Sensor":

        {


            "Temperature":

            92,


            "Gas_Level":

            145,


            "Humidity":

            88,


            "Machine_Vibration":

            9.5,


            "Noise_Level":

            118,


            "Worker_Fatigue":

            91,


            "PPE_Status":

            "Missing"


        },


        "Risk":

        "CRITICAL",


        "Confidence":

        97.8


    }


    return scenario





# ==========================================================
# DEMO EXECUTION ENGINE
# ==========================================================


def run_demo():



    print("\n")

    print("="*60)

    print("🚨 PREET SAFETY TECHNOLOGY")

    print("🏭 INDUSTRIAL ACCIDENT SIMULATION")

    print("="*60)



    scenario = generate_accident_scenario()



    print("\n🔥 INCIDENT DETECTED")



    print(

        "Worker:",

        scenario["Worker"]

    )


    print(

        "Zone:",

        scenario["Zone"]

    )



    print("\n📡 SENSOR DATA")



    for key,value in scenario["Sensor"].items():

        print(

            key,

            ":",

            value

        )




    print("\n🤖 AI ANALYSIS")



    explanation = generate_ai_explanation(

        scenario["Worker"],

        scenario["Zone"],

        scenario["Sensor"],

        scenario["Risk"],

        scenario["Confidence"]

    )




    print("\nRisk:")

    print(

        explanation["Risk_Level"]

    )



    print("\nWhy AI Predicted This:")



    for reason in explanation["Detected_Factors"]:

        print(

            " -",

            reason

        )




    print("\n🚨 EMERGENCY RESPONSE")



    response = create_emergency_report(

        scenario["Worker"],

        scenario["Zone"],

        scenario["Risk"],

        scenario["Confidence"]

    )




    print(

        "\nEmergency Level:",

        response["Emergency Level"]

    )




    print("\nActions:")



    for action in response["Actions"]:

        print(

            " -",

            action

        )




    print("\nTimeline:")



    for key,value in response["Timeline"].items():

        print(

            key,

            ":",

            value

        )




    print("\nGenerated:")

    print(

        datetime.now().strftime(

            "%H:%M:%S"

        )

    )


    print("\n")

    print("="*60)

    print("🏆 DEMO COMPLETED")

    print("="*60)







# ==========================================================
# RUN
# ==========================================================


if __name__ == "__main__":


    run_demo()