from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate

# Create a new item in PostgreSQL
def create_item(db: Session, item_in: ItemCreate) -> Item:
    db_item = Item(**item_in.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Fetch all items from PostgreSQL
def get_items(db: Session) -> list[Item]:
    return db.query(Item).all()

# Delete an item by its ID
def delete_item(db: Session, item_id: int) -> bool:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True