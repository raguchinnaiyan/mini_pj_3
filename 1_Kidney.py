import streamlit as st

st.title("🩺 Kidney Disease Prediction")

st.write("Fill the patient details below to predict Chronic Kidney Disease (CKD).")



import pandas as pd
import joblib  

# Load your trained model (make sure you save it as .pkl or .joblib before using here)
model = joblib.load("C:/Users/ragu/Min_pj_3/Stremlet_UI/pages/logistic_regression_model.pkl")  # Replace with your model filename


# Input fields for all selected features
hemo = st.number_input("Hemoglobin (g/dL)", min_value=3.0, max_value=18.0, step=0.1)
sg = st.number_input("Specific Gravity", min_value=1.000, max_value=1.030, step=0.001)
pcv = st.number_input("Packed Cell Volume", min_value=15, max_value=55, step=1)
rc = st.number_input("Red Blood Cell Count", min_value=2.0, max_value=8.0, step=0.1)
pc = st.selectbox("Pus Cell", ["Normal", "Abnormal"])
htn = st.selectbox("Hypertension", ["No", "Yes"])
dm = st.selectbox("Diabetes Mellitus", ["No", "Yes"])
al = st.slider("Albumin Level", min_value=0, max_value=5, step=1)
appet = st.selectbox("Appetite", ["Good", "Poor"])
bgr = st.number_input("Blood Glucose Random", min_value=50, max_value=500, step=1)

# Map categorical inputs to numeric
pc_map = {"Normal": 0, "Abnormal": 1}
yn_map = {"No": 0, "Yes": 1}
appet_map = {"Good": 0, "Poor": 1}

# Create input DataFrame
input_data = pd.DataFrame([{
    "hemo": hemo,
    "sg": sg,
    "pcv": pcv,
    "rc": rc,
    "pc": pc_map[pc],
    "htn": yn_map[htn],
    "dm": yn_map[dm],
    "al": al,
    "appet": appet_map[appet],
    "bgr": bgr
}])

# Predict button
if st.button("Predict CKD"):
    prediction = model.predict(input_data)
    result = "✅ CKD Present" if prediction[0] == 1 else "❌ CKD Not Present"
    st.success(f"Prediction Result: {result}")