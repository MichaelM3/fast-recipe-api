from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
        tags=["Authentication"]
)

@router.post("/login")
def login(req: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == req.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username or password")
    return user
