from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .hashing import Hash

from . import models, schemas

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

def create_user(req: schemas.UserCreate, db: Session):
    new_user = models.User(username=req.username, email=req.email, password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
