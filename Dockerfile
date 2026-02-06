FROM python:3.11-slim

LABEL maintainer="KnowledgeRAG Team"
LABEL description="KnowledgeRAG - Retrieval Augmented Generation API"

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py embed.py k8s.txt ./

# Run embedding initialization
RUN python embed.py

# Expose application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]