"""create_table_follow

Revision ID: 21351b816f58
Revises: 7ab0cfdc2ff2
Create Date: 2023-03-28 21:59:35.947736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21351b816f58'
down_revision = '7ab0cfdc2ff2'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the follow table
    """
    op.create_table(
        'follower',
        sa.Column('id', sa.String(length=255), primary_key=True),
        sa.Column('id_user_fr', sa.String(length=255), sa.ForeignKey('user.id'), nullable=False),
    )


def downgrade():
    """
    Drops the follow table
    """
    op.drop_table('follow')