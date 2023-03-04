from functools import lru_cache
from fastapi import FastAPI
from . import config, models
from .database import engine
from .routes import recipe

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@lru_cache()
def get_settings():
    return config.settings

app.include_router(recipe.router)
