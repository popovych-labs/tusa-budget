from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Tusa(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class InventoryItemCreate(BaseModel):
    item_name: str
    price: int
    # owner_name: str

class InventoryItem(InventoryItemCreate):
    id: int
    tusa_id: int