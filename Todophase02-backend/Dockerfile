FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install Python dependencies directly
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
    fastapi \
    sqlmodel \
    uvicorn[standard] \
    pydantic-settings \
    python-jose[cryptography] \
    python-multipart \
    psycopg2-binary \
    passlib==1.7.4 \
    bcrypt==3.2.0 \
    python-dotenv \
    alembic

# Copy application code
COPY --chown=user . /app

# Expose port for Hugging Face Spaces
EXPOSE 7860

# Set environment variables for Hugging Face Spaces
ENV HOST=0.0.0.0
ENV PORT=7860

# Run the application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]