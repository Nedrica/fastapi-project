"""add user table

Revision ID: 82989b54cddd
Revises: a278aa2e2fcd
Create Date: 2022-04-27 09:34:24.185314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82989b54cddd'
down_revision = 'a278aa2e2fcd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

    pass


def downgrade():
    op.drop_table('users')
    pass
