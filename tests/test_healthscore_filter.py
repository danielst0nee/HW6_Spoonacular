"""
Author: Daniel Stone

Filename: test_healthscore_filter.py

File Description: Test to ensure the recipes displayed meet the minimum health score from the user.
"""

from api_calls import get_random_recipe

def test_healthscore_filter() -> None:
    """
    Tests recipes displayed fit healthscore filter
    """
    test_score = 50
    recipes = get_random_recipe(test_score)

    for recipe in recipes:
        assert recipe["health_score"] >= test_score