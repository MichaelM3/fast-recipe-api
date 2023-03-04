from functools import lru_cache
from fastapi import FastAPI
from . import config, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@lru_cache()
def get_settings():
    return config.settings

@app.get("/")
def index():
    return "Hello world!"
