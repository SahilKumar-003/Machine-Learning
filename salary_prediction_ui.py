import joblib
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💼",
    layout="centered"
)

# Load Model
MODEL_PATH = "SLR.joblib"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("Unable to load the salary prediction model.")
    st.stop()

# Header
st.title("💼 Salary Prediction System")
st.markdown(
    """
    Welcome! 👋  
    Enter your **years of professional experience** below to estimate your expected salary.
    """
)

st.divider()

# User Input
experience = st.number_input(
    "📊 Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1,
    help="Enter your total professional experience in years."
)

# Prediction
if st.button("🔮 Predict Salary", use_container_width=True):

    prediction = model.predict([[experience]])[0]

    st.success("Prediction generated successfully!")

    st.metric(
        label="💰 Predicted Salary",
        value=f"₹{prediction:,.2f}"
    )

    st.info(
        f"Based on **{experience:.1f} years** of experience, "
        f"the estimated salary is **₹{prediction:,.2f}**."
    )