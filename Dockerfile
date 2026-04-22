FROM python:3.13-slim

WORKDIR /app

# Instalar solo dependencias esenciales (sin gcc innecesario)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código y entrenar modelo (esto generará el modelo pequeño)
COPY . .
RUN python scripts/train_model.py

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
