"""create_table_following

Revision ID: 367621ffac79
Revises: a42dd9333f63
Create Date: 2023-04-03 19:28:08.380157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367621ffac79'
down_revision = 'a42dd9333f63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'following',
        sa.Column('id', sa.String(length=255), primary_key=True, server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('id_follower', sa.String(length=255), sa.ForeignKey('follower.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
        sa.Column('id_user_to', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
    )


def downgrade() -> None:
    op.drop_table('following')
