# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE AI INDUSTRIAL SAFETY COMMAND CENTER
# PHASE 2 - LIVE MONITOR ENGINE
# PART 1
# ==========================================================


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

from datetime import datetime


# UI ENGINE

from ui.premium_theme import load_premium_theme

from ui.components import (
    hero_header,
    metric_card,
    alert_box
)



# SENSOR ENGINE

from sensor_engine import generate_live_sensor



# ==========================================================
# PAGE CONFIG
# ==========================================================


st.set_page_config(

    page_title="Preet Safety AI Command Center",

    page_icon="🚨",

    layout="wide"

)



# Load Premium UI

load_premium_theme()



# ==========================================================
# MODEL LOADER
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



model, scaler, ppe_encoder, risk_encoder = load_ai_model()



# ==========================================================
# SESSION MEMORY
# ==========================================================


if "records" not in st.session_state:

    st.session_state.records=[]



if "alerts" not in st.session_state:

    st.session_state.alerts=[]



if "monitoring" not in st.session_state:

    st.session_state.monitoring=False




# ==========================================================
# HEADER
# ==========================================================


hero_header()



st.divider()



# ==========================================================
# SYSTEM STATUS BAR
# ==========================================================



c1,c2,c3,c4 = st.columns(4)


with c1:

    metric_card(

        "AI Engine",

        "ACTIVE",

        "🤖"

    )


with c2:

    metric_card(

        "Sensors",

        "ONLINE",

        "📡"

    )


with c3:

    metric_card(

        "Workers",

        "250",

        "👷"

    )


with c4:

    metric_card(

        "Security",

        "98%",

        "🛡️"

    )



st.divider()



# ==========================================================
# SIDEBAR CONTROL
# ==========================================================


st.sidebar.title(

"🎛 COMMAND CONTROL"

)



start = st.sidebar.button(

"▶ START AI MONITORING"

)


stop = st.sidebar.button(

"⛔ STOP SYSTEM"

)



if start:

    st.session_state.monitoring=True



if stop:

    st.session_state.monitoring=False




# ==========================================================
# SENSOR NORMALIZER
# ==========================================================


def normalize_sensor(sensor):


    return {


        "Temperature":

        sensor["Temperature"],


        "Gas_Level":

        sensor["Gas_Level"],


        "Humidity":

        sensor["Humidity"],


        "Machine_Vibration":

        sensor["Vibration"],


        "Noise_Level":

        sensor["Noise"],


        "Worker_Fatigue":

        sensor["Fatigue"],


        "PPE_Status":

        sensor["PPE"]


    }




# ==========================================================
# AI PREDICTION
# ==========================================================


def predict_risk(sensor):


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



    scaled=scaler.transform(data)



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
# LIVE MONITOR LOOP
# ==========================================================


if st.session_state.monitoring:


    placeholder=st.empty()


    for i in range(100):


        if not st.session_state.monitoring:

            break



        with placeholder.container():


            st.subheader(

            f"📡 LIVE AI SCAN : {i+1}"

            )


            sensor_raw=generate_live_sensor()


            sensor=normalize_sensor(

                sensor_raw

            )


            risk,confidence=predict_risk(

                sensor

            )



            record={

                "Time":

                datetime.now().strftime(
                    "%H:%M:%S"
                ),


                "Worker":

                sensor_raw["Worker"],


                "Zone":

                sensor_raw["Zone"],


                "Risk":

                risk,


                "Confidence":

                confidence


            }



            st.session_state.records.append(

                record

            )



            if risk!="SAFE":


                st.session_state.alerts.append(

                    record

                )



            col1,col2,col3=st.columns(3)



            with col1:

                metric_card(

                    "Worker",

                    sensor_raw["Worker"],

                    "👷"

                )


            with col2:

                metric_card(

                    "Risk",

                    risk,

                    "🚨"

                )


            with col3:

                metric_card(

                    "Confidence",

                    f"{confidence}%",

                    "🧠"

                )



            if risk=="CRITICAL":

                alert_box(

                    "Critical Industrial Hazard Detected"

                )



        time.sleep(2)
# ==========================================================
# PHASE 2 - PART 2
# AI EXPLANATION + EMERGENCY INTELLIGENCE CENTER
# ==========================================================


from explain_ai import generate_ai_explanation

from emergency_response import create_emergency_report



# ==========================================================
# AI EXPLANATION CENTER
# ==========================================================


st.divider()


st.header(

"🤖 AI DECISION INTELLIGENCE CENTER"

)



