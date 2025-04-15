# Dockerfile for Random Recipes App
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

#Copy elements of /src into container at /app/src
COPY ./src /app/src

# Install required dependencies using pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Ensure .env is in the container
COPY .env .env

# Set environment variables
ENV PYTHONPATH="/app/src"

# Specify necessary ports and set run to default command to run app
EXPOSE 8501

# Run the app
CMD [ "streamlit", "run", "--server.port", "8501", "src/Random Recipes.py" ]