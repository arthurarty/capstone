from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app import db


class Cast(db.Model):
    """Cast model keeps track of
    the cast per movie"""

    __tablename__ = 'cast'
    __table_args__ = (
        db.UniqueConstraint(
            'actor_id', 'movie_id', name='unique_cast'),)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)
