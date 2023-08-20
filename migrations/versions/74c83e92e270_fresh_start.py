"""Fresh start

Revision ID: 74c83e92e270
Revises: 2050d207702d
Create Date: 2023-08-20 12:11:54.904183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74c83e92e270'
down_revision: Union[str, None] = '2050d207702d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tusa',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tusa_id'), 'tusa', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('user_tusa_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tusa_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tusa_id'], ['tusa.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tusa_id')
    )
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_table('user_tusa_table_association')
    op.drop_index('ix_tusa_table_id', table_name='tusa_table')
    op.drop_table('tusa_table')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tusa_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tusa_table_id', 'tusa_table', ['id'], unique=False)
    op.create_table('user_tusa_table_association',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('tusa_table_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['tusa_table_id'], ['tusa_table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tusa_table_id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.drop_table('user_tusa_association')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tusa_id'), table_name='tusa')
    op.drop_table('tusa')
    # ### end Alembic commands ###
