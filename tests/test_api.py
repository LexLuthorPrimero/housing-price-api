import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de predicción de precios de viviendas"}

def test_predict_valid():
    payload = {
        "MedInc": 5.0,
        "HouseAge": 30,
        "AveRooms": 6,
        "AveBedrms": 1,
        "Population": 1000,
        "AveOccup": 3,
        "Latitude": 34.0,
        "Longitude": -118.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "price" in response.json()
    assert isinstance(response.json()["price"], float)

def test_predict_missing_field():
    payload = {"MedInc": 5.0}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
