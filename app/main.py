from fastapi import FastAPI

from app.database import Base, engine
from app.routers import router as item_router

# Auto-creates the tables in PostgreSQL if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + Postgres CRUD API")

# Connect the item endpoints
app.include_router(item_router)


@app.get("/")
def home():
    return {"message": "API is up and running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
