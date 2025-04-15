"""
Author: Daniel Stone

Filename: api_calls.py

File Description: Function for the Spoonacular API calls
"""
import os
from dotenv import load_dotenv
from pathlib import Path
from json import dump, load
from datetime import timedelta
from requests import get
import streamlit as st
from requests.exceptions import RequestException


# Point to the correct .env file
env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path, override=True)

API_KEY = os.getenv("SECRET_KEY")
if not API_KEY:
    raise ValueError("SECRET_KEY is not set")
print(API_KEY)
RECIPE_DATA_FILE = "data/recipe_data.json"


def get_random_recipe(min_health_score: int = 0, num_recipes: int = 1) -> dict:
    """
    Gets a random recipe from Spoonacular API
    """
    recipes = []

    # Attempts API first
    try:
        response = get(f"https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=100", timeout=3)
        print(f"Using API key: {API_KEY}")
        print(f"Making request to: https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=100")
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            recipes = data["recipes"]
            with open(RECIPE_DATA_FILE, "w", encoding="utf-8") as file:
               dump(data, file)
            print("Recipes fetched from API and saved to backup.")
        else:
            print(f"API error {response.status_code}. Attempting to load from backup...")
    except RequestException as e:
        print(f"API request failed: {e}. Attempting to load from backup...")

    if not recipes and os.path.exists(RECIPE_DATA_FILE):
        try:
            with open(RECIPE_DATA_FILE, "r", encoding="utf-8") as file:
                data = load(file)
                recipes = data.get("recipes", [])
            print("Reciped loaded from backup file.")
        except (OSError, ValueError) as e:
            print(f"Failed to load backup file: {e}")
            return []

    if not recipes:
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

my_recipes = get_random_recipe(min_health_score=10, num_recipes=3)