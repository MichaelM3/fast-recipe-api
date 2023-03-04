from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

@router.get("/")
def get_all(db: Session = Depends(database.get_db)):
    return crud.get_all_recipes(db)

@router.get("/{id}")
def show_recipe(id: int, db: Session = Depends(database.get_db)):
    return crud.show_recipe(id, db)
