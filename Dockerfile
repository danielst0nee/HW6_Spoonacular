# Dockerfile for Random Recipes App
FROM python:3.10-slim

WORKDIR /app

COPY ./src /app/src
COPY ./src/pages /app/src/pages 

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY .env /app/.env
COPY .streamlit /app/.streamlit

# ✅ Create the data directory inside the container
RUN mkdir -p /app/data

EXPOSE 8501

ENV PYTHONPATH="/app/src"
ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

CMD [ "streamlit", "run", "--server.port", "8501", "src/Random Recipes.py" ]
