"""
Author: Daniel Stone

Filename: random_recipe.py

File Description:
"""
import streamlit as st
from api_calls import get_random_recipe

st.title("Random Recipe Generator")

num_recipes = st.slider("Number of Recipes", 1, 5, 1)
min_health_score = st.slider("Minimum Health Score", 0, 100, 0)

recipes = get_random_recipe(min_health_score, num_recipes)

if len(recipes) < num_recipes:
    st.warning(f"Only {len(recipes)} recipes with that health score could be found. Please try again.")

for recipe in recipes:
    with st.container(border=True):
        st.header(recipe["title"])
        st.image(recipe["image"])

        st.subheader("Recipe Information:")
        st.write(f"Time: {recipe["time"]} minutes")
        st.write(f"Servings: {recipe["servings"]}")
        st.write(f"Health Score: {recipe["health_score"]}")
        st.write(f"Link: {recipe["link"]}")

        st.subheader("Ingredients:")
        st.markdown("\n".join([f" - {ingredient}" for ingredient in recipe["ingredients"]]))
