from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    item: str
    category: str
    quantity: int
    price: int | float

class ItemResponse(BaseModel):
    id: int
    item: str
    category: str
    quantity: int
    price: int|float
    

class ItemUpdate(BaseModel):
    item: Optional[str] 
    category: Optional[str] 
    quantity: Optional[int] 
    price: Optional[int|float] 
    
