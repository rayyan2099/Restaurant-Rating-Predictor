import streamlit as st
import numpy as np
import joblib

from sklearn.preprocessing import StandardScaler

# Page setup
st.set_page_config(layout='wide')
st.title('🍽️ Restaurant Rating Prediction App')
st.caption('This app helps you predict a restaurant review class.')
st.divider()

# Load trained artifacts
scaler = joblib.load('scaler.pkl')
model = joblib.load('mlmodel.pkl')

# User inputs
averagecost = st.number_input('Estimated average cost for two', min_value=0.0, step=10.0)
tablebooking = st.selectbox("Restaurant has Table Booking?", ['Yes', 'No'])
onlinedelivery = st.selectbox("Restaurant has Online Delivery?", ['Yes', 'No'])
pricerange = st.selectbox("What is the price range?", [1, 2, 3, 4])

predict = st.button("🔮 Predict Rating and Review")

st.divider()

# Convert categorical inputs to numeric
booking = 1 if tablebooking == 'Yes' else 0
online = 1 if onlinedelivery == 'Yes' else 0

# Create input array
values = np.array([[averagecost, booking, online, pricerange]])
X_scaled = scaler.transform(values)

# Prediction
if predict:
    prediction = model.predict(X_scaled)
    pred_value=prediction[0]
    st.success(f"Predicted Rating/Review Class: {prediction[0]}")
    if pred_value < 2.5:
        st.error("Poor 😞")
    elif pred_value < 3.5:
        st.warning("Average 😐")
    elif pred_value < 4.0:
        st.info("Good 🙂")
    elif pred_value < 4.5:
        st.success("Very Good 😃")
    else:
        st.balloons()
        st.success("Excellent 🌟")