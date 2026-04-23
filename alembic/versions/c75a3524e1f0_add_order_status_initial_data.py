"""add order_status initial data

Revision ID: c75a3524e1f0
Revises: 80a1461cd8fc
Create Date: 2026-04-23 15:52:01.283026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c75a3524e1f0'
down_revision: Union[str, Sequence[str], None] = '80a1461cd8fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            """
            INSERT INTO "order_status" (status)
            VALUES
            ('Created'),
            ('Processing'),
            ('Shipped'),
            ('Delivered')
            """
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
