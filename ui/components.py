# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE PREMIUM UI ENGINE
# ==========================================================

import streamlit as st


def load_premium_theme():


    st.markdown(
    """

<style>


.stApp{

background:

linear-gradient(
135deg,
#020617,
#111827
);

color:white;

}



.hero-card{


padding:40px;

border-radius:30px;


background:

rgba(255,255,255,0.08);


border:

1px solid rgba(255,255,255,0.2);


box-shadow:

0 0 50px rgba(0,229,255,0.25);


}



.hero-title{


font-size:52px;

font-weight:900;

color:#00e5ff;


}



.metric-card{


padding:20px;

border-radius:20px;


background:

rgba(255,255,255,0.08);


border:

1px solid rgba(255,255,255,0.15);


text-align:center;


}


.safe{

color:#22c55e;

}


.warning{

color:#f59e0b;

}


.danger{

color:#ef4444;

}



</style>


""",

unsafe_allow_html=True

)