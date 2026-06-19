# 🍷 WineIQ Analytics

AI-Powered Wine Quality Intelligence Platform built with Machine Learning, Streamlit, and Plotly.

---

## 📌 Project Overview

WineIQ Analytics is a production-ready machine learning application that predicts wine quality using physicochemical attributes.

The platform combines:

* Machine Learning
* Interactive Analytics
* Real-Time Predictions
* Data Visualization
* Business Insights

into a modern SaaS-style dashboard.

---

## 🎯 Problem Statement

Wine quality evaluation is traditionally performed by expert tasters.

This project uses Machine Learning to predict wine quality from measurable chemical properties, enabling faster and more consistent quality assessment.

---

## 🏗 Architecture

```text
                ┌─────────────┐
                │    User     │
                └──────┬──────┘
                       │
                       ▼
            ┌────────────────────┐
            │ Streamlit Frontend │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Prediction Engine  │
            └─────────┬──────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌──────────────┐           ┌────────────────┐
│ scaler.pkl   │           │ model.pkl      │
└──────────────┘           └────────────────┘
        │                           │
        └─────────────┬─────────────┘
                      ▼
             Prediction Output
```

---

## ✨ Features

### Dashboard

* Hero Section
* KPI Cards
* Interactive Visualizations
* Correlation Analysis

### Prediction Engine

* Real-Time Wine Prediction
* Interactive Input Form
* Prediction Summary

### Analytics

* Quality Distribution
* Correlation Heatmap
* Dataset Explorer
* CSV Download

### Model Insights

* Feature Importance
* Model Comparison
* Business Insights

---

## 📊 Dataset

Wine Quality Dataset

* Samples: 1599
* Features: 11
* Target: Wine Quality

Features include:

* Alcohol
* pH
* Sulphates
* Density
* Chlorides
* Citric Acid
* Residual Sugar

---

## 🤖 Machine Learning Pipeline

Models Trained:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest

Best Model:

Random Forest

Accuracy:

~90%

---

## 🛠 Tech Stack

Frontend:

* Streamlit

Backend:

* Python

Machine Learning:

* Scikit-Learn

Visualization:

* Plotly
* Matplotlib

Data Processing:

* Pandas
* NumPy

Model Storage:

* Joblib

---

## 📸 Screenshots

### Dashboard

Add screenshot here:

screenshots/dashboard.png

### Prediction

Add screenshot here:

screenshots/prediction.png

### Analytics

Add screenshot here:

screenshots/analytics.png

---

## ⚙ Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/wineiq-analytics.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train model

```bash
python train.py
```

Run application

```bash
streamlit run app/app.py
```

---

## ☁ Deployment

### GitHub

Push project to GitHub.

### Streamlit Cloud

1. Login with GitHub
2. Create App
3. Select repository
4. Main file:

```text
app/app.py
```

5. Deploy

---

## 🚀 Future Enhancements

* SHAP Explainability
* PDF Reports
* Authentication
* CI/CD Pipeline
* Prediction History

---

## 👨‍💻 Author

Hemanth Reddy

CSE (AI & ML)

WineIQ Analytics

