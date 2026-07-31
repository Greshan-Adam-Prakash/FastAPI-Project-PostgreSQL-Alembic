"""add content column

Revision ID: ab4577394dac
Revises: 180d48ca5567
Create Date: 2026-07-31 21:02:48.298691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab4577394dac'
down_revision: Union[str, Sequence[str], None] = '180d48ca5567'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
