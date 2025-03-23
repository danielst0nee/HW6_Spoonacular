"""
Author: Daniel Stone

Filename: api_calls.py

File Description: Functions for the Spoonacular API calls
"""
import os
from json import dump, load
from datetime import timedelta
from requests import get
import streamlit as st


API_KEY = st.secrets["API_key"]
RECIPE_DATA_FILE = "data/recipe_data.json"


@st.cache_data(show_spinner="Finding delicious recpipes...", ttl=timedelta(days=1))
def get_random_recipe(min_health_score: int = 0, num_recipes: int = 1) -> dict:
    """
    Gets a random recipe from Spoonacular API
    """
    data = None

    # Trying to load from JSON file first
    if os.path.exists(RECIPE_DATA_FILE):
        try:
            with open(RECIPE_DATA_FILE, "r", encoding="utf-8") as file:
                data = load(file)
                recipes = data["recipes"]
                if recipes:
                    print("Recipes loaded from backup file")
        except (OSError, ValueError):
            print("Initiating API Request...")

    if not data:
        try:
            response = get(f"https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=100", timeout=3)

            if response.status_code == 200:
                data = response.json()
                with open(RECIPE_DATA_FILE, "w", encoding="utf-8") as file:
                    dump(data, file)
                recipes = data["recipes"]
        except Exception as e:
            print(f"API request failed: {e}")
            return []

    recipe_info = []
    for recipe in recipes:
        if recipe["healthScore"] >= min_health_score:
            recipe_info.append({
                "health_score": recipe["healthScore"],
                "title": recipe["title"],
                "image": recipe["image"],
                "time": recipe["readyInMinutes"],
                "servings": recipe["servings"],
                "link": recipe["sourceUrl"],
                "ingredients": [ingredient["original"] for ingredient in recipe["extendedIngredients"]]
            })
        if len(recipe_info) >= num_recipes:
            break
    return recipe_info


get_random_recipe()
