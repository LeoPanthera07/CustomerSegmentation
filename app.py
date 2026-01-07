### Imports
# import sklearn
import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('Kmeans.pkl', 'rb') as f: kmeans = pickle.load(f)
with open('Scaler.pkl', 'rb') as f: scaler = pickle.load(f)

st.title("Customer Segmentation App")
st.write("Enter Customer details to predict the customer".title())

age = st.number_input("Age", 18, value=35)
income = st.number_input("Income",100,value=50000)
totalSpending = st.number_input("Total spending (Sum of Pruchases)",0,max_value=5000,value=1000)
numWebPurchases = st.number_input("Number of Web Purchases",min_value=0, max_value=100,value=20)
numStorePurchases = st.number_input("Number of Store Purchases",min_value=0,max_value=100,value=10)
numWebVisits = st.number_input("Number of Webvisits",0,20,5,25)
Recency = st.number_input("Days Since Last Purchase",0,365,30)

input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "totalSpending": [totalSpending],
    "NumWebPurchases": [numWebPurchases],
    "NumStorePurchases": [numStorePurchases],
    "NumWebVisitsMonth": [numWebVisits],
    "Recency":[Recency]    
})

input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):
    
    cluster = kmeans.predict(input_scaled)[0]
    
    st.success(f"Predicted Segment: Clusters {cluster}")
    