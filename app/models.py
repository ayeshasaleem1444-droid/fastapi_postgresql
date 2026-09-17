from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, func
from app.database import Base                   


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default= func.now())