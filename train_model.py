import pandas as pd
import numpy as np
import os
import joblib


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report



# ==================================
# PREET SAFETY TECHNOLOGY
# AI Risk Prediction Model Training
# ==================================



print("\nLoading Safety Dataset...")


# Load dataset

df = pd.read_csv(
    "data/safety_data.csv"
)



print("Dataset Loaded")
print("Total Records:", len(df))



# ==================================
# Data Preparation
# ==================================


# Convert PPE text into numbers

ppe_encoder = LabelEncoder()


df["PPE_Status"] = ppe_encoder.fit_transform(
    df["PPE_Status"]
)



# Convert Risk labels

risk_encoder = LabelEncoder()


df["Risk_Level"] = risk_encoder.fit_transform(
    df["Risk_Level"]
)



# Features

X = df[

[
"Temperature",
"Gas_Level",
"Humidity",
"Machine_Vibration",
"Noise_Level",
"Worker_Fatigue",
"PPE_Status"
]

]



# Target

y = df["Risk_Level"]




# ==================================
# Train Test Split
# ==================================


X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)



# ==================================
# Scaling
# ==================================


scaler = StandardScaler()


X_train = scaler.fit_transform(
    X_train
)


X_test = scaler.transform(
    X_test
)




# ==================================
# AI Model
# ==================================


print("\nTraining AI Safety Model...")


model = RandomForestClassifier(

    n_estimators=200,
    max_depth=12,
    random_state=42

)



model.fit(

    X_train,
    y_train

)



# ==================================
# Accuracy
# ==================================


prediction = model.predict(
    X_test
)



accuracy = accuracy_score(

    y_test,
    prediction

)



print("\n==============================")
print("AI MODEL PERFORMANCE")
print("==============================")

print(
    "Accuracy:",
    round(accuracy*100,2),
    "%"
)



print(
    classification_report(
        y_test,
        prediction
    )
)



# ==================================
# Save Model
# ==================================


os.makedirs(
    "model",
    exist_ok=True
)



joblib.dump(

    model,
    "model/risk_model.pkl"

)



joblib.dump(

    scaler,
    "model/scaler.pkl"

)



joblib.dump(

    ppe_encoder,
    "model/ppe_encoder.pkl"

)



joblib.dump(

    risk_encoder,
    "model/risk_encoder.pkl"

)



print("==============================")
print("MODEL SAVED SUCCESSFULLY")
print("==============================")

print(
"""
model/
 |
 ├── risk_model.pkl
 ├── scaler.pkl
 ├── ppe_encoder.pkl
 └── risk_encoder.pkl
"""
)