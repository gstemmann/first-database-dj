"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    songs = db.relationship('PlaylistSong', backref='playlist')

    def __repr__(self):
        return f"<Playlist {self.id} {self.name} {self.description} >"

class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    playlists = db.relationship('PlaylistSong', backref='song')

    def __repr__(self):
        return f"<Song {self.id} {self.title} {self.artist} >"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer,
                       db.ForeignKey("songs.id"))
    playlist_id = db.Column(db.Integer,
                          db.ForeignKey("playlists.id"))

    def __repr__(self):
        return f"<PlaylistSong {self.id} {self.song_id} {self.playlist_id} >"
    
    

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
