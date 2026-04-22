import pandas as pd
import numpy as np

def clean_properati(input_path='data/raw/properati.csv', output_path='data/processed/properati_clean.csv'):
    # Leer CSV con engine='python' para tolerar errores, saltar líneas mal formadas
    df = pd.read_csv(input_path, engine='python', on_bad_lines='skip', encoding='utf-8')
    # Seleccionar columnas relevantes (las que existen)
    cols = ['place_name', 'state_name', 'lat', 'lon', 'price', 'currency',
            'surface_total', 'surface_covered', 'rooms', 'bedrooms', 'bathrooms',
            'property_type', 'operation_type']
    # Solo mantener columnas que estén en el DataFrame
    available_cols = [c for c in cols if c in df.columns]
    df = df[available_cols].copy()
    # Filtrar solo ventas
    if 'operation_type' in df.columns:
        df = df[df['operation_type'] == 'Venta'].copy()
    # Eliminar filas sin precio o superficie
    df = df.dropna(subset=['price', 'surface_total'])
    # Filtrar precios razonables (entre 10k y 1M USD)
    df = df[(df['price'] > 10000) & (df['price'] < 1000000)]
    # Convertir superficie a float
    df['surface_total'] = pd.to_numeric(df['surface_total'], errors='coerce')
    df = df.dropna(subset=['surface_total'])
    # Crear precio por metro cuadrado
    df['price_per_m2'] = df['price'] / df['surface_total']
    # Limitar valores extremos de price_per_m2
    df = df[(df['price_per_m2'] > 100) & (df['price_per_m2'] < 10000)]
    # Guardar
    df.to_csv(output_path, index=False)
    print(f"Dataset limpiado guardado en {output_path}")
    print(f"Registros: {len(df)}")
    return df

if __name__ == "__main__":
    clean_properati()
