"""create token table

Revision ID: e310a62e91a2
Revises: bdd5e29300dc
Create Date: 2026-04-22 13:42:56.426407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e310a62e91a2'
down_revision: Union[str, Sequence[str], None] = 'bdd5e29300dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'token' not in inspector.get_table_names():
        op.create_table(
            'token',
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('user_id', sa.Integer, sa.ForeignKey("user.id")),
            sa.Column('token', sa.String(128), nullable=False, unique=True),
            sa.Column('valid_until', sa.DateTime, nullable=False)
        )



def downgrade() -> None:
    op.drop_table('user')
