from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TusaTable(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserTusaMany(User):
    tusa_table_id: list[TusaTable]

class TusaUserMany(User):
    users_id: list[User]