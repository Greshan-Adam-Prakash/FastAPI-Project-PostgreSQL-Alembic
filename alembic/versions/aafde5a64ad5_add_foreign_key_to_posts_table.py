"""add foreign-key to posts table

Revision ID: aafde5a64ad5
Revises: ec4b33197c15
Create Date: 2026-07-31 21:16:24.415709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aafde5a64ad5'
down_revision: Union[str, Sequence[str], None] = 'ec4b33197c15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", 
                          referent_table="users", local_cols=['owner_id'],
                          remote_cols=['id'], ondelete= "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
