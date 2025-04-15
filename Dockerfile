# Dockerfile for Random Recipes App
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

#Copy elements of /src into container at /app/src
COPY ./src /app/src

# Copy requirements.txt into the container
COPY requirements.txt requirements.txt

# Install required dependencies using pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy .env file to the container
COPY .env /app/.env

# Copy the data directory into the container
# COPY ./data /app/data

# Specify necessary ports and set run to default command to run app
EXPOSE 8501

# Set environment variables
ENV PYTHONPATH="/app/src"

ARG SECRET_KEY
ENV SECRET_KEY = $SECRET_KEY

# Run the app
CMD [ "streamlit", "run", "--server.port", "8501", "src/Random Recipes.py" ]