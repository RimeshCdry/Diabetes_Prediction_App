import numpy as np
import pandas as pd
import joblib
import streamlit as st

# Load the trained model and scaler
model = joblib.load("Diabetes_Prediction_model.pkl")
scaler = joblib.load("scaler.pkl")  # Load the pre-trained scaler

# Set the page configuration
st.set_page_config(page_title="Diabetes Prediction App 🏥", page_icon="🏥")

# Streamlit App Title
st.title("Diabetes Prediction App 🏥")
st.write("A simple machine learning-based app to predict diabetes risk."
         " Enter the details below and click 'Predict'.")

# Sidebar for user input
st.header("Enter Patient Details")

# Get user input
pregnancies = st.number_input("Pregnancies", 0, 17, 3)
glucose = st.number_input("Glucose Level", 0, 199, 117)
blood_pressure = st.number_input("Blood Pressure (mmHg)", 0, 122, 72)
skin_thickness = st.number_input("Skin Thickness (mm)", 0, 99, 23)
insulin = st.number_input("Insulin Level (µU/mL)", 0, 846, 30)
bmi = st.number_input("Body Mass Index (BMI)", 0.0, 67.1, 32.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.078, 2.42, 0.3725)
age = st.number_input("Age (years)", 21, 150, 29)

feature_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                 "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

# Convert user input to a DataFrame
user_input_df = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                               insulin, bmi, dpf, age]], columns=feature_names)

# Standardize the input using the same scaler
user_input_scaled = scaler.transform(user_input_df)

# Make prediction
if st.button("Predict"):
    try:
        prediction = model.predict(user_input_scaled)

        st.subheader("Prediction Result")
        if prediction[0] == 1:
            st.error("⚠️ You might have diabetes.")
            
            # Suggestions for patients with diabetes
            st.write("### Suggested Actions:")
            st.markdown(
                """
                - 🥗 Maintain a healthy diet with low sugar and carbs.
                - 🏃 Exercise regularly (walking, yoga, or light workouts).
                - 🩸 Monitor blood sugar levels frequently.
                - 🏥 Consult a healthcare professional for further evaluation.
                """
            )
        else:
            st.success("✅ You might not have diabetes.")
            st.write("Keep maintaining a healthy lifestyle! 💪")

    except Exception as e:
        st.error("An error occurred during prediction. Please check the input values.")

# Footer
st.markdown("---")

# Contact Information
st.markdown("### 📬 Connect with Me")
st.markdown(
    """
    - 🛠️ [GitHub](https://github.com/RimeshCdry/)  
    - ✉️ Email: rimeshcdry45@gmail.com  
    """
)
st.caption("⚠️ *This app provides a preliminary risk assessment and should not be used as a substitute for professional medical advice.*")
