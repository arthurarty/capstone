from sqlalchemy import Column, Integer, String, create_engine

from app import db
from app.models.cast import Cast


class Actor(db.Model):
    '''Actor model
    '''
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    movies = db.relationship('Cast', backref='actor', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.db = db

    def update(self):
        return self.model_update(db)

    def delete(self):
        return self.model_delete(db)

    @property
    def movies_in(self):
        movies_in = []
        for movie in self.movies:
            movie_dict = {
                "id": movie.movie_id,
                "title": movie.movie.title,
            }
            movies_in.append(movie_dict)
        return movies_in

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies_in': self.movies_in
        }
