from functools import lru_cache
from fastapi import FastAPI
from . import config 

app = FastAPI()

@lru_cache()
def get_settings():
    return config.settings

@app.get("/")
def index():
    return "Hello world!"
