"""create product table

Revision ID: 0bd61a9bcf9f
Revises: e310a62e91a2
Create Date: 2026-04-23 12:02:43.701240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bd61a9bcf9f'
down_revision: Union[str, Sequence[str], None] = 'e310a62e91a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('inventory', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('product')
