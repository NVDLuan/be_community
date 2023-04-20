"""create_table_comment

Revision ID: 13223206b3cc
Revises: 364d80c8e809
Create Date: 2023-03-28 21:58:36.151615

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '13223206b3cc'
down_revision = '364d80c8e809'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the comment table
    """
    op.create_table(
        'comment',
        sa.Column('id', sa.String(length=255), primary_key=True, server_default=sa.text('uuid_generate_v4()'),
                  nullable=False),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                  ondelete='CASCADE', deferrable=True)),
        sa.Column('id_post', sa.String(length=255), sa.ForeignKey('post.id', onupdate='CASCADE',
                  ondelete='CASCADE', deferrable=True)),
        sa.Column('content', sa.String(length=500), nullable=False),
        sa.Column('image', sa.String(length=256), nullable=True),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
    )


def downgrade():
    """
    Drops the comment table
    """
    op.drop_table('comment')
