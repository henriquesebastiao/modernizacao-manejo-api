"""renomeado campos mae e pai Animal

Revision ID: a0c243e6daae
Revises: fbfd732f9aff
Create Date: 2023-06-07 11:47:31.575372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0c243e6daae'
down_revision = 'fbfd732f9aff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animal', sa.Column('mae_id', sa.Integer(), nullable=True))
    op.add_column('animal', sa.Column('pai_id', sa.Integer(), nullable=True))
    op.drop_column('animal', 'id_pai')
    op.drop_column('animal', 'id_mae')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animal', sa.Column('id_mae', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('animal', sa.Column('id_pai', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('animal', 'pai_id')
    op.drop_column('animal', 'mae_id')
    # ### end Alembic commands ###
