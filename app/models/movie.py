from sqlalchemy import Column, Integer, String, DateTime

from app import db


class Movie(db.Model):
    '''Movie model
    '''
    __tablename__ = 'movies'

    title = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
        self.db = db

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }
