"""create table user

Revision ID: 951d01b7000d
Revises: 
Create Date: 2023-03-23 09:13:27.831484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '843850c0ed0c'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    """
    Creates the user table
    """
    op.create_table(
        'user',
        sa.Column('id', sa.String(length=255), primary_key=True),
        sa.Column('fullname', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=120), unique=True, nullable=False),
        sa.Column('address', sa.String(length=120), nullable=True),
        sa.Column('password', sa.String(length=256), nullable=False),
        sa.Column('sex', sa.String(length=10), nullable=True),
        sa.Column('avatar', sa.String(length=256), nullable=True),
        sa.Column('birthday', sa.Date(), nullable=True),
        sa.Column('lasted_login', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
        sa.Column('is_super', sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column('description', sa.String(length=256), nullable=True),
        sa.Column('image_cover', sa.String(length=256), nullable=True),
        sa.Column('is_activate', sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )


def downgrade():
    """
    Drops the user table
    """
    op.drop_table('user')

def downgrade():
    op.drop_table("user")
