import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model/kidney_risk_model.pkl")

# Streamlit app title
st.title("🌡️ Kidney Stress Risk Predictor")
st.subheader("For Heat-Exposed Individuals in the UAE")

# User input form
with st.form("input_form"):
    age = st.slider("Age", 20, 60, 35)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=24.0)
    hours_in_heat = st.slider("Hours Exposed to Heat (Daily)", 0, 12, 6)
    temp = st.slider("Ambient Temperature (°C)", 35, 55, 44)
    humidity = st.slider("Humidity (%)", 5, 90, 30)
    bp_sys = st.number_input("Systolic BP", 90, 180, 120)
    bp_dia = st.number_input("Diastolic BP", 50, 120, 80)
    heart_rate = st.slider("Heart Rate (bpm)", 50, 150, 90)
    urine_color = st.slider("Urine Color (1=Clear, 4=Dark)", 1, 4, 2)
    water_intake = st.number_input("Water Intake (liters)", 0.0, 5.0, 2.5)
    diabetes = st.selectbox("Diabetic?", ["No", "Yes"])
    prior_dehydration = st.selectbox("History of Dehydration?", ["No", "Yes"])

    submitted = st.form_submit_button("Predict Risk")

# When form is submitted
if submitted:
    input_data = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "hours_in_heat": hours_in_heat,
        "temp": temp,
        "humidity": humidity,
        "bp_sys": bp_sys,
        "bp_dia": bp_dia,
        "heart_rate": heart_rate,
        "urine_color": urine_color,
        "water_intake_liters": water_intake,
        "diabetes": 1 if diabetes == "Yes" else 0,
        "prior_dehydration": 1 if prior_dehydration == "Yes" else 0
    }])

    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.error("🚨 High Risk: Patient may be experiencing heat-induced kidney stress.")
    else:
        st.success("✅ Low Risk: Patient is not currently showing signs of heat-related kidney stress.")

