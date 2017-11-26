"""empty message

Revision ID: 521314e8ee51
Revises: 16b369ba889c
Create Date: 2017-11-26 11:37:17.759090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '521314e8ee51'
down_revision = '16b369ba889c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    op.drop_constraint('on_playlist_user_id_fkey', 'on_playlist', type_='foreignkey')
    op.create_foreign_key(None, 'on_playlist', 'songs', ['user_id'], ['id'])
    op.add_column('playlists', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('playlists', 'name')
    op.drop_constraint(None, 'on_playlist', type_='foreignkey')
    op.create_foreign_key('on_playlist_user_id_fkey', 'on_playlist', 'users', ['user_id'], ['id'])
    op.create_table('song',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genre', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('album_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], name='song_album_id_fkey'),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='song_artist_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='song_pkey'),
    sa.UniqueConstraint('title', name='song_title_key')
    )
    # ### end Alembic commands ###
