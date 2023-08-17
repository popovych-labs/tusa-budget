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


def get_tusa_tables_by_username(db: Session, username: str):
    return db.query(models.TusaTable
            ).join(models.assosiation_table
            ).join(models.User
            ).filter(models.User.username == username
            ).all()


