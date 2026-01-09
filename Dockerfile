FROM python:3.10-slim

WORKDIR /app

# Prevenir archivos .pyc y buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para lanzar la app apuntando al módulo app.main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]