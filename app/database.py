import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Load environment variables from .env file
load_dotenv()

# The database address (read from .env)
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
engine = create_engine(DATABASE_URL)

# Create sessions
SessionLocal = sessionmaker(bind=engine)

# Base class for models
class Base(DeclarativeBase):
    pass

# Get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()