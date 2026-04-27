# 🚀 Concrete Strength Prediction API

This project predicts concrete compressive strength using a Machine Learning model (XGBoost) and serves predictions via a FastAPI-based REST API.

---

## 🌐 Live Demo
🔗 API: https://concrete-deployment.onrender.com  
📘 Docs: https://concrete-deployment.onrender.com/docs  

---

## 🧠 Project Overview
- Built a regression model to predict concrete strength
- Trained using XGBoost Regressor
- Deployed as a REST API using FastAPI
- Hosted on Render cloud platform

---

## ⚙️ Tech Stack
- Python
- XGBoost
- FastAPI
- Scikit-learn
- Render (Deployment)

---

## 📡 API Usage

### Endpoint:
POST `/predict`

### Input Example:
```json
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
