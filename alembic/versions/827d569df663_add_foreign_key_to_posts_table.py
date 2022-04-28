"""add foreign-key to posts table

Revision ID: 827d569df663
Revises: 82989b54cddd
Create Date: 2022-04-27 10:47:35.491902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '827d569df663'
down_revision = '82989b54cddd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id')
    pass
