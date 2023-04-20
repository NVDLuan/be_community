"""create_table_like

Revision ID: 7ab0cfdc2ff2
Revises: 089d99b52b62
Create Date: 2023-03-28 21:59:13.205517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab0cfdc2ff2'
down_revision = '089d99b52b62'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the like table
    """
    op.create_table(
        'like',
        sa.Column('id', sa.String(length=255), primary_key=True),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('id_post', sa.String(length=255), sa.ForeignKey('post.id'), nullable=False),
    )


def downgrade():
    """
    Drops the like table
    """
    op.drop_table('like')