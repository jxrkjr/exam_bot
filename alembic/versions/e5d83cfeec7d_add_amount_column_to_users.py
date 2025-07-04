"""add amount column to users

Revision ID: e5d83cfeec7d
Revises: d212ab99cb45
Create Date: 2025-06-20 22:51:25.566477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5d83cfeec7d'
down_revision: Union[str, Sequence[str], None] = 'd212ab99cb45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'amount',
               existing_type=sa.NUMERIC(precision=12, scale=2),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'amount',
               existing_type=sa.NUMERIC(precision=12, scale=2),
               nullable=True)
    # ### end Alembic commands ###
