# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on
EXPOSE 8080

# Command to run the application
CMD ["python", "heos-http-control.py"]

