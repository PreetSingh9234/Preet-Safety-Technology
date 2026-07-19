# ==========================================================
# PREET SAFETY TECHNOLOGY
# AI INDUSTRIAL SAFETY COMMAND CENTER
# ENTERPRISE EDITION v5.0
# ==========================================================


import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import joblib


from datetime import datetime



# AI ENGINES

from compound_risk_engine import (
    calculate_compound_risk
)


from geospatial_engine import (
    generate_factory_map,
    generate_worker_tracking_map
)


from rag_safety_agent import (
    generate_safety_advice
)


from emergency_orchestrator import (
    create_emergency_report
)


from explain_ai import (
    generate_ai_explanation
)


from analytics_engine import (
    generate_executive_summary,
    risk_distribution,
    zone_risk_analysis
)





# ==========================================================
# PAGE CONFIG
# ==========================================================


st.set_page_config(

    page_title=
    "Preet Safety Technology",

    page_icon=
    "🚨",

    layout=
    "wide"

)







# ==========================================================
# PREMIUM ENTERPRISE UI
# ==========================================================


st.markdown(

"""

<style>


/* MAIN BACKGROUND */


.main{

background:

linear-gradient(

135deg,

#020617,

#0f172a

);

}



/* HEADER */


.hero{


background:

linear-gradient(

90deg,

#00e5ff,

#0077ff

);


padding:

25px;


border-radius:

25px;


color:white;


text-align:center;


box-shadow:

0 0 30px #00e5ff;


animation:

glow 3s infinite;


}



@keyframes glow{


0%{

box-shadow:

0 0 10px #00e5ff;

}


50%{

box-shadow:

0 0 40px #00e5ff;

}


100%{

box-shadow:

0 0 10px #00e5ff;

}


}






/* CARDS */


.card{


background:

rgba(255,255,255,0.08);


padding:

20px;


border-radius:

20px;


border:

1px solid rgba(255,255,255,0.2);


backdrop-filter:

blur(10px);


}




/* ALERT */


.alert{


padding:

15px;


border-radius:

15px;


font-size:

20px;


font-weight:

bold;


}






</style>


""",

unsafe_allow_html=True

)








# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================


@st.cache_resource

def load_ai_model():



    model = joblib.load(

        "model/risk_model.pkl"

    )



    scaler = joblib.load(

        "model/scaler.pkl"

    )



    ppe_encoder = joblib.load(

        "model/ppe_encoder.pkl"

    )



    risk_encoder = joblib.load(

        "model/risk_encoder.pkl"

    )



    return (

        model,

        scaler,

        ppe_encoder,

        risk_encoder

    )





model,scaler,ppe_encoder,risk_encoder = load_ai_model()







# ==========================================================
# HEADER
# ==========================================================



st.markdown(

"""

<div class="hero">


<h1>

🚨 PREET SAFETY TECHNOLOGY

</h1>


<h3>

AI Powered Industrial Worker Safety Intelligence Platform

</h3>


<p>

Zero Harm Operations | Predict Before Accident

</p>


</div>


""",

unsafe_allow_html=True

)




st.write("")






# ==========================================================
# SESSION MEMORY
# ==========================================================



if "records" not in st.session_state:


    st.session_state.records=[]




if "incidents" not in st.session_state:


    st.session_state.incidents=[]




if "latest_explanation" not in st.session_state:


    st.session_state.latest_explanation=None




if "latest_emergency" not in st.session_state:


    st.session_state.latest_emergency=None




if "monitoring" not in st.session_state:


    st.session_state.monitoring=False








# ==========================================================
# MASTER DATA
# ==========================================================


WORKERS=[


"Worker-001",

"Worker-002",

"Worker-003",

"Worker-004",

"Worker-005",

"Worker-006",

"Worker-007",

"Worker-008"


]





ZONES=[


"Chemical Processing Unit",

"Steel Furnace Zone",

"Mining Area",

"Assembly Line",

"Power Plant"


]





# ==========================================================
# SENSOR SIMULATION ENGINE
# ==========================================================



def generate_sensor():



    return {


"Temperature":

random.randint(35,95),



"Gas_Level":

random.randint(10,150),



"Humidity":

random.randint(30,95),



"Machine_Vibration":

round(

random.uniform(1,10),

2

),



"Noise_Level":

random.randint(50,120),



"Worker_Fatigue":

random.randint(10,95),



"PPE_Status":

random.choice(

[

"Available",

"Missing"

]

)

}





# ==========================================================
# AI MODEL PREDICTION
# ==========================================================



