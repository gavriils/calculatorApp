# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /docker_app_test

# Copy the requirements and main script into the container
COPY requirements.txt main.py ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to run the Python script
ENTRYPOINT ["python", "main.py"]