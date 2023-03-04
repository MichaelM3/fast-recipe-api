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