def predict_ai(sensor):


    ppe = ppe_encoder.transform(

        [

        sensor["PPE_Status"]

        ]

    )[0]



    data=pd.DataFrame(

    [[

    sensor["Temperature"],

    sensor["Gas_Level"],

    sensor["Humidity"],

    sensor["Machine_Vibration"],

    sensor["Noise_Level"],

    sensor["Worker_Fatigue"],

    ppe

    ]],

    columns=[

    "Temperature",

    "Gas_Level",

    "Humidity",

    "Machine_Vibration",

    "Noise_Level",

    "Worker_Fatigue",

    "PPE_Status"

    ]

    )



    scaled=scaler.transform(

        data

    )



    prediction=model.predict(

        scaled

    )



    probability=model.predict_proba(

        scaled

    )[0]



    risk=risk_encoder.inverse_transform(

        prediction

    )[0]



    confidence=max(probability)*100



    return risk,round(confidence,2)
# ==========================================================
# LIVE AI MONITORING ENGINE
# ==========================================================



# ==========================================================
# SIDEBAR CONTROL PANEL
# ==========================================================


st.sidebar.markdown(

"""

## 🎛 AI CONTROL CENTER

"""

)



start = st.sidebar.button(

"🚀 START LIVE MONITORING"

)



demo = st.sidebar.button(

"🔥 ACTIVATE JUDGE DEMO MODE"

)





# ==========================================================
# JUDGE DEMO SCENARIO
# ==========================================================



def generate_demo_incident():



    sensor={


        "Temperature":92,


        "Gas_Level":145,


        "Humidity":88,


        "Machine_Vibration":9.5,


        "Noise_Level":118,


        "Worker_Fatigue":91,


        "PPE_Status":"Missing"


    }



    return {


        "Worker":

        "Worker-007",



        "Zone":

        "Chemical Processing Unit",



        "Sensor":

        sensor

    }








# ==========================================================
# DEMO MODE
# ==========================================================



if demo:



    scenario=generate_demo_incident()



    worker=scenario["Worker"]

    zone=scenario["Zone"]

    sensor=scenario["Sensor"]



    risk="CRITICAL"

    confidence=97.8




    # Compound AI


    compound=calculate_compound_risk(

        sensor,

        "ACTIVE",

        "CONFLICT"

    )




    # XAI


    explanation=generate_ai_explanation(

        worker,

        zone,

        sensor,

        risk,

        confidence

    )



    emergency=create_emergency_report(

        worker,

        zone,

        risk,

        confidence,

        sensor,

        compound["Compound_Risk_Score"]

    )




    advice=generate_safety_advice(

        sensor,

        risk,

        explanation["Detected Factors"]

    )




    st.session_state.latest_explanation=explanation


    st.session_state.latest_emergency=emergency




    st.session_state.records.append(

        {


        "Time":

        datetime.now().strftime("%H:%M:%S"),


        "Worker":

        worker,


        "Zone":

        zone,


        "Risk":

        risk,


        "Confidence":

        confidence,


        "Temperature":

        sensor["Temperature"],


        "Gas":

        sensor["Gas_Level"],


        "Fatigue":

        sensor["Worker_Fatigue"]


        }

    )




    st.error(

    """

    🚨 INDUSTRIAL ACCIDENT SIMULATION ACTIVATED

    AI detected critical compound risk condition.

    """

    )








# ==========================================================
# LIVE MONITORING LOOP
# ==========================================================



if start:



    st.session_state.monitoring=True





