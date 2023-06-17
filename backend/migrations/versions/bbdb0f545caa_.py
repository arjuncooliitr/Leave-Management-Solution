"""empty message

Revision ID: bbdb0f545caa
Revises: 45cf5ad0f2f0
Create Date: 2023-06-15 16:49:55.501447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbdb0f545caa'
down_revision = '45cf5ad0f2f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leaves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('leave_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leaves', schema=None) as batch_op:
        batch_op.drop_column('leave_count')

    # ### end Alembic commands ###