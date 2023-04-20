"""create table post

Revision ID: 364d80c8e809
Revises: 843850c0ed0c
Create Date: 2023-03-23 09:26:21.013555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364d80c8e809'
down_revision = '843850c0ed0c'
branch_labels = None
depends_on = None

def upgrade():
    """
    Creates the post table
    """
    op.create_table(
        'post',
        sa.Column('id', sa.String(length=255), primary_key=True),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('content', sa.String(length=5000), nullable=False),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
        sa.Column('image', sa.String(length=256), nullable=True),
        sa.Column('status', sa.String(length=20), nullable=True),
    )


def downgrade():
    """
    Drops the post table
    """
    op.drop_table('post')