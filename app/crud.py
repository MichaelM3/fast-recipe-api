from sqlalchemy.orm import Session
from . import models

def get_all_recipes(db: Session):
    recipes = db.query(models.Recipe).all()
    return recipes
