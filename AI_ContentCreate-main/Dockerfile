# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default port (Railway will override this automatically via $PORT)
ENV PORT=5001

# Run the Flask app with gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT web_app:app
