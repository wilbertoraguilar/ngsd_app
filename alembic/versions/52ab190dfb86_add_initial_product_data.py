"""add initial product data

Revision ID: 52ab190dfb86
Revises: 0bd61a9bcf9f
Create Date: 2026-04-23 12:20:10.812940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52ab190dfb86'
down_revision: Union[str, Sequence[str], None] = '0bd61a9bcf9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.execute(
        sa.text(
            """
            INSERT INTO "product" (name, description, price, inventory)
            VALUES
            ('E-Commerce done right', 'A comprehensive guide to building successful e-commerce platforms. Hardcover', 29.99, 100),
            ('E-Commerce Simulator', 'Software License', 19.99, 500),
            ('Voucher', 'Event Voucher', 39.99, 200)
            """
        )
    )



def downgrade() -> None:
    """Downgrade schema."""
    pass
