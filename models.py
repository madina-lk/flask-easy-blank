
from setup_db import db
from marshmallow import Schema, fields


class DirectorModel(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreModel(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class MovieModel(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("GenreModel")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("DirectorModel")

    def __init__(
        self,
        id,
        title,
        description,
        trailer,
        year,
        rating,
        genre_id,
        genre,
        director_id,
        director,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.trailer = trailer
        self.year = year
        self.rating = rating
        self.genre_id = genre_id
        self.genre = genre
        self.director_id = director_id
        self.director = director


class MovieSchema(Schema):

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director_id = fields.Int()
    director = fields.Nested(DirectorSchema)