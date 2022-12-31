FROM python:3.8-slim

# Copy application code
COPY requirements.txt requirements.txt

COPY . ./app

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt \
    && pip install Flask gunicorn

# # Expose port 8080
# EXPOSE 8080

# Run the application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app



