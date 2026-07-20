import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Preet Safety Technology",
    page_icon="🏭",
    layout="wide"
)

# Premium CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #0b1220;
    }
    h1 {
        color: #00e5ff;
        font-size: 42px;
    }
    h2, h3 {
        color: white;
    }
    .metric-card {
        background: rgba(255,255,255,0.08);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.15);
    }
    .stButton>button {
        background: #00e5ff;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load AI Model
model = joblib.load("model/risk_model.pkl")
scaler = joblib.load("model/scaler.pkl")
ppe_encoder = joblib.load("model/ppe_encoder.pkl")
risk_encoder = joblib.load("model/risk_encoder.pkl")

# Header
st.title("🏭 Preet Safety Technology")
st.subheader("AI Based Industrial Worker Safety Monitoring System")
st.divider()

# Sidebar
st.sidebar.header("⚙️ Sensor Control Panel")

temperature = st.sidebar.slider("🌡 Temperature (°C)", 20, 100, 45)
gas = st.sidebar.slider("☣ Gas Level (ppm)", 0, 150, 40)
humidity = st.sidebar.slider("💧 Humidity (%)", 10, 100, 60)
vibration = st.sidebar.slider("⚙ Machine Vibration", 0.0, 10.0, 3.0)
noise = st.sidebar.slider("🔊 Noise Level (dB)", 40, 120, 75)
fatigue = st.sidebar.slider("😴 Worker Fatigue (%)", 0, 100, 40)
ppe = st.sidebar.selectbox("🦺 PPE Status", ["Available", "Missing"])

# Prediction
if st.button("🚀 RUN AI SAFETY ANALYSIS"):

    ppe_value = ppe_encoder.transform([ppe])[0]

    input_data = np.array([[
        temperature, gas, humidity, vibration, noise, fatigue, ppe_value
    ]])

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    probability = model.predict_proba(scaled_data)[0]
    risk = risk_encoder.inverse_transform(prediction)[0]
    confidence = max(probability) * 100

    # Safety Score
    safety_score = 100 - confidence

    # Result Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Risk Status", risk)
    with col2:
        st.metric("AI Confidence", f"{confidence:.2f}%")
    with col3:
        st.metric("Safety Score", f"{safety_score:.1f}%")

    st.divider()

    # Alert System
    if risk == "CRITICAL":
        st.error(
            """
            🚨 CRITICAL SAFETY ALERT
            Immediate evacuation required.
            AI detected dangerous industrial conditions.
            """
        )
        action = """
        - Stop machine operation
        - Evacuate worker
        - Check gas leakage
        - Contact safety officer
        """

    elif risk == "WARNING":
        st.warning(
            """
            ⚠ WARNING CONDITION
            Monitor worker continuously.
            """
        )
        action = """
        - Reduce exposure time
        - Check equipment
        - Improve ventilation
        """

    else:
        st.success(
            """
            🟢 WORKPLACE SAFE
            Environment conditions normal.
            """
        )
        action = """
        - Continue monitoring
        - Maintain PPE compliance
        """

    st.subheader("Recommended Safety Action")
    st.info(action)

    # Sensor Chart
    sensor_df = pd.DataFrame({
        "Sensor": ["Temperature", "Gas", "Humidity", "Vibration", "Noise", "Fatigue"],
        "Value": [temperature, gas, humidity, vibration, noise, fatigue]
    })

    fig = px.bar(sensor_df, x="Sensor", y="Value", title="Live Sensor Intelligence")
    st.plotly_chart(fig, width="stretch")

# Industrial Overview
st.divider()
st.subheader("🏭 Industrial Zone Overview")

zones = pd.DataFrame({
    "Zone": ["Chemical Plant", "Steel Furnace", "Mining Area", "Assembly Line", "Power Station"],
    "Risk": ["HIGH", "MEDIUM", "LOW", "HIGH", "LOW"]
})

fig2 = px.pie(zones, names="Risk", title="Factory Risk Distribution")
st.plotly_chart(fig2, width="stretch")

# Footer
st.divider()
st.caption(
    f"Preet Safety Technology | AI Industrial Safety Platform | Last Update: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)