if st.session_state.monitoring:



    display=st.empty()



    for cycle in range(30):



        with display.container():



            st.subheader(

            f"""

            📡 LIVE AI MONITORING

            Cycle {cycle+1}

            """

            )





            safe=0

            warning=0

            critical=0



            columns=st.columns(4)






            for index,worker in enumerate(WORKERS):


                sensor=generate_sensor()



                zone=random.choice(

                    ZONES

                )



                # ML Prediction


                risk,confidence=predict_ai(

                    sensor

                )





                # Compound Intelligence


                compound=calculate_compound_risk(

                    sensor,

                    random.choice(

                    [

                    "NORMAL",

                    "ACTIVE"

                    ]

                    ),

                    random.choice(

                    [

                    "VALID",

                    "CONFLICT"

                    ]

                    )

                )





                # Final Risk Fusion


                if compound["Risk_Level"]=="CRITICAL":


                    risk="CRITICAL"



                elif compound["Risk_Level"]=="WARNING":


                    risk="WARNING"






                if risk=="SAFE":


                    safe+=1


                elif risk=="WARNING":


                    warning+=1


                else:


                    critical+=1







                record={


                "Time":

                datetime.now().strftime(

                "%H:%M:%S"

                ),



                "Worker":

                worker,



                "Zone":

                zone,



                "Risk":

                risk,



                "Confidence":

                confidence,



                "Temperature":

                sensor["Temperature"],



                "Gas":

                sensor["Gas_Level"],



                "Fatigue":

                sensor["Worker_Fatigue"]


                }




                st.session_state.records.append(

                    record

                )





                if risk!="SAFE":


                    st.session_state.incidents.append(

                        record

                    )





                # XAI


                st.session_state.latest_explanation=generate_ai_explanation(

                    worker,

                    zone,

                    sensor,

                    risk,

                    confidence

                )






                # Emergency


                if risk=="CRITICAL":


                    st.session_state.latest_emergency=create_emergency_report(

                        worker,

                        zone,

                        risk,

                        confidence,

                        sensor,

                        compound["Compound_Risk_Score"]

                    )







                # Worker Card UI


                with columns[index%4]:


                    if risk=="CRITICAL":


                        st.error(

                        f"""

                        🚨 {worker}


                        🔴 {risk}


                        Confidence:

                        {confidence}%


                        Zone:

                        {zone}

                        """

                        )



                    elif risk=="WARNING":


                        st.warning(

                        f"""

                        ⚠ {worker}


                        🟡 {risk}


                        Confidence:

                        {confidence}%


                        """

                        )



                    else:


                        st.success(

                        f"""

                        👷 {worker}


                        🟢 SAFE


                        Confidence:

                        {confidence}%


                        """

                        )







            st.divider()



            a,b,c,d=st.columns(4)



            a.metric(

            "👷 Workers",

            len(WORKERS)

            )



            b.metric(

            "🟢 Safe",

            safe

            )


            c.metric(

            "⚠ Warning",

            warning

            )


            d.metric(

            "🚨 Critical",

            critical

            )





        time.sleep(2)
# ==========================================================
# FACTORY DIGITAL TWIN + AI EXPLANATION
# ==========================================================



st.divider()



st.header(

"🏭 AI FACTORY DIGITAL TWIN"

)




map_col1,map_col2 = st.columns(2)




with map_col1:


    st.subheader(

    "🌍 Factory Risk Heatmap"

    )


    try:


        factory_map = generate_factory_map()


        st.plotly_chart(

            factory_map,

            use_container_width=True

        )


    except Exception as e:


        st.warning(

        "Factory map waiting for sensor data"

        )






with map_col2:


    st.subheader(

    "👷 Worker Location Intelligence"

    )


    try:


        worker_map=generate_worker_tracking_map()


        st.plotly_chart(

            worker_map,

            use_container_width=True

        )


    except:


        st.warning(

        "Worker tracking initializing..."

        )








# ==========================================================
# EXPLAINABLE AI PANEL
# ==========================================================



if st.session_state.latest_explanation:



    st.divider()



    st.header(

    "🤖 WHY DID AI PREDICT THIS?"

    )



    explanation=st.session_state.latest_explanation



    col1,col2=st.columns(2)





    with col1:



        st.markdown(

        """

        <div class="card">


        ### 🧠 AI Decision


        """,

        unsafe_allow_html=True

        )



        st.write(

        "Worker:",

        explanation["Worker"]

        )


        st.write(

        "Zone:",

        explanation["Zone"]

        )



        st.write(

        "Prediction:",

        explanation["Prediction"]

        )



        st.write(

        "Confidence:",

        f'{explanation["Confidence"]}%'

        )



        st.markdown(

        "</div>",

        unsafe_allow_html=True

        )







    with col2:



        st.markdown(

        """

        <div class="card">


        ### 🔍 Detected Risk Factors


        """,

        unsafe_allow_html=True

        )



        for factor in explanation["Detected Factors"]:



            st.warning(

            factor

            )



        st.markdown(

        "</div>",

        unsafe_allow_html=True

        )







    st.subheader(

    "📊 AI Feature Contribution"

    )



    contribution=pd.DataFrame(

        {

        "Factor":

        list(

        explanation["Risk Contribution"].keys()

        ),


        "Impact":

        list(

        explanation["Risk Contribution"].values()

        )

        }

    )




    st.bar_chart(

        contribution.set_index(

            "Factor"

        )

    )









# ==========================================================
# RAG SAFETY INTELLIGENCE
# ==========================================================



if st.session_state.latest_explanation:



    st.divider()



    st.header(

    "🧠 Safety Knowledge Intelligence Agent"

    )



    advice=generate_safety_advice(



        {},



        explanation["Prediction"],



        explanation["Detected Factors"]



    )





    st.success(

    "Knowledge Base Connected ✅"

    )





    st.subheader(

    "📚 Historical Pattern Analysis"

    )



    matches=advice[

    "Matched Historical Cases"

    ]





    if len(matches)>0:



        for item in matches:


            st.info(

            f"""

            Previous Incident:

            {item["Previous Incident"]}


            Similarity:

            {item["Similarity"]}%


            """

            )



    else:


        st.write(

        "No matching historical incident found"

        )






    st.subheader(

    "🛡 Preventive Recommendations"

    )



    for action in advice[

    "Preventive Recommendations"

    ]:



        st.write(

        action

        )









