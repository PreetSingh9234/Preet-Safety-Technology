# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE SAFETY ANALYTICS INTELLIGENCE ENGINE
# Executive Command Center Analytics v2.0
# ==========================================================


import pandas as pd
import numpy as np

from datetime import datetime



# ==========================================================
# SAFETY INTELLIGENCE SCORE
# ==========================================================


def calculate_safety_intelligence_score(data):


    if len(data)==0:

        return 0



    total=len(data)


    critical=len(

        data[

            data["Risk"]=="CRITICAL"

        ]

    )


    warning=len(

        data[

            data["Risk"]=="WARNING"

        ]

    )



    penalty=(

        critical*2

        +

        warning

    )



    score=100-(

        penalty/total*100

    )



    return round(

        max(

            0,

            min(

                score,

                100

            )

        ),

        2

    )







# ==========================================================
# RISK DISTRIBUTION
# ==========================================================



def risk_distribution(data):


    result=(


        data["Risk"]

        .value_counts()

        .reset_index()

    )



    result.columns=[

        "Risk Level",

        "Count"

    ]



    return result







# ==========================================================
# ZONE INTELLIGENCE
# ==========================================================



def zone_risk_analysis(data):


    zone=(


        data

        .groupby(

            [

            "Zone",

            "Risk"

            ]

        )

        .size()

        .reset_index(

            name="Events"

        )

    )



    return zone






# ==========================================================
# MOST DANGEROUS ZONE FINDER
# ==========================================================



def highest_risk_zone(data):


    critical=data[

        data["Risk"]=="CRITICAL"

    ]



    if len(critical)==0:


        return "No Critical Zone"




    result=(


        critical

        ["Zone"]

        .value_counts()

        .idxmax()

    )



    return result







# ==========================================================
# INCIDENT INTELLIGENCE
# ==========================================================



def incident_pattern_analysis(data):


    incidents=data[

        data["Risk"]!="SAFE"

    ]



    report={


        "Total Incidents":

        len(incidents),



        "Critical Cases":

        len(

            incidents[

            incidents["Risk"]

            =="CRITICAL"

            ]

        ),



        "Warning Cases":

        len(

            incidents[

            incidents["Risk"]

            =="WARNING"

            ]

        )

    }



    return report







# ==========================================================
# SENSOR TREND ENGINE
# ==========================================================



def sensor_trend_analysis(data):


    sensors=[


        "Temperature",

        "Gas",

        "Fatigue"


    ]



    available=[

        x for x in sensors

        if x in data.columns

    ]



    if len(available)==0:


        return pd.DataFrame()



    return data[available]







# ==========================================================
# EXECUTIVE DASHBOARD SUMMARY
# ==========================================================



def generate_executive_summary(data):



    summary={



        "Safety Score":

        calculate_safety_intelligence_score(

            data

        ),



        "Total Monitoring Events":

        len(data),



        "Danger Events":

        len(

            data[

            data["Risk"]!="SAFE"

            ]

        ),



        "Critical Zone":

        highest_risk_zone(

            data

        ),



        "Generated":

        datetime.now().strftime(

            "%H:%M:%S"

        )



    }



    return summary







# ==========================================================
# EXPORT REPORT
# ==========================================================



def export_analytics_report(data):


    filename=(


        "Preet_Safety_Analytics_"

        +

        datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        +

        ".csv"


    )



    data.to_csv(

        filename,

        index=False

    )



    return filename







# ==========================================================
# TEST
# ==========================================================


if __name__=="__main__":


    sample=pd.DataFrame(

    {


    "Zone":[

    "Chemical",

    "Mining",

    "Chemical"

    ],


    "Risk":[

    "CRITICAL",

    "SAFE",

    "WARNING"

    ]


    }

    )


    print(

        generate_executive_summary(

            sample

        )

    )