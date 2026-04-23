"""add order table

Revision ID: 83beb3c89cdd
Revises: 977d88b02a5d
Create Date: 2026-04-23 14:07:04.049892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83beb3c89cdd'
down_revision: Union[str, Sequence[str], None] = '977d88b02a5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'order',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("user.id"), nullable=False),
        sa.Column('status_id', sa.Integer, sa.ForeignKey("order_status.id"), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),


    )


def downgrade() -> None:
    op.drop_table('order')
