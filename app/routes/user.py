from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database, schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
def create_user(req: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(req, db)
