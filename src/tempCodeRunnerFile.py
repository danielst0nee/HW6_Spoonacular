        print(f"Using API key: {API_KEY}")
        print(f"Making request to: https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=100")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")