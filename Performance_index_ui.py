import streamlit as st
import joblib

model = joblib.load("MLR.joblib")

st.title("Predicting Performance Index of Students")
st.markdown("Hello Students Enter the following Details!")

st.subheader("Hour Studied")
hour_studied = st.number_input("Enter the hours you studied",min_value= 0.0, max_value= 24.0, step= 1.0)

st.subheader("Previous Scores")
previous_score = st.number_input("Enter your previous score",min_value= 0.0,step= 1.0)

st.subheader("Extracurricular Activities")
extracurricular_activities = st.selectbox("Participates in extracurricular activities?",["Yes", "No"])

st.subheader("Sleep Hours")
sleep_hours = st.number_input("Enter the number of hour  slept",min_value=0.0, max_value= 24.0, step= 1.0)

st.subheader("Sample Question Papers Practiced")
sample_question_paper_solved = st.number_input("Number of question paper solved", min_value=0, step= 1)

# converting categorical inputs into numeric values
extracurricular_activities = (1 if extracurricular_activities == "Yes" else 0)

st.subheader("Prediction")
if st.button("Predict"):
    try:
        prediction = st.write(model.predict
                           ([[hour_studied,
                              previous_score,
                              extracurricular_activities,
                              sleep_hours,
                              sample_question_paper_solved]]))
        st.success("Prediction Successful")
    except Exception as e:
        st.error(f"Prediction Failed!: {e}")
