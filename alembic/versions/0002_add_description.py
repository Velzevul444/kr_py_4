"""add description to product

Revision ID: 0002_add_description
Revises: 0001_create_product
Create Date: 2026-05-23
"""
from alembic import op
import sqlalchemy as sa

revision = '0002_add_description'
down_revision = '0001_create_product'
branch_labels = None
depends_on = None

def upgrade():
    # Add description with a server default so existing rows get a value
    op.add_column('product', sa.Column('description', sa.String(length=500), nullable=False, server_default=''))
    # remove server_default for cleanliness (some DBs support alter)
    try:
        op.alter_column('product', 'description', server_default=None)
    except Exception:
        pass

def downgrade():
    op.drop_column('product', 'description')
