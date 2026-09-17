from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Schema for incoming request data when creating an item
class ItemCreate(BaseModel):
    title: str
    description: str | None = None
    price: float

# Schema for outgoing data sent back to the user
class ItemResponse(ItemCreate):
    id: int
    created_at: datetime

    # Tells Pydantic to automatically convert SQLAlchemy database models into JSON
    model_config = ConfigDict(from_attributes=True)