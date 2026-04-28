"""add order_line table

Revision ID: 80a1461cd8fc
Revises: 83beb3c89cdd
Create Date: 2026-04-23 14:10:30.401443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80a1461cd8fc'
down_revision: Union[str, Sequence[str], None] = '83beb3c89cdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'order_line' not in inspector.get_table_names():
        op.create_table(
            'order_line',
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('product_id', sa.Integer, sa.ForeignKey("product.id"), nullable=False),
            sa.Column('quantity', sa.Integer, nullable=False),
            sa.Column('subtotal', sa.Float, nullable=False),
            sa.Column('order_id', sa.Integer, sa.ForeignKey("order.id"), nullable=False),
        )


def downgrade() -> None:
    op.drop_table('order_line')

