FROM docker.arvancloud.ir/python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install --fix-missing -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV IS_DOCKER=True
ENV DJANGO_SETTINGS_MODULE=ispp_project.settings

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/media

EXPOSE 8000

# Use Gunicorn for production
CMD ["gunicorn", "ispp_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
