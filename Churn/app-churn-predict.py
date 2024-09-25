import streamlit as st
import requests
import json
import os
st.title("Customer Churn Prediction")

# Input fields for the user
age = st.number_input("Age", min_value=18, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges")
contract_type = st.selectbox("Contract Type", ["Month-to-Month", "One-Year", "Two-Year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber Optic", "None"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])
total_charges = monthly_charges * tenure

# Prepare the input data for the API
input_data = {
    "input_data": {
        "columns": [
            "Age",
            "Gender",
            "Tenure",
            "MonthlyCharges",
            "ContractType",
            "InternetService",
            "TotalCharges",
            "TechSupport"
        ],
        "index": [0],
        "data": [
            [
                age,
                gender,
                tenure,
                monthly_charges,
                contract_type,
                internet_service,
                total_charges,
                tech_support
            ]
        ]
    }
}

api_endpoint = api_endpoint = os.getenv("API_ENDPOINT")
api_key = os.getenv("API_KEY")


if st.button("Predict Churn"):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'  
    }
    
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(input_data))
    
  
   
    
    if response.status_code == 200:
        prediction = response.json()
       
        
       
        if isinstance(prediction, list) and len(prediction) > 0:
            churn_value = prediction[0]  
            st.write("Churn Prediction: ", "Yes" if churn_value else "No")
        else:
            st.error("Unexpected response format.")
    else:
        st.error("Error: " + response.text)
