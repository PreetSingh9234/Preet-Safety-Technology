import streamlit as st
import time

# DIGITAL TWIN HEADER
def digital_twin_header():
    st.markdown(
        """
        <div class="ai-card">
            <h1>🏭 AI FACTORY DIGITAL TWIN</h1>
            <p>Real-Time Geospatial Safety Intelligence</p>
            <p>Worker Location • Hazard Zones • Risk Heatmap</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# FACTORY STATUS PANEL
def factory_status_panel():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏭 Active Zones", "06")
    with col2:
        st.metric("👷 Workers Tracked", "08")
    with col3:
        st.metric("⚠ High Risk Areas", "02")

# LIVE MAP DISPLAY
def show_factory_map(fig):
    st.subheader("🗺️ Live Factory Risk Map")
    st.plotly_chart(fig, width="stretch")

# WORKER TRACKING
def worker_tracking_table(data):
    st.subheader("👷 Worker Digital Twin Tracking")
    st.dataframe(data, width="stretch")

# SIMULATION MODE
def digital_twin_simulation():
    if st.button("🚨 RUN FACTORY INCIDENT SIMULATION"):
        progress = st.progress(0)
        
        for i in range(101):
            time.sleep(0.02)
            progress.progress(i)

        st.error(
            """
            🚨 INCIDENT SIMULATION COMPLETE

            Gas Leak Detected
            Zone: Chemical Processing Unit

            AI Action:
            Emergency Response Activated
            """
        )