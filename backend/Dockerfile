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

# Copy and set permissions for entrypoint script
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV IS_DOCKER=True
ENV DJANGO_SETTINGS_MODULE=ispp_project.settings

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/media /app/media/profile_images /app/logs

EXPOSE 8000

# Use entrypoint script
ENTRYPOINT ["/app/docker-entrypoint.sh"]
