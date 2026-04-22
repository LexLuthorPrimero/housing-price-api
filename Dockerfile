FROM python:3.13-slim

WORKDIR /app

# Instalar dependencias (incluyendo pandas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código y entrenar modelo
COPY . .
RUN python scripts/train_model.py

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
