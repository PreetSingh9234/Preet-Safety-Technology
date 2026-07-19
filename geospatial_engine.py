# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE GEOSPATIAL SAFETY INTELLIGENCE ENGINE
# FACTORY DIGITAL TWIN v2.0
# ==========================================================


import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime



# ==========================================================
# FACTORY ZONE DATABASE
# ==========================================================


FACTORY_ZONES = {


    "Chemical Processing Unit":

    {

        "x":10,

        "y":80,

        "hazard":"HIGH"

    },


    "Steel Furnace Zone":

    {

        "x":80,

        "y":75,

        "hazard":"HIGH"

    },


    "Mining Operation Area":

    {

        "x":20,

        "y":30,

        "hazard":"MEDIUM"

    },


    "Assembly Line":

    {

        "x":70,

        "y":25,

        "hazard":"LOW"

    },


    "Power Generation Unit":

    {

        "x":50,

        "y":55,

        "hazard":"MEDIUM"

    }

}





# ==========================================================
# WORKER POSITION SIMULATOR
# ==========================================================



def generate_worker_locations():


    workers=[]


    for i in range(8):


        zone=random.choice(

            list(FACTORY_ZONES.keys())

        )


        base=FACTORY_ZONES[zone]



        workers.append(


            {


            "Worker":

            f"Worker-{i+1:03}",


            "Zone":

            zone,


            "X":

            base["x"]+random.randint(-8,8),


            "Y":

            base["y"]+random.randint(-8,8),


            "Risk":

            random.choice(

                [

                "SAFE",

                "WARNING",

                "CRITICAL"

                ]

            )


            }


        )


    return pd.DataFrame(workers)






# ==========================================================
# FACTORY HEATMAP GENERATOR
# ==========================================================



def generate_factory_map():



    data=[]



    for zone,info in FACTORY_ZONES.items():


        risk_value=random.randint(

            20,

            95

        )



        data.append(

            {


            "Zone":

            zone,


            "X":

            info["x"],


            "Y":

            info["y"],


            "Risk Score":

            risk_value,


            "Hazard":

            info["hazard"]


            }

        )




    df=pd.DataFrame(data)




    # Factory heatmap


    fig=px.scatter(


        df,


        x="X",


        y="Y",


        size="Risk Score",


        color="Risk Score",


        hover_name="Zone",


        text="Zone",


        title=

        "🏭 AI Factory Digital Twin - Risk Heatmap",


        size_max=60



    )




    fig.update_layout(


        height=600,


        template="plotly_dark",


        xaxis_title="Factory X Coordinate",


        yaxis_title="Factory Y Coordinate"


    )



    return fig






# ==========================================================
# WORKER TRACKING MAP
# ==========================================================



def generate_worker_tracking_map():



    workers=generate_worker_locations()



    fig=px.scatter(


        workers,


        x="X",


        y="Y",


        color="Risk",


        hover_name="Worker",


        hover_data=[

            "Zone"

        ],


        size=[20]*len(workers),


        title=

        "👷 Real-Time Worker Safety Tracking"


    )



    fig.update_layout(

        template="plotly_dark",

        height=600

    )



    return fig






# ==========================================================
# ZONE RISK SUMMARY
# ==========================================================



def get_zone_risk_summary():



    summary=[]



    for zone,data in FACTORY_ZONES.items():


        summary.append(


            {


            "Zone":

            zone,


            "Hazard Classification":

            data["hazard"],


            "Updated":

            datetime.now().strftime(

                "%H:%M:%S"

            )


            }


        )


    return pd.DataFrame(summary)





# ==========================================================
# TEST
# ==========================================================


if __name__=="__main__":


    print(

        get_zone_risk_summary()

    )