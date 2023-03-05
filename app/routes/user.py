from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database, schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

