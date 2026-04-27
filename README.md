# Concrete Strength Prediction API

This project predicts concrete compressive strength using XGBoost.

## 🚀 Features
- Machine Learning Model (XGBoost)
- FastAPI Deployment
- REST API

## 📦 Installation
pip install -r requirements.txt

## ▶️ Run Locally
uvicorn app:app --reload

## 📡 API Endpoint
POST /predict

## 📊 Input Example
{
  "cement": 540.0,
  "slag": 0.0,
  "ash": 0.0,
  "water": 162.0,
  "superplasticizer": 2.5,
  "coarseagg": 1040.0,
  "fineagg": 676.0,
  "age": 28
}

## 🧠 Model
Trained using XGBoost Regressor

## ☁️ Deployment
Deployed on Render / Railway
