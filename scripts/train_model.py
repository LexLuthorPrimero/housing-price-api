import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os


def train():
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df["target"] = housing.target

    features = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude",
    ]
    target = "target"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Modelo liviano: Regresión Lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE (Linear Regression): ${mae:.2f}")
    print(f"R2: {r2:.4f}")

    os.makedirs("models", exist_ok=True)
    # Guardar modelo comprimido (opcional, pero ya es pequeño)
    joblib.dump(model, "models/housing_price_predictor.pkl", compress=3)
    print("Modelo guardado (tamaño muy pequeño).")

    with open("models/features.txt", "w") as f:
        f.write("\n".join(features))


if __name__ == "__main__":
    train()
