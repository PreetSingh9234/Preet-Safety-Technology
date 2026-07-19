import streamlit as st

from ui.premium_theme import load_premium_theme
from ui.components import hero_header,metric_card,alert_box


st.set_page_config(
layout="wide"
)


load_premium_theme()


hero_header()


c1,c2,c3=st.columns(3)


with c1:
    metric_card(
        "Workers",
        "250",
        "👷"
    )


with c2:
    metric_card(
        "AI Score",
        "98%",
        "🧠"
    )


with c3:
    metric_card(
        "Alerts",
        "03",
        "🚨"
    )


alert_box(
"Industrial Gas Risk Detected"
)