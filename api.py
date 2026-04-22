import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

# Cargar modelo y features
model_path = 'models/housing_price_predictor.pkl'
features_path = 'models/features.txt'

if not os.path.exists(model_path):
    raise RuntimeError(f"Modelo no encontrado en {model_path}")
model = joblib.load(model_path)

with open(features_path, 'r') as f:
    FEATURES = [line.strip() for line in f.readlines()]

app = FastAPI(title="California Housing Price Predictor", description="Predice precios de viviendas basado en características", version="1.0")

class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

class PredictionOut(BaseModel):
    price: float

@app.get("/")
def root():
    return {"message": "API de predicción de precios de viviendas"}

@app.post("/predict", response_model=PredictionOut)
def predict(data: InputData):
    # Convertir a array numpy en el orden correcto
    input_array = np.array([[data.MedInc, data.HouseAge, data.AveRooms, data.AveBedrms,
                             data.Population, data.AveOccup, data.Latitude, data.Longitude]])
    prediction = model.predict(input_array)[0]
    return {"price": prediction}
