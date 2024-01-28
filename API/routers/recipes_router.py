import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import RecipeCreate, Recipe
from database import SessionLocal, RecipeModel

recipes_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@recipes_router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe_data: RecipeCreate, db: Session = Depends(get_db)):
    # Tworzenie nowego obiektu RecipeModel na podstawie danych z RecipeCreate
    db_recipe = RecipeModel(
        name=recipe_data.name, 
        ingredients=recipe_data.ingredients,  # Przypisanie jako zwykły string
        content=recipe_data.content
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    
    # Konwersja obiektu bazy danych na schemat Pydantic do odpowiedzi
    return Recipe(
        id=db_recipe.id, 
        name=db_recipe.name, 
        ingredients=db_recipe.ingredients, 
        content=db_recipe.content
    )

@recipes_router.delete("/recipes/{recipe_name}")
def delete_recipe(recipe_name: str, db: Session = Depends(get_db)):
    db_recipe = db.query(RecipeModel).filter(RecipeModel.name == recipe_name).first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Przepis nie znaleziony")
    db.delete(db_recipe)
    db.commit()
    return {"ok": True}

@recipes_router.get("/recipes/{recipe_name}", response_model=Recipe)
def get_recipe(recipe_name: str, db: Session = Depends(get_db)):
    db_recipe = db.query(RecipeModel).filter(RecipeModel.name == recipe_name).first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Przepis nie znaleziony")
    return db_recipe
