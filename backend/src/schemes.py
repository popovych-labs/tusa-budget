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

class InventoryItem(BaseModel):
    id: int
    item_name: str
    price: int
    tusa_id: int