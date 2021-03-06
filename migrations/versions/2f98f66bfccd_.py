"""empty message

Revision ID: 2f98f66bfccd
Revises: 31f5674f01ff
Create Date: 2022-03-12 15:40:06.542446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f98f66bfccd'
down_revision = '31f5674f01ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'user_id')
    # ### end Alembic commands ###
