# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY gemini_api.py .

# Expose the application port (default Flask port is 5000)
EXPOSE 5005

# Command to run the Flask application
CMD ["python3", "gemini_api.py"]