"""add order_status table

Revision ID: 977d88b02a5d
Revises: 52ab190dfb86
Create Date: 2026-04-23 13:57:51.265837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '977d88b02a5d'
down_revision: Union[str, Sequence[str], None] = '52ab190dfb86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'order_status' not in inspector.get_table_names():
        op.create_table(
            'order_status',
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('status', sa.String, nullable=False),

        )


def downgrade() -> None:
    op.drop_table('order_status')
