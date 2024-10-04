"""add foreign key to Onboardig

Revision ID: d356c26b0dab
Revises: ad46faa003ac
Create Date: 2024-10-04 10:09:32.491670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd356c26b0dab'
down_revision = 'ad46faa003ac'
branch_labels = None
depends_on = None


def upgrade():
    # Using batch mode for SQLite
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            op.f('fk_onboardings_employee_id_employees'), 
            'employees', 
            ['employee_id'], 
            ['id']
        )


def downgrade():
    # Using batch mode for SQLite
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
