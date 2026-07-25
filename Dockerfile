# ─────────────────────────────────────────────
#  STAGE: imagen base Python ligera
# ─────────────────────────────────────────────
FROM python:3.12-slim

# Evita que Python genere archivos .pyc y fuerza salida sin buffer (logs en tiempo real)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# ─────────────────────────────────────────────
#  Instalar dependencias del sistema
# ─────────────────────────────────────────────
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ─────────────────────────────────────────────
#  Instalar dependencias de Python
# ─────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ─────────────────────────────────────────────
#  Copiar todo el proyecto al contenedor
# ─────────────────────────────────────────────
COPY . .

# ─────────────────────────────────────────────
#  Recolectar archivos estaticos (CSS, JS, img)
# ─────────────────────────────────────────────
RUN python manage.py collectstatic --noinput

# ─────────────────────────────────────────────
#  Puerto expuesto
# ─────────────────────────────────────────────
EXPOSE 8000

# ─────────────────────────────────────────────
#  Comando para iniciar la aplicacion con Gunicorn
# ─────────────────────────────────────────────
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
