import streamlit as st
import requests

st.set_page_config(page_title="Test API", layout="centered")
st.title("Test de conexión a la API")

API_URL = "https://housing-price-api-1-p1hf.onrender.com/predict"

if st.button("Probar conexión"):
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
    try:
        st.write("Enviando petición a:", API_URL)
        response = requests.post(API_URL, json=payload, timeout=10)
        st.write("Código de estado:", response.status_code)
        st.write("Respuesta completa:", response.text)
        if response.status_code == 200:
            data = response.json()
            st.success("Respuesta JSON: " + str(data))
            if "price" in data:
                st.success(f"Precio: {data['price']}")
            else:
                st.error("La respuesta no contiene 'price'")
        else:
            st.error(f"Error HTTP {response.status_code}")
    except Exception as e:
        st.error(f"Excepción: {e}")
