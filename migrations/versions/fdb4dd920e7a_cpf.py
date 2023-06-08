"""cpf

Revision ID: fdb4dd920e7a
Revises: 1238dab14c5f
Create Date: 2023-06-07 02:57:52.401930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdb4dd920e7a'
down_revision = '1238dab14c5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa', sa.Column('cpf', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'pessoa', ['cpf'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pessoa', type_='unique')
    op.drop_column('pessoa', 'cpf')
    # ### end Alembic commands ###