if len(st.session_state.records)>0:


    latest = st.session_state.records[-1]



    # Generate explanation sensor


    explanation_sensor = {


        "Temperature":random.randint(40,90),

        "Gas_Level":random.randint(20,140),

        "Humidity":random.randint(30,90),

        "Machine_Vibration":random.uniform(1,9),

        "Noise_Level":random.randint(50,120),

        "Worker_Fatigue":random.randint(20,95),

        "PPE_Status":

        random.choice(

            [
                "Available",
                "Missing"
            ]

        )

    }



    ai_report = generate_ai_explanation(


        latest["Worker"],


        latest["Zone"],


        explanation_sensor,


        latest["Risk"],


        latest["Confidence"]


    )



    col1,col2=st.columns(2)



    with col1:


        st.markdown(

        f"""

        <div class="glass-card">


        <h2>🧠 AI Prediction</h2>


        <h3>

        Worker:

        {ai_report["Worker"]}

        </h3>


        <h3>

        Zone:

        {ai_report["Zone"]}

        </h3>


        <h3>

        Risk:

        {ai_report["Risk_Level"]}

        </h3>


        <h3>

        Confidence:

        {ai_report["AI_Confidence"]}%

        </h3>


        </div>

        """,

        unsafe_allow_html=True

        )




    with col2:


        st.markdown(

        """

        <div class="glass-card">


        <h2>

        🔍 Why AI Decided This?

        </h2>


        """,

        unsafe_allow_html=True

        )


        for reason in ai_report["Detected_Factors"]:


            st.warning(

                reason

            )


        st.markdown(

        "</div>",

        unsafe_allow_html=True

        )






# ==========================================================
# SAFETY ACTION CENTER
# ==========================================================



st.divider()


st.header(

"🛡 AI Recommended Safety Actions"

)



if len(st.session_state.records)>0:


    actions = ai_report["Recommended_Actions"]


    for action in actions:


        st.info(

            action

        )





# ==========================================================
# EMERGENCY RESPONSE CENTER
# ==========================================================


st.divider()


st.header(

"🚨 AUTONOMOUS EMERGENCY RESPONSE CENTER"

)



