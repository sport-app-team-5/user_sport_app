"""Create countries table

Revision ID: 2de1e5940f75
Revises: 46f44135f3ea
Create Date: 2024-04-02 12:24:01.307260

"""
from datetime import datetime
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2de1e5940f75'
down_revision: Union[str, None] = 'a1b295e75aed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'countries', sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('code', sa.String(5), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow, nullable=False),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('countries')
