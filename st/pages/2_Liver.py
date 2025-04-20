import streamlit as st
import pandas as pd
import joblib

model = joblib.load("st/models/random_forest_model.pkl")  

st.title("🧪 Liver Disease Prediction")
st.write("Enter the patient's basic liver panel values to predict liver disease status.")

# Input fields
total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", min_value=0.0, max_value=30.0, step=0.1)
direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", min_value=0.0, max_value=15.0, step=0.1)
alk_phos = st.number_input("Alkaline Phosphotase (U/L)", min_value=50, max_value=2000, step=1)
total_proteins = st.number_input("Total Proteins (g/dL)", min_value=2.0, max_value=10.0, step=0.1)

# Create DataFrame
input_data = pd.DataFrame([{
    "Total_Bilirubin": total_bilirubin,
    "Direct_Bilirubin": direct_bilirubin,
    "Alkaline_Phosphotase": alk_phos,
    "Total_Protiens": total_proteins
}])

# Predict button
if st.button("Predict Liver Disease"):
    prediction = model.predict(input_data)
    result = "⚠️ Liver Disease Detected" if prediction[0] == 1 else "✅ No Liver Disease"
    st.success(f"Prediction Result: {result}")

