from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

assosiation_table = Table(
    "user_tusa_table_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("tusa_table_id", ForeignKey("tusa_table.id"), primary_key=True),        
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    tables: Mapped[list["TusaTable"]] = relationship(
        secondary="user_tusa_table_association",
        back_populates="users"
    )


class TusaTable(Base):
    __tablename__ = "tusa_table"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    users: Mapped[list["User"]] = relationship(
        secondary="user_tusa_table_association",
        back_populates="tables"
    )