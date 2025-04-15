"""
Author: Daniel Stone

Filename: test_API_key.py

File Description: This file tests the API key as an environment variable
"""
import os

def test_api_key() -> None:
    """Test API key as an environment variable"""
    api_key = os.environ.get("API_KEY", None)
    assert api_key == "0376596f3a6c42cab4d065d7c7553ae5"