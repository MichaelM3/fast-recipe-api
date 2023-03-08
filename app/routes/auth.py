from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, database, crud
from ..hashing import Hash
from .token import create_access_token

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == req.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username or password")

    if not Hash.verify(req.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})
    return { "access_token": access_token, "token_type": "bearer" }

@router.post("/register")
def register(req: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(req, db)
