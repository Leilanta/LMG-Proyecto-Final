"""empty message

Revision ID: 13805cd024e6
Revises: 719e42d8f477
Create Date: 2024-01-30 21:58:15.372022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13805cd024e6'
down_revision = '719e42d8f477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre_ong_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('campaign_ong_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ongs', ['nombre_ong_id'], ['id'])
        batch_op.drop_column('ong_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ong_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('campaign_ong_id_fkey', 'ongs', ['ong_id'], ['id'])
        batch_op.drop_column('nombre_ong_id')

    # ### end Alembic commands ###
