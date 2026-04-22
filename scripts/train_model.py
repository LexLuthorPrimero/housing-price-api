import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def train():
    # Cargar dataset
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df['target'] = housing.target
    
    # Features y target
    features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    target = 'target'
    
    X = df[features]
    y = df[target]
    
    # Dividir entrenamiento/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Evaluar
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Error absoluto medio (MAE): {mae:.4f}")
    print(f"R²: {r2:.4f}")
    
    # Guardar modelo
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/housing_price_predictor.pkl')
    print("Modelo guardado en models/housing_price_predictor.pkl")
    
    # Guardar nombres de features
    with open('models/features.txt', 'w') as f:
        f.write('\n'.join(features))

if __name__ == "__main__":
    train()
