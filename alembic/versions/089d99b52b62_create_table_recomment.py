"""create_table_recomment

Revision ID: 089d99b52b62
Revises: 13223206b3cc
Create Date: 2023-03-28 21:59:03.904494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '089d99b52b62'
down_revision = '13223206b3cc'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the recomment table
    """
    op.create_table(
        'recomment',
        sa.Column('id', sa.String(length=255), primary_key=True),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('id_cmt', sa.String(length=255), sa.ForeignKey('comment.id'), nullable=False),
        sa.Column('content', sa.String(length=500), nullable=False),
        sa.Column('image', sa.String(length=256), nullable=True),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
    )


def downgrade():
    """
    Drops the recomment table
    """
    op.drop_table('recomment')
