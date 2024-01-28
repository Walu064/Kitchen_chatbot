from pydantic import BaseModel
from typing import List

class RecipeCreate(BaseModel):
    name: str
    ingredients: str
    content: str

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: str
    content: str

    class Config:
        from_attributes = True