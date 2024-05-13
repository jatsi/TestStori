# Use an official Python runtime as a parent image
FROM python:3.10

# Install ncat for network communication
RUN apt-get update && apt-get install -y ncat

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Run main.py from src directory when the container launches
CMD ["python3", "./src/main.py"]
