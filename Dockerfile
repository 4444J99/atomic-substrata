FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY scripts/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY scripts/ ./scripts/
COPY data/ ./data/

# Create non-root user
RUN useradd -m -u 1000 uaks && \
    chown -R uaks:uaks /app
USER uaks

# Expose API port
EXPOSE 8080

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV DATA_DIR=/app/data

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1

# Run API server
CMD ["python", "scripts/api_server.py"]
