## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor


st.title('Telco Customer churn Prediction')
gender = st.selectbox("gender", options=["Male", "Female"])
SeniorCitizen = st.selectbox("SeniorCitizen", options=["0", "1"])
Partner = st.selectbox('Partner', options=['Yes', 'No'])
Dependents = st.selectbox('Dependents', options=['Yes', 'No'])
tenure = st.number_input('tenure', 0,100)
PhoneService = st.selectbox('PhoneService', options=['Yes', 'No'])
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
MonthlyCharges = st.number_input('MonthlyCharges', 0, 1000)
TotalCharges = st.number_input('TotalCharges', 0, 2000)
Churn=st.form('Churn', clear_on_submit=False)

input_data_dict = {
'gender': gender,
 'SeniorCitizen': SeniorCitizen,
 'Partner': Partner,
 'Dependents': Dependents,
 'tenure': tenure,
 'PhoneService': PhoneService,
 'MultipleLines': MultipleLines,
 'InternetService': InternetService,
 'OnlineSecurity': OnlineSecurity,
 'OnlineBackup': OnlineBackup,
 'DeviceProtection': DeviceProtection,
 'TechSupport': TechSupport,
 'StreamingTV': StreamingTV,
 'StreamingMovies': StreamingMovies,
 'Contract': Contract,
 'PaperlessBilling': PaperlessBilling,
 'PaymentMethod': PaymentMethod,
 'MonthlyCharges': MonthlyCharges,
 'TotalCharges': TotalCharges
}

st.write(input_data_dict)

input_data=pd.DataFrame([input_data_dict])

st.write(input_data)

save_path  = "models"


save_model_predictor = TabularPredictor.load(save_path)
submit = st.button("CLICK TO PREDICT CUSTOMER CHURN")
if submit:
    customer_churn_prediction=save_model_predictor.predict(input_data)[0]
    st.write(f"The Telco customer churn is: {customer_churn_prediction}")
