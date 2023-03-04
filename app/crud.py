from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import models

def get_all_recipes(db: Session):
    recipes = db.query(models.Recipe).all()
    return recipes

def show_recipe(id: int, db: Session):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No recipe found with that id"
        )
    return recipe
