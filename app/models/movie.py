from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app import db
from app.models.cast import Cast


class Movie(db.Model):
    '''Movie model
    '''
    __tablename__ = 'movies'

    title = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    actors = db.relationship('Cast', backref='movie', lazy=True)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
        self.db = db

    @property
    def cast(self):
        """returns a list of all
        actors in the movie
        """
        actor_list = []
        for actor in self.actors:
            actor_dict = {
                "id": actor.actor_id,
                "name": actor.actor.name,
            }
            actor_list.append(actor_dict)
        return actor_list

    def format(self):
        """formats a movie obj
        into a dict which is json serializable
        """
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'cast': self.cast
        }

    def update(self):
        """updates a movie"""
        return self.model_update(db)
