"""empty message

Revision ID: ad0a9a2bf745
Revises: 3f17d7c0672f
Create Date: 2022-04-15 23:38:38.073087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad0a9a2bf745'
down_revision = '3f17d7c0672f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schema_migrations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schema_migrations',
    sa.Column('version', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('version', name='schema_migrations_pkey')
    )
    # ### end Alembic commands ###