"""create_table_friend

Revision ID: a42dd9333f63
Revises: 21351b816f58
Create Date: 2023-03-28 22:00:24.823246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a42dd9333f63'
down_revision = '21351b816f58'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the friend table
    """
    op.create_table(
        'friend',
        sa.Column('id', sa.String(length=255), primary_key=True, server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('id_user_fr', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
        sa.Column('id_user_to', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
        sa.Column('time_add', sa.DateTime, nullable=False)
    )


def downgrade():
    """
    Drops the friend table
    """
    op.drop_table('friend')