"""added to allowed password length

Revision ID: 793d321f97af
Revises: 31d5c68957ca
Create Date: 2023-03-08 13:54:34.975152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '793d321f97af'
down_revision = '31d5c68957ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password', type_=sa.String(100)) 
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
