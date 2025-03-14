"""
Author: Daniel Stone

Filename: api_calls.py

File Description: Functions for the Spoonacular API calls
"""
from requests import get
import streamlit as st

API_KEY = st.secrets["API_key"]


def get_random_recipe():
    """
    Gets a random recipe from Spoonacular API
    """
    try:
        response = get(f"https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=", timeout=3)
    except OSError:
        print("Request Failed")

    if response.status_code == 200:
        data = response.json()
        recipes = data["recipes"][0]
        recipe_info = {
            "title": recipes["title"],
            "image": recipes["image"]
        }
        return recipe_info
    else:
        print("it didn't work")


get_random_recipe()
