# ==========================================================
# PREET SAFETY TECHNOLOGY
# ENTERPRISE PREMIUM UI THEME
# ==========================================================


import streamlit as st



def load_theme():

    st.markdown(
    """

<style>


.main {

background:#020617;

}


.stApp{

background:

linear-gradient(

135deg,

#020617,

#0f172a

);

color:white;

}



.hero-card{


padding:35px;

border-radius:25px;


background:

rgba(255,255,255,0.08);


border:

1px solid rgba(255,255,255,0.15);


box-shadow:

0 0 40px rgba(0,229,255,0.25);


}



.hero-title{


font-size:48px;

font-weight:900;

color:#00e5ff;


}



.card{


padding:22px;

border-radius:20px;


background:

rgba(255,255,255,0.08);


border:

1px solid rgba(255,255,255,0.15);


backdrop-filter:blur(10px);


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