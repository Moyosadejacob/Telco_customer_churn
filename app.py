## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
import numpy as np

st.title('Telco Customer churn Prediction')
gender = st.selectbox("gender", options=["Male", "Female"])
SeniorCitizen = st.selectbox("SeniorCitizen", options=["0", "1"])
Partner = st.selectbox('Partner', options=['Yes', 'No'])
Dependents = st.selectbox('Dependents', options=['Yes', 'No'])
tenure = st.number_input('tenure')
DPhoneService = st.selectbox('PhoneService', options=['Yes', 'No'])
MultipleLines = st.selectbox('MultipleLines', options=['No phone service', 'No', 'Yes'])
InternetService = st.selectbox('InternetService', options=['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('OnlineSecurity', options=['Yes', 'No'])
OnlineBackup = st.selectbox('DeviceProtection', options=['Yes', 'No'])
DeviceProtection = st.selectbox('OnlineBackup', options=['Yes', 'No'])
TechSupport = st.selectbox('TechSupport', options=['Yes', 'No'])
StreamingTV = st.selectbox('StreamingTV', options=['Yes', 'No'])
StreamingMovies = st.selectbox('StreamingMovies', options=['Yes', 'No'])
Contract = st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('PaperlessBilling', options=['Yes', 'No'])
PaymentMethod = st.selectbox('PaymentMethod', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])
MonthlyCharges = st.number_input('MonthlyCharges')
TotalCharges = st.number_input('TotalCharges')
Churn=st.form('Churn', clear_on_submit=False)

## st.form_submit_button(label="Churn", help=None, on_click=None, args=None, kwargs=None,  type="secondary", disabled=False, use_container_width=False)