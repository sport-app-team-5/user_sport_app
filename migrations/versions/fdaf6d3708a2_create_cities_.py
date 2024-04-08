"""Create City table

Revision ID: fdaf6d3708a2
Revises: 46f44135f3ea
Create Date: 2024-04-02 22:20:52.894838

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdaf6d3708a2'
down_revision: Union[str, None] = '2de1e5940f75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        'cities', sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('country_id', sa.Integer(), sa.ForeignKey('countries.id'), index=True),
        sa.Column('code', sa.String(5), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow, nullable=False),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    )    

def downgrade() -> None:
    op.drop_table('cities')
