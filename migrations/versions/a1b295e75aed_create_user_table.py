"""Create user table

Revision ID: a1b295e75aed
Revises: 
Create Date: 2024-02-28 08:20:18.876096

"""
from datetime import datetime
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46f44135f3ea'
down_revision: Union[str, None] = 'fdaf6d3708a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users', sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'), index=True),
        sa.Column('city_id', sa.Integer(), sa.ForeignKey('cities.id'), index=True),
        sa.Column('document_type', sa.String(20), nullable=False),
        sa.Column('document_number', sa.String(20), unique=True, nullable=False),
        sa.Column('email', sa.String(256), unique=True, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('lastname', sa.String(50), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(256), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow, nullable=False),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
