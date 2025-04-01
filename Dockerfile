# Dockerfile for Random Recipes App
FROM python:3.10-slim

# Copy the application code into the container
COPY . .

# Install required dependencies using pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Specify necessary ports and set run to default command to run app
EXPOSE 8501
CMD [ "streamlit", "run", "--server.port", "8501", "Random Recipes.py" ]