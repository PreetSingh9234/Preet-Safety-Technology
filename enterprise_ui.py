import streamlit as st

def load_enterprise_ui():
    st.markdown(
        """
        <style>
        .stApp{
            background: linear-gradient(135deg, #020617, #111827);
            color:white;
        }
        .hero-card{
            padding:35px;
            border-radius:25px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            box-shadow: 0 0 40px rgba(0,229,255,0.25);
            animation: fade 1s ease-in-out;
        }
        .hero-title{
            font-size:48px;
            font-weight:900;
            color:#00e5ff;
        }
        @keyframes fade{
            0%{
                opacity:0;
                transform:translateY(-20px);
            }
            100%{
                opacity:1;
                transform:translateY(0);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-card">
        <div class="hero-title">🛡️ PREET SAFETY AI</div>
        <p>AI-Powered Industrial Safety Intelligence Platform</p>
        </div>
        """,
        unsafe_allow_html=True
    )

import streamlit as st

def metric_card(title, value):
    st.markdown(
        f"""
        <div style="padding:20px; border-radius:20px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); text-align:center; box-shadow:0 0 20px rgba(0,229,255,0.15);">
        <h1 style="color:#00e5ff; font-size:38px; margin:0;">{value}</h1>
        <p style="color:#cbd5e1; font-size:16px;">{title}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def risk_alert(level,message):
    if level=="CRITICAL":
        st.error(f"🚨 {message}")
    elif level=="WARNING":
        st.warning(f"⚠️ {message}")
    else:
        st.success(f"✅ {message}")