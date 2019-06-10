from datetime import datetime

from app import db

class PostCancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Unicode(255), nullable=False)
    artista = db.Column(db.Unicode(255))
    album = db.Column(db.Unicode(255))
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.today)
    fecha_publicacion = db.Column(db.Date, nullable=False)
    texto = db.Column(db.Text(convert_unicode=True))
    spotify_uri = db.Column(db.Unicode(50))
    youtube_url = db.Column(db.Unicode(255))

    def serialize(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'artista': self.artista,
            'album': self.album,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'fecha_publicacion': self.fecha_publicacion.isoformat(),
            'texto': self.texto,
            'spotify_uri': self.spotify_uri,
            'youtube_url': self.youtube_url
        }

    def serialize_short(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'artista': self.artista,
            'album': self.album
        }