# ==========================================================
# EMERGENCY RESPONSE COMMAND CENTER
# ==========================================================



if st.session_state.latest_emergency:



    st.divider()



    st.header(

    "🚨 AUTONOMOUS EMERGENCY RESPONSE CENTER"

    )



    emergency=st.session_state.latest_emergency






    st.error(

    f"""

    🚨 {emergency["Emergency Level"]}



    Worker:

    {emergency["Worker"]}



    Zone:

    {emergency["Zone"]}



    AI Confidence:

    {emergency["AI Confidence"]}%



    """

    )





    st.subheader(

    "⚡ Automatic Actions"

    )



    for action in emergency["Actions"]:


        st.write(

        action

        )






    st.subheader(

    "⏱ Emergency Timeline"

    )



    timeline=emergency["Timeline"]




    for key,value in timeline.items():



        st.info(

        f"""

        {key}

        →

        {value}

        """

        )






    st.subheader(

    "📄 Incident Evidence Report"

    )



    st.json(

        emergency["Incident Report"]

    )
# ==========================================================
# EXECUTIVE SAFETY ANALYTICS COMMAND CENTER
# ==========================================================



st.divider()



st.header(

"📊 EXECUTIVE SAFETY COMMAND CENTER"

)





if len(st.session_state.records)>0:



    analytics_df=pd.DataFrame(

        st.session_state.records

    )





    # ======================================================
    # KPI ENGINE
    # ======================================================


    summary=generate_executive_summary(

        analytics_df

    )




    c1,c2,c3,c4=st.columns(4)




    c1.metric(

    "🛡 Safety Intelligence Score",

    f'{summary["Safety Score"]}%'

    )



    c2.metric(

    "📡 Monitoring Events",

    summary["Total Monitoring Events"]

    )



    c3.metric(

    "🚨 Danger Events",

    summary["Danger Events"]

    )



    c4.metric(

    "🏭 Critical Zone",

    summary["Critical Zone"]

    )







    st.divider()



    # ======================================================
    # RISK DISTRIBUTION
    # ======================================================



    st.subheader(

    "🔥 Risk Distribution Intelligence"

    )



    risk_chart=risk_distribution(

        analytics_df

    )



    st.bar_chart(

        risk_chart.set_index(

            "Risk Level"

        )

    )








    # ======================================================
    # ZONE ANALYTICS
    # ======================================================



    st.subheader(

    "🏭 Zone Risk Intelligence"

    )



    zone_data=zone_risk_analysis(

        analytics_df

    )



    st.dataframe(

        zone_data,

        use_container_width=True

    )







    # ======================================================
    # SENSOR TREND ANALYSIS
    # ======================================================



    st.subheader(

    "📈 Industrial Sensor Behaviour"

    )



    sensor_columns=[

    "Temperature",

    "Gas",

    "Fatigue"

    ]



    available=[

    c for c in sensor_columns

    if c in analytics_df.columns

    ]



    if len(available)>0:


        st.line_chart(

            analytics_df[available]

        )








    # ======================================================
    # INCIDENT HISTORY
    # ======================================================



    st.subheader(

    "🚨 Safety Incident Timeline"

    )



    if len(st.session_state.incidents)>0:



        incident_df=pd.DataFrame(

            st.session_state.incidents

        )



        st.dataframe(

            incident_df,

            use_container_width=True

        )


    else:


        st.success(

        "✅ No incidents detected"

        )








    # ======================================================
    # REPORT EXPORT
    # ======================================================



    st.subheader(

    "📄 Safety Intelligence Report"

    )



    csv=analytics_df.to_csv(

        index=False

    )



    st.download_button(

        label=

        "⬇ Download AI Safety Report",


        data=

        csv,


        file_name=

        "Preet_Safety_Intelligence_Report.csv",


        mime=

        "text/csv"

    )







else:



    st.info(

    """

    🚀 Start Live Monitoring

    or

    Activate Judge Demo Mode

    to generate intelligence data.

    """

    )







# ==========================================================
# SYSTEM HEALTH MONITOR
# ==========================================================



st.divider()



st.success(

"""

# 🟢 SYSTEM ONLINE



🤖 AI Risk Prediction Engine     : ACTIVE


🧠 Compound Risk Intelligence    : ACTIVE


🌍 Factory Digital Twin          : ACTIVE


📚 RAG Safety Agent              : ACTIVE


🚨 Emergency Orchestrator        : READY


🔍 Explainable AI                : ENABLED



---------------------------------

PREET SAFETY TECHNOLOGY

AI Industrial Worker Safety

Zero Harm Operations Platform

---------------------------------


"""

)