"""Add InventoryItem table with relationship to Tusa

Revision ID: cbd002bdb3ca
Revises: 74c83e92e270
Create Date: 2023-08-20 12:52:34.804563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbd002bdb3ca'
down_revision: Union[str, None] = '74c83e92e270'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('tusa_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tusa_id'], ['tusa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_item_id'), 'inventory_item', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_item_id'), table_name='inventory_item')
    op.drop_table('inventory_item')
    # ### end Alembic commands ###
