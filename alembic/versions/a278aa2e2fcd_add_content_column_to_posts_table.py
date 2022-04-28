"""add content column to posts table

Revision ID: a278aa2e2fcd
Revises: dddfc3acb856
Create Date: 2022-04-27 09:14:28.093435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a278aa2e2fcd'
down_revision = 'dddfc3acb856'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
