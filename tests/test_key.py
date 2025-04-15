import os
import requests
import pytest
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("SECRET_KEY")
def test_api_key_validity():
    assert API_KEY is not None and API_KEY != "", "API key is missing or empty"
    #assert API_KEY = f6850151164e4220b30bcb2cbf19a89e5

    # Make a test request to Spoonacular
    url = "https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": API_KEY,
        "number": 1
    }