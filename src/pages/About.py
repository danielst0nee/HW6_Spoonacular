"""
Author: Daniel Stone

Filename: about.py

File Description: Second page that provides a description of the web application to the user
"""
import streamlit as st

st.title("About This App")
st.write("""
         This app helps you find healthy and delicious recipes using the Spoonacular API.
         You can filter recipes by health score and get recommendations.
         """)

st.subheader("How It Works")
st.write("""
- Select your preferred health score range.
- Choose how many recipes you want.
- See the recipes appear!
""")
