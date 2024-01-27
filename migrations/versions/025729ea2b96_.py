"""empty message

Revision ID: 025729ea2b96
Revises: 
Create Date: 2024-01-21 15:34:01.184230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025729ea2b96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ongs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('ciudad', sa.String(length=80), nullable=False),
    sa.Column('nif', sa.String(length=80), nullable=False),
    sa.Column('actividad', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('aprobado', sa.Boolean(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('lat'),
    sa.UniqueConstraint('lng')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('voluntario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('ciudad', sa.String(length=80), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('lat'),
    sa.UniqueConstraint('lng')
    )
    op.create_table('campaign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=False),
    sa.Column('fecha_finalizacion', sa.Date(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('objetivo', sa.String(length=80), nullable=False),
    sa.Column('articulos', sa.String(length=80), nullable=False),
    sa.Column('ong_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ong_id'], ['ongs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign')
    op.drop_table('voluntario')
    op.drop_table('user')
    op.drop_table('ongs')
    # ### end Alembic commands ###
