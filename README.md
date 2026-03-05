# Restaurant Rating Prediction

A machine learning web app that predicts a restaurant's aggregate rating based on its features, built with scikit-learn and Streamlit.

---

## Overview

This project trains a **Random Forest Regressor** (tuned with GridSearchCV) on the Zomato restaurant dataset to predict a restaurant's aggregate rating score. The trained model is served through a Streamlit app where you can enter restaurant details and get an instant predicted rating with a review class label (Poor → Excellent).

---

## Demo

Enter the restaurant details and click **Predict Rating and Review** to see:
- A **predicted aggregate rating score**
- A **review class label** — Poor, Average, Good, Very Good, or Excellent

---

## Dataset

**Zomato Restaurant Dataset** (`Dataset.csv`)

- ~9,500 restaurant records from multiple countries
- Features include cost, table booking, online delivery, price range, cuisines, votes, and more
- Target: `Aggregate rating` (continuous, 0–5 scale)

---

## Model

| Detail | Value |
|---|---|
| Algorithm | Random Forest Regressor |
| Tuning | GridSearchCV (`max_depth`: [5, 15], `n_estimators`: [2, 5, 10]) |
| Best params | `max_depth=5`, `n_estimators=10` |
| Preprocessing | StandardScaler (saved via `scaler.pkl`) |
| MAE | 0.352 |
| RMSE | 0.453 |

---

## Rating Classes

| Score | Label |
|---|---|
| < 2.5 | Poor 😞 |
| 2.5 – 3.4 | Average 😐 |
| 3.5 – 3.9 | Good 🙂 |
| 4.0 – 4.4 | Very Good 😃 |
| ≥ 4.5 | Excellent 🌟 |

---

## Input Features

| Feature | Type |
|---|---|
| Average cost for two | Numeric |
| Has Table Booking | Yes / No |
| Has Online Delivery | Yes / No |
| Price Range | 1 – 4 |

---

## Project Structure

```
.
├── app.py               # Streamlit app
├── Restaurant.ipynb     # Training notebook (run on Google Colab)
├── mlmodel.pkl          # Saved Random Forest Regressor (GridSearchCV best estimator)
├── scaler.pkl           # Saved StandardScaler
├── Dataset.csv          # Zomato restaurant dataset
└── requirements.txt     # Python dependencies
```

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

Make sure `mlmodel.pkl` and `scaler.pkl` are in the same directory as `app.py`.

---

## Requirements

```
streamlit
numpy
scikit-learn
joblib
```
