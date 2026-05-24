# 📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a telecom customer will churn or stay, along with churn probability and risk level. The project includes data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

---

## 🚀 Project Overview

Customer churn is a critical problem in the telecom industry. This project builds a predictive system to identify customers who are likely to leave, helping businesses take proactive retention actions.

---

## 📁 Dataset

- Source: Kaggle Telco Customer Churn Dataset
- Records: ~7,000 customers
- Features: Customer demographics, account information, services used

---

## 🧠 Workflow

1. Data Cleaning
   - Handled missing values
   - Converted TotalCharges to numeric

2. Feature Engineering
   - Label encoding for target (Churn)
   - One-hot encoding for categorical variables

3. Model Building
   - Logistic Regression (primary model)
   - Decision Tree
   - Random Forest

4. Model Evaluation
   - Accuracy
   - F1 Score
   - Cross-validation

5. Model Persistence
   - Saved model using `joblib`
   - Saved feature columns for consistency

6. Deployment
   - Built interactive web app using Streamlit

---

## 🏆 Best Model

- Logistic Regression performed best based on F1 Score
- Balanced performance for imbalanced dataset

---

## 📊 Key Features Used

- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method
- Gender

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 🌐 Streamlit App Features

- Real-time customer input form
- Churn prediction (Yes/No)
- Churn probability score
- Risk level classification (Low / Medium / High)
- Business explanation of prediction

---

## 📈 Output Example

- Churn Probability: 78.45%
- Risk Level: High Risk
- Explanation: High monthly charges and short tenure increase churn likelihood

---

## 🖥️ How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py