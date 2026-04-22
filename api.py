import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

model_path = 'models/housing_price_predictor.pkl'
if not os.path.exists(model_path):
    raise RuntimeError(f"Modelo no encontrado en {model_path}")
model = joblib.load(model_path)

app = FastAPI(title="California Housing Price Predictor")

# Configurar CORS para que el frontend (Streamlit Cloud) pueda llamar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En producción, limita a la URL de tu frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    input_array = np.array([[data.MedInc, data.HouseAge, data.AveRooms, data.AveBedrms,
                             data.Population, data.AveOccup, data.Latitude, data.Longitude]])
    prediction = model.predict(input_array)[0]
    return {"price": prediction}
