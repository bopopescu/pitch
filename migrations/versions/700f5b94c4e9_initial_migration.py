"""Initial Migration

Revision ID: 700f5b94c4e9
Revises: 1c77bf9ffe93
Create Date: 2019-03-01 13:24:47.149111

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '700f5b94c4e9'
down_revision = '1c77bf9ffe93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitch_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_of_category', sa.String(length=255), nullable=True),
    sa.Column('category_description', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitches')
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('username', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('votes', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitch_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitch', ['pitch_id'], ['id'])
    op.drop_column('comments', 'pitch')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'pass_secure')
    op.add_column('comments', sa.Column('pitch', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_fkey', 'comments', 'pitches', ['pitch'], ['id'])
    op.drop_column('comments', 'votes')
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'pitch_id')
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pitch_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pitch_content', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitches_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey')
    )
    op.drop_table('vote')
    op.drop_table('pitch_categories')
    op.drop_table('pitch')
    # ### end Alembic commands ###
