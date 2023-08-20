from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

assosiation_table = Table(
    "user_tusa_association",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("tusa_id", ForeignKey("tusa.id"), primary_key=True),        
)

# assosiation_table = Table(
#     "item_user_association",
#     Base.metadata,
#     Column("inventory_item_id", ForeignKey("inventory_item.id"), primary_key=True),
#     Column("user_id", ForeignKey("users.id"), primary_key=True)
# )

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)

    # owner_inventory_items: Mapped[List["InventoryItem"]] = relationship()
    # participant_inventory_items: Mapped[List["InventoryItem"]] = relationship(
    #     secondary="item_user_association", 
    #     back_populates="participants_ids"
    # )


class Tusa(Base):
    __tablename__ = "tusa"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    participants: Mapped[list[User]] = relationship(secondary="user_tusa_association")

    items: Mapped[list["InventoryItem"]] = relationship(back_populates="tusa")


class InventoryItem(Base):
    __tablename__ = "inventory_item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    tusa_id: Mapped[int] = mapped_column(ForeignKey("tusa.id"))
    tusa: Mapped[Tusa] = relationship(back_populates="items")
    

