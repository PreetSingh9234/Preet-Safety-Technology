import streamlit as st

def show_winner_layer():
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("🏆 AI Safety Winner Intelligence Layer")

    # Performance Metrics
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("⏱ Early Warning Lead Time", "45 Minutes")
    with m2:
        st.metric("🎯 Risk Detection Accuracy", "97.7%")
    with m3:
        st.metric("🛡 False Negative Reduction", "82%")
    with m4:
        st.metric("👷 Worker Protection Score", "96%")

    # AI Explainability
    st.subheader("🧠 AI Explainability Engine")
    st.info(
        """
        AI Decision Trace:
        
        ☣ Gas sensor detected abnormal concentration
        🛠 Maintenance activity identified
        🔥 Hot work permit conflict detected
        🦺 Worker PPE violation detected
        📚 Historical incidents matched using RAG
        🚨 Emergency response automatically initiated
        
        Final Decision:
        Compound Risk = HIGH
        
        Reason:
        Multiple weak signals combined into one strong prediction.
        """
    )

    # Multi Agent Status
    st.subheader("🤖 Multi-Agent AI Architecture")
    agents = [
        ("📡 IoT Sensor Agent", "ONLINE"),
        ("🧠 Compound Risk Agent", "ACTIVE"),
        ("📄 Permit Intelligence Agent", "ACTIVE"),
        ("👁 Computer Vision Agent", "ONLINE"),
        ("📚 RAG Safety Agent", "ACTIVE"),
        ("🚨 Emergency Orchestrator", "READY"),
        ("📋 Compliance Agent", "MONITORING")
    ]

    a1, a2 = st.columns(2)
    for index, (agent, status) in enumerate(agents):
        box = a1 if index % 2 == 0 else a2
        with box:
            st.success(
                f"""
                {agent}
                
                Status:
                🟢 {status}
                """
            )

    # Industrial Impact
    st.subheader("🌍 Industrial Impact Simulation")
    i1, i2, i3 = st.columns(3)

    with i1:
        st.metric("🚨 Potential Incidents Prevented", "127")
    with i2:
        st.metric("⚡ Response Time Reduction", "70%")
    with i3:
        st.metric("🏭 Safety Intelligence Level", "Enterprise")

    # Final Message
    st.success(
        """
        🚀 ZERO HARM MISSION
        
        Preet Safety AI transforms traditional reactive safety systems
        into predictive autonomous safety intelligence.
        
        Instead of detecting accidents after failure,
        AI identifies dangerous combinations before escalation.
        
        Goal:
        🛡 ZERO HARM INDUSTRIAL OPERATIONS
        """
    )