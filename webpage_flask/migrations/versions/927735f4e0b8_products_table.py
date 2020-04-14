"""products table

Revision ID: 927735f4e0b8
Revises: 8944053df8c3
Create Date: 2019-04-14 03:10:49.227412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927735f4e0b8'
down_revision = '8944053df8c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_product_timestamp'), 'product', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_timestamp'), table_name='product')
    op.drop_column('product', 'timestamp')
    # ### end Alembic commands ###
