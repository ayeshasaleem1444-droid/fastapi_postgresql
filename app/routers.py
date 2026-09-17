from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ItemCreate, ItemResponse
import app.crud as crud

# Create a router instance with a prefix for all routes
router = APIRouter(prefix="/items", tags=["Items"])

# Endpoint to create a new item
@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item_in=item_in)

# Endpoint to fetch all items
@router.get("/", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db=db)

# Endpoint to delete an item by ID
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    success = crud.delete_item(db=db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")