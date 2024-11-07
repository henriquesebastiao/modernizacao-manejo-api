"""adjusting optional fill columns when registering an animal

Revision ID: 436c61f7e398
Revises: a86e37fb3f31
Create Date: 2024-11-06 13:58:41.890826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '436c61f7e398'
down_revision: Union[str, None] = 'a86e37fb3f31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('animal', 'sisbov',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('animal', 'breed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('animal', 'father_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('animal', 'mother_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('animal', 'birth_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('animal', 'buy_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('animal', 'sell_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('animal', 'sell_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('animal', 'buy_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('animal', 'birth_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('animal', 'mother_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('animal', 'father_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('animal', 'breed_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('animal', 'sisbov',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
