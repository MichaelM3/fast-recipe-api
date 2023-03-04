import uuid
from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), index=True)
    username = Column(String(15), unique=True, nullable=False, index=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    image = Column(String(200), default="")
    recipes = relationship("Recipe", secondary="user_recipe_assocation_table", back_populates="users")

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), index=True)
    title = Column(String(), nullable=False, index=True)
    summary = Column(String(), default="No summary given")
    image = Column(String(), default="")
    spoonacularId = Column(Integer, nullable=False)
    users = relationship("User", secondary="user_recipe_assocation_table", back_populates="recipes")

user_recipe_assocation_table = Table("user_recipe_assocation_table", Base.metadata, 
    Column("user_id", String(36), ForeignKey("users.id"), primary_key=True),
    Column("recipe_id", String(36), ForeignKey("recipes.id"), primary_key=True)
)

