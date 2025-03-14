"""
Author: Daniel Stone

Filename: random_recipe.py

File Description:
"""
import streamlit as st
from api_calls import get_random_recipe

st.title("Random Recipe Generator")

recipe = get_random_recipe()
st.header(recipe["title"])
st.image(recipe["image"])
