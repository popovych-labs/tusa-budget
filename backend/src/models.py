from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    tables: Mapped[list["TusaTable"]] = relationship(
        secondary="user_tusa_table_association", back_populates="users"
    )


class TusaTable(Base):
    __tablename__ = "tusa_table"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    users: Mapped[list["User"]] = relationship(
        secondary="user_tusa_table_association", back_populates="tusa_table"
    )


class UserTusaTableAssociation(Base):
    __tablename__ = "user_tusa_table_association"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    tusa_table_id: Mapped[int] = mapped_column(
        ForeignKey("tusa_table.id"), primary_key=True)