# Use a lightweight Python image
#FROM python:3.9-slim
FROM python:3.10.12

# Set the working directory
WORKDIR /app

# Copy the script and JSON file
COPY mailer_service.py /app/
COPY data.json /app/

# Run the script
CMD ["python", "mailer_service.py"]

