"""empty message

Revision ID: 56a3bd1612cd
Revises: 
Create Date: 2025-03-30 20:30:56.510790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a3bd1612cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyname', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), server_default='c', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_company_companyname'), ['companyname'], unique=True)
        batch_op.create_index(batch_op.f('ix_company_email'), ['email'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=False),
    sa.Column('patronymic', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), server_default='u', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_patronymic'), ['patronymic'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_surname'), ['surname'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=False)

    op.create_table('curriculum_vitae',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=256), nullable=False),
    sa.Column('link', sa.String(length=64), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('curriculum_vitae', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_curriculum_vitae_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_curriculum_vitae_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curriculum_vitae', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_curriculum_vitae_user_id'))
        batch_op.drop_index(batch_op.f('ix_curriculum_vitae_timestamp'))

    op.drop_table('curriculum_vitae')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_surname'))
        batch_op.drop_index(batch_op.f('ix_user_patronymic'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_company_email'))
        batch_op.drop_index(batch_op.f('ix_company_companyname'))

    op.drop_table('company')
    # ### end Alembic commands ###
