# Telco Customer Churn Prediction

## Problem Statement

Customer churn — when a customer stops doing business with a company — is a critical problem for telecom providers. It directly affects profitability and business growth. The Telco dataset includes customer demographics, services signed up for, and account details, which can be used to predict if a customer is likely to churn.

---

## Objective

The goal of this project is to build a **reusable, production-ready machine learning pipeline** that accurately predicts customer churn using the Telco Customer Churn dataset. The pipeline should be:

- Modular and maintainable using `Pipeline` and `ColumnTransformer`
- Tuned for best performance using `GridSearchCV`
- Exportable using `joblib` for reuse in deployment environments

---

## 📁 Dataset

**Telco Customer Churn Dataset**  
Available on [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)

- `7043` customer records
- Features include:
  - Demographics (`gender`, `SeniorCitizen`, etc.)
  - Services (`PhoneService`, `InternetService`, etc.)
  - Account info (`Contract`, `PaymentMethod`, `MonthlyCharges`, etc.)
  - Target: `Churn` (Yes/No)

---

## Project Workflow

1. **Data Cleaning & Exploration**
   - Checked for nulls and data types
   - Encoded target variable
2. **Feature Engineering**
   - Handled categorical variables via One-Hot and Ordinal Encoding
   - Imputed missing values using `SimpleImputer`
3. **Pipeline Construction**
   - Used `Pipeline` and `ColumnTransformer` for preprocessing + modeling
   - Scaled numeric features and encoded categorical features
4. **Model Training**
   - Logistic Regression and Random Forest
   - Used `GridSearchCV` for hyperparameter tuning
5. **Evaluation**
   - Evaluated on accuracy, precision, and recall
6. **Export**
   - Saved best pipeline using `joblib` for later use

---

## Models Used

- **Logistic Regression**
- **Random Forest Classifier**

---

## 📈 Evaluation Metrics

| Metric     | Description                                |
|------------|--------------------------------------------|
| Accuracy   | Overall correctness                        |
| Precision  | True churns correctly predicted            |
| Recall     | Coverage of actual churns                  |

---

## Output

- Final trained pipeline: `churn_prediction_pipeline.pkl`

---

##  Summary

This project demonstrates how to:
- Build an end-to-end ML pipeline with Scikit-learn
- Handle both numeric and categorical features using proper preprocessing
- Tune model parameters with cross-validation
- Package the model for production using `joblib`

The result is a clean, modular pipeline that can be easily reused or deployed to predict customer churn in real-world settings.

---

## Skills Applied

- ML Pipeline Construction
- Feature Engineering
- Hyperparameter Tuning with GridSearchCV
- Model Evaluation
- Production-Readiness and Export

