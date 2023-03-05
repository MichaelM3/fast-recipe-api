from .config import settings
import requests

async def get_recipes(ingredient: str):
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={ingredient}"
    headers = { "x-api-key": settings.API_KEY, "Content-Type": "application/json" }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
