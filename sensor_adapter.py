# ==========================================================
# PREET SAFETY TECHNOLOGY
# SENSOR DATA ADAPTER ENGINE
# Enterprise Data Normalization Layer v1.0
# ==========================================================


from datetime import datetime



def normalize_sensor(raw_sensor):

    """
    Converts all sensor formats into
    one standard industrial format
    """

    sensor = {

        # Worker Information

        "Worker":

        raw_sensor.get(
            "Worker",
            "Unknown"
        ),


        "Zone":

        raw_sensor.get(
            "Zone",
            "Unknown"
        ),



        # Industrial Sensors

        "Temperature":

        float(
            raw_sensor.get(
                "Temperature",
                0
            )
        ),



        "Gas_Level":

        float(
            raw_sensor.get(
                "Gas_Level",
                0
            )
        ),



        "Humidity":

        float(
            raw_sensor.get(
                "Humidity",
                0
            )
        ),



        "Machine_Vibration":

        float(
            raw_sensor.get(
                "Machine_Vibration",
                raw_sensor.get(
                    "Vibration",
                    0
                )
            )
        ),



        "Noise_Level":

        float(
            raw_sensor.get(
                "Noise_Level",
                raw_sensor.get(
                    "Noise",
                    0
                )
            )
        ),



        "Worker_Fatigue":

        float(
            raw_sensor.get(
                "Worker_Fatigue",
                raw_sensor.get(
                    "Fatigue",
                    0
                )
            )
        ),



        "PPE_Status":

        raw_sensor.get(

            "PPE_Status",

            raw_sensor.get(

                "PPE",

                "Available"

            )

        ),



        "Timestamp":

        datetime.now().strftime(
            "%H:%M:%S"
        )

    }


    return sensor