import uvicorn
from fastapi import FastAPI
from database import create_database
from routers import recipes_router

app = FastAPI()

create_database()

app.include_router(recipes_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)