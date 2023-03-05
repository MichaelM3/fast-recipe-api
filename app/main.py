from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import config, models
from .database import engine
from .routes import recipe
from .fetch_recipes import get_recipes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@lru_cache()
def get_settings():
    return config.settings

app.include_router(recipe.router)

@app.get("/search")
async def search_recipe(ingredient: str):
    recipes = await get_recipes(ingredient)
    return recipes
