import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler

#loading our trained ANN model,OHE,LabelEncoder,pickle files
model = load_model('model.h5')

#load the encoder
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)
    
#load the OHE
with open('one_hot_encoder_geo.pkl','rb') as file:
    one_hot_encoder_geo = pickle.load(file)
    
#load the scaler
with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)
    
#Streamlit.app

st.title('CUSTOMER CHURN PREDICTION')

#user input

geography = st.selectbox('Geography',one_hot_encoder_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st. number_input( 'Estimated Salary')
tenure = st. slider ('Tenure', 0, 10)
num_of_products = st.slider ('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])

# Prepare the input data
input_data = pd.DataFrame({
'CreditScore': [credit_score],
'Gender': [label_encoder_gender.transform([gender])[0]],
'Age' : [age],
'Tenure': [tenure],
'Balance': [balance],
'NumOfProducts' : [num_of_products],
'HasCrCard': [has_cr_card],
'IsActiveMember': [is_active_member],
'EstimatedSalary': [estimated_salary]
})

geo_encoded =  one_hot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=one_hot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

#scaling it

input_data_scaled = scaler.transform(input_data)

#prediction
prediction = model.predict(input_data_scaled)
pred_prob = prediction[0][0]

if pred_prob > 0.5:
    st.write('The customer is likely to churn')
else:
    st.write('The customer is not likely to churn')