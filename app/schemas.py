from typing import List, Optional
from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    summary: str = ""
    image: Optional[str] = None
    spoonacular_id: int
    class Config:
        orm_mode = True

class RecipeShow(RecipeBase):
    pass

class UserBase(BaseModel):
    username: str
    email: str
    image: Optional[str] = None
    recipes: List[RecipeShow] = []

    class Config:
        orm_mode = True

class UserShow(UserBase):
    pass

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

