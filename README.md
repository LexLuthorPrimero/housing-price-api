[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green.svg)](https://fastapi.tiangolo.com)
[![Coverage](badges/coverage.svg)](https://github.com/LexLuthorPrimero/housing-price-api)
[![Render](https://img.shields.io/badge/Render-API-46E3B7)](https://housing-price-api-1-p1hf.onrender.com)
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://housing-price-api-vhnugf6deyxkt8xri92wy6.streamlit.app)

# 🏠 Housing Price Prediction API

API de predicción de precios de viviendas basada en el dataset **California Housing**.
El modelo utiliza regresión lineal para estimar el precio en cientos de miles de dólares.

## 🚀 Tecnologías

- **Python 3.13**
- **FastAPI** (backend)
- **Streamlit** (frontend interactivo)
- **scikit-learn** (entrenamiento)
- **Docker** + **Render** (despliegue)

## 📦 Instalación y uso local

```bash
git clone https://github.com/LexLuthorPrimero/housing-price-api.git
cd housing-price-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/train_model.py   # entrena el modelo
uvicorn api:app --reload        # levanta la API en http://localhost:8000
streamlit run app_frontend.py   # levanta el frontend en http://localhost:8501
```

## 🌐 Demo en línea

- **API**: [https://housing-price-api-1-p1hf.onrender.com](https://housing-price-api-1-p1hf.onrender.com)
- **Frontend interactivo**: [https://housing-price-api-frontend.streamlit.app](https://housing-price-api-frontend.streamlit.app) (si lo despliegas)

## 📊 Uso de la API

**Endpoint:** `POST /predict`

**Body (JSON):**
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

**Respuesta:**
```json
{"price": 2.30433}
```

> El precio está en cientos de miles de dólares (ej. 2.30 = $230,000 USD).

## 📄 Licencia

MIT

## 👤 Autor

**Lucas Cañete**  
[GitHub](https://github.com/LexLuthorPrimero) · [LinkedIn](https://www.linkedin.com/in/lucas-ca%C3%B1ete-823591236/)
