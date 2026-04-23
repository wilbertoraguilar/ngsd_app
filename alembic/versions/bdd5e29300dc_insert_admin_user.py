"""insert admin user

Revision ID: bdd5e29300dc
Revises: f23e4485f4ef
Create Date: 2026-04-21 18:22:53.308994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdd5e29300dc'
down_revision: Union[str, Sequence[str], None] = 'f23e4485f4ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            """
            INSERT INTO "user" (name, email, password_hash, admin)
            VALUES ('Admin', 'admin@example.com', '$2b$12$VIQvElBNzg7ps02CNEKSsuI0lZ67MH.6Lo0lBi.6dne8RzrN22wDu', TRUE)
            """
        )
    )

def downgrade() -> None:
    op.execute(
        sa.text(
            """
            DELETE FROM "user"
            WHERE email = 'admin@example.com'
            """
        )
    )

