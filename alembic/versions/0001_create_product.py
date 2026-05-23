"""create product table

Revision ID: 0001_create_product
Revises: 
Create Date: 2026-05-23
"""
from alembic import op
import sqlalchemy as sa

revision = '0001_create_product'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('count', sa.Integer, nullable=False),
    )

def downgrade():
    op.drop_table('product')