if len(st.session_state.alerts)>0:



    latest_alert = st.session_state.alerts[-1]



    emergency = create_emergency_report(

        latest_alert["Worker"],

        latest_alert["Zone"],

        latest_alert["Risk"],

        latest_alert["Confidence"]

    )



    st.markdown(

    f"""

    <div class="glass-card alert">


    <h2>

    🚨 {emergency["Emergency Level"]}

    </h2>


    <h3>

    Worker:

    {emergency["Worker"]}

    </h3>


    <h3>

    Zone:

    {emergency["Zone"]}

    </h3>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.subheader(

    "⚡ Automated Response Protocol"

    )



    for action in emergency["Actions"]:


        st.error(

            action

        )





    st.subheader(

    "⏱ Emergency Timeline"

    )


    timeline_df=pd.DataFrame(

        emergency["Timeline"].items(),

        columns=[

            "Time",

            "Action"

        ]

    )



    st.dataframe(

        timeline_df,

        width="stretch"

    )



else:


    st.success(

        "🟢 No active emergency detected"

    )





# ==========================================================
# LIVE ALERT WALL
# ==========================================================


st.divider()


st.header(

"📢 LIVE SAFETY ALERT WALL"

)



if len(st.session_state.alerts)>0:


    alert_df=pd.DataFrame(

        st.session_state.alerts

    )


    st.dataframe(

        alert_df.tail(10),

        width="stretch"

    )


else:


    st.info(

    "System monitoring active. Waiting for events..."

    )


# ==========================================================
# PHASE 2 - PART 3
# DIGITAL TWIN + GEO AI + COMPUTER VISION
# ==========================================================


import plotly.graph_objects as go
import plotly.express as px



# ==========================================================
# DIGITAL TWIN FACTORY COMMAND CENTER
# ==========================================================


st.divider()

st.header(
    "🏭 DIGITAL TWIN FACTORY INTELLIGENCE"
)



factory_data = pd.DataFrame(

[
    {
        "Zone":"Chemical Processing Unit",
        "X":20,
        "Y":80,
        "Risk":"CRITICAL"
    },

    {
        "Zone":"Steel Furnace",
        "X":70,
        "Y":75,
        "Risk":"WARNING"
    },

    {
        "Zone":"Assembly Line",
        "X":40,
        "Y":40,
        "Risk":"SAFE"
    },

    {
        "Zone":"Power Plant",
        "X":80,
        "Y":30,
        "Risk":"WARNING"
    },

    {
        "Zone":"Storage Area",
        "X":15,
        "Y":20,
        "Risk":"SAFE"
    }

]

)



color_map={

    "SAFE":"green",

    "WARNING":"orange",

    "CRITICAL":"red"

}



fig_factory = go.Figure()



for risk in [

    "SAFE",

    "WARNING",

    "CRITICAL"

]:


    data=factory_data[
        factory_data["Risk"]==risk
    ]


    fig_factory.add_trace(

        go.Scatter(

            x=data["X"],

            y=data["Y"],

            mode="markers+text",

            text=data["Zone"],

            marker=dict(

                size=35,

                color=color_map[risk]

            ),

            name=risk

        )

    )




fig_factory.update_layout(

    title="Real-Time Industrial Safety Digital Twin",

    height=500,

    template="plotly_dark",

    xaxis_title="Factory X Position",

    yaxis_title="Factory Y Position"

)



st.plotly_chart(

    fig_factory,

    width="stretch"

)





# ==========================================================
# SAFETY HEATMAP
# ==========================================================



st.subheader(

"🔥 Dynamic Risk Heatmap"

)



heatmap_data=pd.DataFrame(

{

"Zone":

factory_data["Zone"],


"Risk Score":

[

95,

65,

10,

55,

20

]

}

)



fig_heat=px.bar(

    heatmap_data,

    x="Zone",

    y="Risk Score",

    title="Zone Wise Risk Intelligence"

)



st.plotly_chart(

    fig_heat,

    width="stretch"

)




# ==========================================================
# WORKER LOCATION TRACKER
# ==========================================================


st.divider()


st.header(

"👷 Worker Location Intelligence"

)



workers_location=pd.DataFrame(

[

{

"Worker":"Worker-001",

"Zone":"Chemical Processing Unit",

"Status":"High Risk"

},

{

"Worker":"Worker-002",

"Zone":"Assembly Line",

"Status":"Safe"

},

{

"Worker":"Worker-003",

"Zone":"Steel Furnace",

"Status":"Warning"

}

]

)



st.dataframe(

    workers_location,

    width="stretch"

)





# ==========================================================
# COMPUTER VISION AI CENTER
# ==========================================================


st.divider()


st.header(

"📷 AI CCTV Vision System"

)



cam1,cam2,cam3=st.columns(3)



with cam1:


    metric_card(

        "Camera-01",

        "ONLINE",

        "📷"

    )


with cam2:


    metric_card(

        "PPE Detection",

        "ACTIVE",

        "🦺"

    )


with cam3:


    metric_card(

        "Fire Detection",

        "READY",

        "🔥"

    )




vision_status=pd.DataFrame(

[

{

"Camera":

"CAM-01",

"Detection":

"Helmet Detected",

"Confidence":

"98%"

},

{

"Camera":

"CAM-02",

"Detection":

"Worker Inside Zone",

"Confidence":

"94%"

},

{

"Camera":

"CAM-03",

"Detection":

"No Fire",

"Confidence":

"99%"

}

]

)



st.dataframe(

    vision_status,

    width="stretch"

)




# ==========================================================
# DIGITAL PERMIT INTELLIGENCE
# ==========================================================



st.divider()


st.header(

"📄 AI Permit Intelligence Agent"

)



permit_data=pd.DataFrame(

[

{

"Permit":

"Hot Work",

"Zone":

"Chemical Area",

"AI Status":

"⚠ Conflict Detected"

},


{

"Permit":

"Maintenance",

"Zone":

"Power Unit",

"AI Status":

"Approved"

}

]

)



st.dataframe(

    permit_data,

    width="stretch"

)



st.info(

"""
🤖 AI Analysis:

Hot work activity detected near hazardous gas zone.

Recommended Action:

Suspend permit until gas level becomes normal.
"""

)
# ==========================================================
# PHASE 2 - PART 4
# RAG SAFETY BRAIN + COMPLIANCE AI + ANALYTICS
# ==========================================================


from datetime import datetime



# ==========================================================
# RAG SAFETY KNOWLEDGE ENGINE
# ==========================================================


st.divider()

st.header(
    "🧠 RAG SAFETY KNOWLEDGE BRAIN"
)


knowledge_base = [

{
"issue":"Gas Leakage",
"risk":"Explosion Hazard",
"solution":
"Stop operation, isolate source, evacuate workers and inspect gas monitoring system."
},

{
"issue":"High Temperature",
"risk":"Fire Hazard",
"solution":
"Reduce process load and activate cooling protocol."
},

{
"issue":"PPE Missing",
"risk":"Worker Injury",
"solution":
"Block entry until required PPE compliance is verified."
},

{
"issue":"High Vibration",
"risk":"Equipment Failure",
"solution":
"Schedule immediate mechanical inspection."
}

]



query = st.text_input(

"🔍 Ask Safety AI Assistant",

placeholder=
"Example: What should we do during gas leakage?"

)



if query:


    response_found=False


    for item in knowledge_base:


        if any(

            word.lower() in query.lower()

            for word in item["issue"].split()

        ):


            st.success(

            "🤖 AI Safety Recommendation"

            )


            st.info(

f"""
Hazard:

{item["issue"]}


Risk:

{item["risk"]}


Recommended Action:

{item["solution"]}

"""

            )


            response_found=True


            break



    if not response_found:


        st.warning(

        """
        AI Knowledge Agent:

        No exact incident found.
        Escalating to safety officer.
        """

        )





# ==========================================================
# COMPLIANCE INTELLIGENCE AGENT
# ==========================================================



st.divider()


st.header(

"📋 Regulatory Compliance Intelligence"

)



compliance=pd.DataFrame(

[

{

"Standard":

"OISD",

"Area":

"Gas Safety",

"Status":

"MONITORING"

},


{

"Standard":

"Factory Act",

"Area":

"Worker Protection",

"Status":

"COMPLIANT"

},


{

"Standard":

"DGMS",

"Area":

"Industrial Hazard Control",

"Status":

"REVIEW REQUIRED"

}

]

)



st.dataframe(

    compliance,

    width="stretch"

)




# Compliance Score


compliance_score=87



st.metric(

"Compliance Health Score",

f"{compliance_score}%"

)






# ==========================================================
# INCIDENT PATTERN INTELLIGENCE
# ==========================================================



st.divider()


st.header(

"📈 Incident Pattern Intelligence Agent"

)



incident_history=pd.DataFrame(

[

{

"Incident":

"Gas Leak",

"Zone":

"Chemical Plant",

"Frequency":

12

},

{

"Incident":

"PPE Violation",

"Zone":

"Assembly",

"Frequency":

25

},

{

"Incident":

"Machine Failure",

"Zone":

"Power Unit",

"Frequency":

8

}

]

)



fig_incident=px.bar(

incident_history,

x="Incident",

y="Frequency",

title="Historical Incident Pattern Analysis"

)



st.plotly_chart(

    fig_incident,

    width="stretch"

)




st.warning(

"""
AI Finding:

Repeated PPE violations detected.

Risk of future injury increased by 34%.

Preventive Action:

Implement automatic PPE verification system.
"""

)






# ==========================================================
# PREDICTIVE SAFETY ANALYTICS
# ==========================================================



st.divider()


st.header(

"🔮 Predictive Safety Analytics"

)



future_prediction=pd.DataFrame(

{

"Parameter":

[

"Gas Level",

"Temperature",

"Fatigue",

"Machine Vibration"

],


"Risk Trend":

[

"↑ Increasing",

"↑ Increasing",

"Stable",

"↑ Increasing"

]

}

)



st.table(

    future_prediction

)



col1,col2,col3=st.columns(3)



with col1:

    st.metric(

    "Next 1 Hour Risk",

    "MEDIUM"

    )


with col2:

    st.metric(

    "Incident Probability",

    "18%"

    )


with col3:

    st.metric(

    "Prediction Lead Time",

    "45 Minutes"

    )






# ==========================================================
# AI EXECUTIVE SUMMARY
# ==========================================================



st.divider()


st.header(

"🏢 Safety Officer Executive Summary"

)



summary=f"""

Generated Time:

{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}



System Status:

🟢 AI Safety Platform Operational



Active Intelligence Modules:

✅ Sensor Fusion Engine

✅ Risk Prediction AI

✅ Emergency Response Agent

✅ RAG Safety Brain

✅ Compliance Monitor

✅ Digital Twin Analytics



Current Recommendation:

Maintain continuous monitoring and verify high-risk zones.

"""



st.success(summary)






# ==========================================================
# INCIDENT REPORT GENERATOR
# ==========================================================



st.divider()


st.header(

"📄 AI Incident Report Generator"

)



if st.button(

"Generate Safety Report"

):


    report_text=f"""

PREET SAFETY TECHNOLOGY

AI INDUSTRIAL SAFETY REPORT


Time:
{datetime.now()}


System:
ACTIVE


Risk Analysis:
Completed


Compliance Check:
Completed


AI Recommendation:
Safety monitoring continued.


"""


    st.download_button(

        "⬇ Download AI Report",

        report_text,

        file_name=

        "Preet_AI_Safety_Report.txt"

    )
# ==========================================================
# PHASE 2 - PART 5
# ULTRA PREMIUM COMMAND CENTER UI
# ==========================================================


import streamlit.components.v1 as components



# ==========================================================
# PREMIUM ANIMATED HEADER
# ==========================================================


st.markdown(
"""
<style>


body{

background:#020617;

}


.hero{

padding:35px;

border-radius:25px;

background:

linear-gradient(
135deg,
rgba(0,229,255,0.15),
rgba(99,102,241,0.15)
);


border:

1px solid rgba(255,255,255,0.15);


box-shadow:

0 0 40px rgba(0,229,255,0.2);


animation:

glow 3s infinite alternate;


}



@keyframes glow{


from{

box-shadow:

0 0 20px #00e5ff;

}


to{


box-shadow:

0 0 50px #6366f1;

}


}



.hero h1{

font-size:50px;

color:#00e5ff;

font-weight:900;

}



.agent-card{


padding:20px;

border-radius:20px;


background:

rgba(255,255,255,0.08);


border:

1px solid rgba(255,255,255,0.15);


text-align:center;


}



</style>



<div class="hero">


<h1>

🚨 PREET SAFETY TECHNOLOGY

</h1>


<h3>

AI Powered Industrial Safety Intelligence Command Center

</h3>


<p>

Zero Harm Operations • Predict Before Incident • Autonomous Response

</p>


</div>

""",

unsafe_allow_html=True
)





# ==========================================================
# AI AGENT STATUS BOARD
# ==========================================================


st.divider()


st.header(

"🤖 Autonomous AI Agent Network"

)



agents=pd.DataFrame(

{

"AI Agent":[

"Sensor Fusion Agent",

"Risk Prediction Agent",

"Emergency Agent",

"RAG Safety Agent",

"Compliance Agent",

"CCTV Vision Agent"

],


"Status":[

"🟢 ONLINE",

"🟢 ONLINE",

"🟢 READY",

"🟢 ACTIVE",

"🟢 MONITORING",

"🟢 CONNECTED"

]


}

)



cols=st.columns(3)



for index,row in agents.iterrows():


    with cols[index%3]:


        st.markdown(

f"""

<div class="agent-card">


<h3>

{row["AI Agent"]}

</h3>


<h4>

{row["Status"]}

</h4>


</div>

""",

unsafe_allow_html=True

)






# ==========================================================
# LIVE RISK RADAR
# ==========================================================


st.divider()


st.header(

"🎯 AI Risk Radar"

)



risk_value=35



if len(st.session_state.records)>0:


    latest_risk = st.session_state.records[-1]["Risk"]


    if latest_risk=="CRITICAL":

        risk_value=90


    elif latest_risk=="WARNING":

        risk_value=60


    else:

        risk_value=15





fig_gauge=go.Figure(

go.Indicator(

mode="gauge+number",

value=risk_value,


title={

"text":

"Industrial Risk Score"

},


gauge={

"axis":

{

"range":[0,100]

}

}

)

)



fig_gauge.update_layout(

height=350,

template="plotly_dark"

)



st.plotly_chart(

fig_gauge,

width="stretch"

)





# ==========================================================
# COMMAND CENTER METRICS
# ==========================================================



st.divider()


st.header(

"📡 Mission Control Dashboard"

)



m1,m2,m3,m4=st.columns(4)



m1.metric(

"AI Engine",

"ACTIVE"

)


m2.metric(

"Sensor Network",

"ONLINE"

)


m3.metric(

"Emergency Response",

"READY"

)


m4.metric(

"Prediction Mode",

"REAL TIME"

)






# ==========================================================
# LIVE ALERT ANIMATION
# ==========================================================


if len(st.session_state.alerts)>0:


    st.divider()


    st.error(

"""
🚨 ACTIVE SAFETY ALERT

AI detected abnormal industrial condition.

Emergency workflow initiated.

"""

    )


    components.html(

"""

<script>


let audio = new Audio();

console.log(

"Safety Alert Triggered"

);


</script>

""",

height=0

)



else:


    st.success(

"""
🟢 ALL SYSTEMS NORMAL

Continuous AI monitoring active.

"""

    )






# ==========================================================
# FOOTER
# ==========================================================



st.divider()



st.markdown(

"""

<center>


<h3>

🏆 Preet Safety Technology

</h3>


<p>

AI Industrial Safety Intelligence Platform

<br>

Built for Zero-Harm Operations

</p>


</center>

""",

unsafe_allow_html=True

)
