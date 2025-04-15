"""
Author: Daniel Stone

Filename: test_data.py

File Description: This file provides test cases for the Random Recipe Generator application.
"""
import sys
import os
import json
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api_calls import get_random_recipe


def test_get_random_recipe() -> None:
    """
    Test that the get_random_recipe function returns the expected content, and
    that the response matches what's saved in the recipe_data.json file.
    """
    # Clear the Streamlit cache to ensure fresh data is fetched
    st.cache_data.clear()

    # Get response from the API
    data = get_random_recipe()

    # Save this response to a backup file for later comparison
    with open("./data/recipe_data_backup.json", "w", encoding="utf-8") as backup_file:
        json.dump(data, backup_file, ensure_ascii=False, indent=4)

    # Load the data from recipe_data.json
    with open("./data/recipe_data.json", "r", encoding="utf-8") as file:
        test_data = json.load(file)

    # Prepare the data in the same format as the API response for comparison
    recipe_info = []
    for recipe in test_data["recipes"]:
        recipe_info.append({
            "health_score": recipe["healthScore"],
            "title": recipe["title"],
            "image": recipe["image"],
            "time": recipe["readyInMinutes"],
            "servings": recipe["servings"],
            "link": recipe["sourceUrl"],
            "ingredients": [ingredient["original"] for ingredient in recipe["extendedIngredients"]]
        })

    # Debugging: Print both responses to check the data
    #print("API response:", data)
    #print("File response:", recipe_info)

    # Compare first few items to ensure they match, even if there are extra items
    for api_recipe, file_recipe in zip(data, recipe_info):
        assert api_recipe == file_recipe, f"Mismatch between API recipe and file recipe: "
    