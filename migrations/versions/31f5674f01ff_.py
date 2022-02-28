"""empty message

Revision ID: 31f5674f01ff
Revises: 15f201c4b96d
Create Date: 2022-02-28 19:30:35.078361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31f5674f01ff'
down_revision = '15f201c4b96d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('startDate', sa.DateTime(), nullable=False))
    op.add_column('events', sa.Column('endDate', sa.DateTime(), nullable=False))
    op.add_column('events', sa.Column('name', sa.String(), nullable=False))
    op.add_column('events', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'description')
    op.drop_column('events', 'name')
    op.drop_column('events', 'endDate')
    op.drop_column('events', 'startDate')
    # ### end Alembic commands ###