import streamlit as st
import joblib 

new_model = joblib.load("PLR.joblib")
poly = joblib.load("poly.joblib")

st.title("Ice Cream Sales Unit Prediction")
st.subheader("Hello Welcome Sir/Mam")

temp = st.number_input("Enter Temperature (°C)")

if st.button("Predict"):
    prediction = new_model.predict(poly.fit_transform([[temp]]))
    st.success(prediction)