from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class Reservation(BaseModel):
   id: UUID
   reserver_name: str
   reserver_email: str
   created_at: datetime

class ItemOutModel(BaseModel):
    id: UUID
    wishlist_id: UUID
    url: str
    title: str
    image_url: str
    price: int
    priority: str
    note: str
    position: int
    is_reserved: bool
    created_at: datetime
    reservation: Reservation

class ItemModel(BaseModel):
    id: UUID
    wishlist_id: UUID
    url: str
    title: str
    image_url: str
    price: int
    priority: str
    note: str
    position: int
    is_reserved: bool
    created_at: datetime
    reservation: Reservation

class ItemOutModel(BaseModel):
    id: UUID
    wishlist_id: UUID
    url: str
    title: str
    image_url: str
    price: int
    priority: str
    note: str
    position: int
    is_reserved: bool
    created_at: datetime
    reservation: Reservation

class ItemPublicModel(BaseModel):
    id: UUID
    title: str
    image_url: str
    price: int
    priority: str
    note: str
    position: int
    is_reserved: bool