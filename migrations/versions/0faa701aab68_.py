"""empty message

Revision ID: 0faa701aab68
Revises: 56a3bd1612cd
Create Date: 2025-03-30 20:31:21.269388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0faa701aab68'
down_revision = '56a3bd1612cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_of_vacancy', sa.String(length=64), nullable=False),
    sa.Column('description_of_vacancy', sa.String(length=256), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('vacancy', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_vacancy_company_id'), ['company_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_vacancy_description_of_vacancy'), ['description_of_vacancy'], unique=False)
        batch_op.create_index(batch_op.f('ix_vacancy_title_of_vacancy'), ['title_of_vacancy'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vacancy', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_vacancy_title_of_vacancy'))
        batch_op.drop_index(batch_op.f('ix_vacancy_description_of_vacancy'))
        batch_op.drop_index(batch_op.f('ix_vacancy_company_id'))

    op.drop_table('vacancy')
    # ### end Alembic commands ###
