# ==========================================================
# PREET SAFETY TECHNOLOGY
# AUTONOMOUS EMERGENCY COMMAND CENTER UI
# ==========================================================


import streamlit as st



def emergency_header():

    st.markdown(
    """

<div class="danger-alert">

<h1>
🚨 AUTONOMOUS EMERGENCY RESPONSE CENTER
</h1>


<p>
AI Incident Detection • Response Coordination • Zero Harm Protocol
</p>


</div>

""",

unsafe_allow_html=True

)




def show_emergency_level(level):


    if "LEVEL 3" in level:


        st.error(

        f"""

        🚨 CRITICAL EMERGENCY

        ## {level}


        Autonomous Response Activated

        """

        )


    elif "LEVEL 2" in level:


        st.warning(

        f"""

        ⚠ WARNING CONDITION

        ## {level}

        Increased Monitoring Required

        """

        )


    else:


        st.success(

        f"""

        ✅ NORMAL OPERATIONS

        ## {level}

        """

        )





def show_actions(actions):


    st.subheader(
        "🛡 AI Recommended Actions"
    )


    for action in actions:


        st.info(action)





def show_timeline(timeline):


    st.subheader(
        "⏱ Emergency Response Timeline"
    )


    for time,event in timeline.items():


        st.markdown(

        f"""

        **{time}**

        ➜ {event}

        """

        )





def emergency_button():


    if st.button(
        "🚨 ACTIVATE EMERGENCY SIMULATION"
    ):


        st.error(

        """

        EMERGENCY PROTOCOL STARTED


        ✔ Alarm Activated

        ✔ Safety Team Notified

        ✔ Evacuation Started

        ✔ Incident Log Created


        """

        )
