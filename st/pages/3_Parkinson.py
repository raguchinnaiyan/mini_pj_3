import streamlit as st
import pandas as pd
import joblib

model = joblib.load("st/models/best_random_forest.pkl")  

st.title("🧠 Parkinson's Disease Prediction")
st.write("Enter the patient's voice measurements to check for Parkinson’s Disease.")

# Input fields for top 8 features
ppq = st.number_input("MDVP:PPQ", min_value=0.0, max_value=0.2, step=0.001, format="%.3f")
rpde = st.number_input("RPDE", min_value=0.0, max_value=1.0, step=0.01)
jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, max_value=1.0, step=0.001, format="%.3f")
ppe = st.number_input("PPE", min_value=0.0, max_value=1.0, step=0.01)
rap = st.number_input("MDVP:RAP", min_value=0.0, max_value=0.2, step=0.001, format="%.3f")
ddp = st.number_input("Jitter:DDP", min_value=0.0, max_value=0.2, step=0.001, format="%.3f")
spread1 = st.number_input("spread1", min_value=-10.0, max_value=0.0, step=0.1)
apq = st.number_input("MDVP:APQ", min_value=0.0, max_value=0.2, step=0.001, format="%.3f")

# Input DataFrame for prediction
input_data = pd.DataFrame([{
    "MDVP:PPQ": ppq,
    "RPDE": rpde,
    "MDVP:Jitter(%)": jitter_percent,
    "PPE": ppe,
    "MDVP:RAP": rap,
    "Jitter:DDP": ddp,
    "spread1": spread1,
    "MDVP:APQ": apq
}])

# Prediction
if st.button("Predict Parkinson's Disease"):
    prediction = model.predict(input_data)
    result = "⚠️ Parkinson's Disease Detected" if prediction[0] == 1 else "✅ No Parkinson's Disease"
    st.success(f"Prediction Result: {result}")
