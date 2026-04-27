from fastapi import FastAPI
import joblib
import numpy as np

# Load model
model = joblib.load("concrete_model.pkl")

# Create app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Concrete Strength Prediction API"}

@app.post("/predict")
def predict(data: dict):
    # Input order:
    # [cement, slag, ash, water, superplasticizer, coarseagg, fineagg, age]
    
    values = np.array([[
        data["cement"],
        data["slag"],
        data["ash"],
        data["water"],
        data["superplasticizer"],
        data["coarseagg"],
        data["fineagg"],
        data["age"]
    ]])

    prediction = model.predict(values)

    return {"prediction": float(prediction[0])}