import streamlit as st
import requests

st.set_page_config(page_title="Predicción de Precios de Viviendas", layout="centered")
st.title("🏠 Predicción de Precios de Viviendas (California)")
st.markdown(
    "Ingresa las características de la vivienda para obtener una estimación de su precio."
)

# URL de la API (cambiar si se despliega en Render)
API_URL = "https://housing-price-api.onrender.com/predict"

with st.form("prediction_form"):
    st.subheader("Características")
    col1, col2 = st.columns(2)
    with col1:
        med_inc = st.number_input(
            "Ingreso medio (MedInc)", min_value=0.0, value=5.0, step=0.5
        )
        house_age = st.number_input(
            "Edad media de la casa (HouseAge)", min_value=0.0, value=30.0, step=5.0
        )
        ave_rooms = st.number_input(
            "Promedio de habitaciones (AveRooms)", min_value=0.0, value=6.0, step=0.5
        )
        ave_bedrms = st.number_input(
            "Promedio de dormitorios (AveBedrms)", min_value=0.0, value=1.0, step=0.5
        )
    with col2:
        population = st.number_input(
            "Población (Population)", min_value=0.0, value=1000.0, step=100.0
        )
        ave_occup = st.number_input(
            "Promedio de ocupación (AveOccup)", min_value=0.0, value=3.0, step=0.5
        )
        latitude = st.number_input(
            "Latitud (Latitude)", min_value=32.0, max_value=42.0, value=34.0, step=0.5
        )
        longitude = st.number_input(
            "Longitud (Longitude)",
            min_value=-125.0,
            max_value=-114.0,
            value=-118.0,
            step=0.5,
        )

    submitted = st.form_submit_button("Predecir precio")

    if submitted:
        payload = {
            "MedInc": med_inc,
            "HouseAge": house_age,
            "AveRooms": ave_rooms,
            "AveBedrms": ave_bedrms,
            "Population": population,
            "AveOccup": ave_occup,
            "Latitude": latitude,
            "Longitude": longitude,
        }
        try:
            response = requests.post(API_URL, json=payload, timeout=10)
            if response.status_code == 200:
                price = response.json()["price"]
                st.success(
                    f"💰 Precio estimado: **${price*100000:.2f} USD** (valor real en cientos de miles)"
                )
                st.info(
                    "Nota: El modelo predice precios en cientos de miles de dólares. Multiplica por 100,000 para obtener el valor real."
                )
            else:
                st.error(f"Error en la API: {response.status_code}")
        except Exception as e:
            st.error(f"No se pudo conectar a la API: {e}")
