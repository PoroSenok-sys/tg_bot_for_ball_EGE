"""add is_registered field

Revision ID: ecdefea84a2d
Revises: 2b684740478a
Create Date: 2024-12-04 20:19:12.276303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecdefea84a2d'
down_revision: Union[str, None] = '2b684740478a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('is_registered', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'is_registered')
    # ### end Alembic commands ###
