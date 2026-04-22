# Housing Price Prediction API

API para predecir precios de viviendas usando Random Forest Regressor (California Housing dataset).

## Tecnologías

- Python 3.14
- FastAPI
- scikit-learn
- Docker
- GitHub Actions (próximamente)

## Instalación y uso local

```bash
git clone https://github.com/LexLuthorPrimero/housing-price-api.git
cd housing-price-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/train_model.py   # genera el modelo
python scripts/run_api.py       # inicia la API en http://localhost:8000
```

## Endpoint

`POST /predict`

Body (JSON):
```json
{
  "MedInc": 5.0,
  "HouseAge": 30,
  "AveRooms": 6,
  "AveBedrms": 1,
  "Population": 1000,
  "AveOccup": 3,
  "Latitude": 34.0,
  "Longitude": -118.0
}
```

Respuesta:
```json
{"price": 2.30433}
```

## Demo (próximamente)

## Licencia

MIT
