FROM python:3.13-slim

WORKDIR /app

# Instalar compiladores y herramientas necesarias para compilar numpy
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias (incluyendo pandas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código y entrenar modelo
COPY . .
RUN python scripts/train_model.py

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
