"""add foreign key to Review

Revision ID: ad46faa003ac
Revises: e7aa8d4fc78b
Create Date: 2024-10-04 09:51:35.080491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad46faa003ac'
down_revision = 'e7aa8d4fc78b'
branch_labels = None
depends_on = None


def upgrade():
    # Using batch mode for SQLite
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            op.f('fk_reviews_employee_id_employees'), 
            'employees', 
            ['employee_id'], 
            ['id']
        )


def downgrade():
    # Using batch mode for SQLite
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint(op.f('fk_reviews_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
