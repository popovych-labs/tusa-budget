from typing import Optional

import os
from sqlalchemy.orm import Session

from . import models, schemes

# User CRUD

def create_user(db: Session, user: schemes.UserCreate):

    hashed_password = user.password

    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_tusa(db: Session, creator_username: str, name: Optional[str] = ""):
    tusa_name = name if name else f"Tusa_{ int.from_bytes(os.urandom(5), byteorder='little')}"

    db_user = get_user_by_username(db, username=creator_username)
    db_tusa = models.Tusa(name=tusa_name)
    db_tusa.participants.append(db_user)

    db.add(db_tusa)
    db.commit()
    db.refresh(db_tusa)
    return db_tusa



def get_tusa_tables_by_username(db: Session, username: str):
    return db.query(models.Tusa
            ).join(models.user_tusa_association
            ).join(models.User
            ).filter(models.User.username == username
            ).all()

def get_tusa_table_by_id(db: Session, id: int):
    return db.query(models.Tusa
            ).filter(models.Tusa.id == id
            ).first()

def get_inventory_items_by_tusa_id(db: Session, id: int):
    return db.query(models.InventoryItem
            ).join(models.Tusa
            ).filter(models.Tusa.id == id
            ).join(models.User, models.InventoryItem.owner_id == models.User.id 
            ).options(
            ).all()

