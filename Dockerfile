# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the container
COPY . /app/

# Expose the port that the application will listen on
EXPOSE 5000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "5000"]