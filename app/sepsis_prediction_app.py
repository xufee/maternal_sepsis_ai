import streamlit as st
import pandas as pd
import numpy as np
import random

# Set the app title and layout
st.set_page_config(page_title="Maternal Sepsis Prediction", layout="wide")

# Add a title and description
st.title("Maternal Sepsis Prediction App")
st.markdown("Upload a CSV file or enter patient data to predict sepsis.")

# Function to predict sepsis
def predict_sepsis(row):
    if (row['Temperature_C'] > 38.5 and row['WBC_count_x10^9/L'] > 12 and row['CRP_mg/L'] > 50) or row['Organ_dysfunction'] == 'Yes':
        return 'Yes', random.randint(1, 48), random.choice(['Recovered', 'ICU', 'Mortality'])
    return 'No', None, 'Recovered'

# Sidebar to choose input method
st.sidebar.header("Choose Input Method")
input_method = st.sidebar.radio("Select:", ["Upload CSV", "Enter Manually"])

# Option 1: Upload CSV
if input_method == "Upload CSV":
    st.header("Upload Dataset")
    uploaded_file = st.file_uploader("Choose maternal_sepsis_dataset.csv", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        # Fix negative CRP values
        df['CRP_mg/L'] = df['CRP_mg/L'].clip(lower=0)
        
        # Apply sepsis prediction
        df[['Sepsis_detected', 'Time_to_diagnosis_hr', 'Outcome']] = df.apply(
            lambda row: pd.Series(predict_sepsis(row)), axis=1
        )
        
        # Show results in a table
        st.subheader("Prediction Results")
        st.dataframe(df[['Patient_ID', 'Temperature_C', 'WBC_count_x10^9/L', 
                         'CRP_mg/L', 'Organ_dysfunction', 'Sepsis_detected', 
                         'Time_to_diagnosis_hr', 'Outcome']])
        
        # Show a bar chart of sepsis counts
        st.subheader("Sepsis Distribution")
        sepsis_counts = df['Sepsis_detected'].value_counts()
        st.bar_chart(sepsis_counts)
        
        # Allow downloading predictions
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="maternal_sepsis_predictions.csv",
            mime="text/csv"
        )

# Option 2: Manual Input
else:
    st.header("Enter Patient Data")
    with st.form("patient_form"):
        temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0, step=0.1)
        wbc = st.number_input("WBC Count (x10^9/L)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
        crp = st.number_input("CRP (mg/L)", min_value=0.0, max_value=200.0, value=30.0, step=0.1)
        organ_dysfunction = st.selectbox("Organ Dysfunction", ["No", "Yes"])
        
        submit_button = st.form_submit_button("Predict Sepsis")
        
        if submit_button:
            # Create a DataFrame for the input
            input_data = pd.DataFrame({
                'Temperature_C': [temperature],
                'WBC_count_x10^9/L': [wbc],
                'CRP_mg/L': [crp],
                'Organ_dysfunction': [organ_dysfunction]
            })
            
            # Predict sepsis
            sepsis_result, time_to_diagnosis, outcome = predict_sepsis(input_data.iloc[0])
            
            # Show results
            st.subheader("Prediction Result")
            st.write(f"Sepsis Detected: {sepsis_result}")
            st.write(f"Time to Diagnosis (hr): {time_to_diagnosis if time_to_diagnosis else 'N/A'}")
            st.write(f"Outcome: {outcome}")
            
