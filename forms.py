"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist name", validators=[
                       InputRequired(message="Name cannot be blank")])
    description = StringField("Playlist description", validators=[
                       InputRequired(message="Name cannot be blank")])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song title", validators=[
                       InputRequired(message="Name cannot be blank")])
    artist = StringField("Artist", validators=[
                       InputRequired(message="Name cannot be blank")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
