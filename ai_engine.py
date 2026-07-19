# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE IoT SENSOR SIMULATOR
# Industrial Digital Twin Sensor Layer v2.0
# ==========================================================


import random
from datetime import datetime



FACTORY_ZONES = [

    "Chemical Processing Unit",
    "Steel Furnace",
    "Assembly Line",
    "Power Plant",
    "Storage Area"

]


WORKERS = [

    "Worker-001",
    "Worker-002",
    "Worker-003",
    "Worker-004",
    "Worker-005",
    "Worker-006"

]



def generate_live_sensor():


    return {


        "Worker":

        random.choice(WORKERS),



        "Zone":

        random.choice(FACTORY_ZONES),



        "Temperature":

        round(

            random.uniform(25,95),

            2

        ),



        "Gas_Level":

        round(

            random.uniform(20,150),

            2

        ),



        "Humidity":

        round(

            random.uniform(35,90),

            2

        ),



        "Machine_Vibration":

        round(

            random.uniform(0.5,10),

            2

        ),



        "Noise_Level":

        round(

            random.uniform(40,120),

            2

        ),



        "Worker_Fatigue":

        round(

            random.uniform(10,95),

            2

        ),



        "PPE_Status":

        random.choice(

            [

            "Available",

            "Missing"

            ]

        ),



        "Timestamp":

        datetime.now().strftime(

            "%H:%M:%S"

        )


    }