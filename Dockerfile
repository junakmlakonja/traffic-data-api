# Use official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000

# Run the app
CMD ["python", "-m", "app.main"]