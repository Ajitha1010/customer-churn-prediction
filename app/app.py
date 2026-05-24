import joblib
import pandas as pd
import streamlit as st

model = joblib.load("models/churn_model.pkl")
feature_columns = joblib.load("models/columns.pkl")
st.title("Customer Churn Predictor")
st.header("Customer Input")
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)
tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=100,
    value=12
)
monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)
total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)
contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'gender_Male': [1 if gender == "Male" else 0],
        'Contract_One year': [1 if contract == "One year" else 0],
        'Contract_Two year': [1 if contract == "Two year" else 0]
    })

    for col in feature_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[feature_columns]
    # Prediction
    prediction = model.predict(input_data)

    # Probability
    proba = model.predict_proba(input_data)

    churn_probability = proba[0][1] * 100  # probability of class 1

    st.header("Prediction Result")
    if prediction[0] == 1:
        st.error(f"Customer likely to churn ({churn_probability:.2f}% probability)")
    else:
        st.success(f"Customer likely to stay ({100 - churn_probability:.2f}% probability)")
    st.progress(int(churn_probability))
    st.write(f"Churn Probability: {churn_probability:.2f}%")
    if churn_probability < 30:
        risk = "Low Risk"
    elif churn_probability < 70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"
    st.info(f"Risk Level: {risk}")
    if prediction[0] == 1:
        st.write("⚠️ High churn risk due to factors like contract type and monthly charges.")
    else:
        st.write("✅ Customer is stable with low churn risk.")
        