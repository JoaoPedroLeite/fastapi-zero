"""Adicionando created_at e updated_at na tabela de todos

Revision ID: 9ef6b60b62f3
Revises: c9083423f860
Create Date: 2025-06-16 15:42:23.353320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ef6b60b62f3'
down_revision: Union[str, None] = 'c9083423f860'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('todos') as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now()))


def downgrade():
    with op.batch_alter_table('todos') as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')
