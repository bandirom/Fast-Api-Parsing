"""init

Revision ID: c82289c9e4a9
Revises:
Create Date: 2020-06-05 16:50:33.491104

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c82289c9e4a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=350), nullable=True),
                    sa.Column('url', sa.String(), nullable=True),
                    sa.Column('context', sa.String(), nullable=True),
                    sa.Column('is_main', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_links_id'), 'links', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_links_id'), table_name='links')
    op.drop_table('links')
    # ### end Alembic commands ###
