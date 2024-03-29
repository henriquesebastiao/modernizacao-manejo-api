"""init

Revision ID: 05684a1d1ae5
Revises: 
Create Date: 2023-06-23 16:12:32.673693

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '05684a1d1ae5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('sisbov', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('breed_id', sa.Integer(), nullable=True),
    sa.Column('father_id', sa.Integer(), nullable=True),
    sa.Column('mother_id', sa.Integer(), nullable=True),
    sa.Column('origin_id', sa.Integer(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('buy_date', sa.Date(), nullable=True),
    sa.Column('sell_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal_weight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight_type_id', sa.Integer(), nullable=False),
    sa.Column('animal_id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('weight_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal_weight_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('breed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employment_position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('farm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('farmer_plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('batch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reg', sa.String(length=20), nullable=False),
    sa.Column('farm_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['farm_id'], ['farm.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=24), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('user_type_id', sa.Integer(), nullable=False),
    sa.Column('manager_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_type_id'], ['user_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('batch_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.Column('animal_id', sa.Integer(), nullable=False),
    sa.Column('entry_date', sa.DateTime(), nullable=False),
    sa.Column('departure_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animal.id'], ),
    sa.ForeignKeyConstraint(['batch_id'], ['batch.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('farmer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('farmer_plan_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['farmer_plan_id'], ['farmer_plan.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('farmer_id', sa.Integer(), nullable=False),
    sa.Column('farm_id', sa.Integer(), nullable=False),
    sa.Column('employment_position_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employment_position_id'], ['employment_position.id'], ),
    sa.ForeignKeyConstraint(['farm_id'], ['farm.id'], ),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmer.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employment')
    op.drop_table('farmer')
    op.drop_table('batch_log')
    op.drop_table('user')
    op.drop_table('batch')
    op.drop_table('user_type')
    op.drop_table('farmer_plan')
    op.drop_table('farm')
    op.drop_table('employment_position')
    op.drop_table('breed')
    op.drop_table('animal_weight_type')
    op.drop_table('animal_weight')
    op.drop_table('animal')
    # ### end Alembic commands ###
