from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String


class BaseModel(Model):
    """Base class for models"""
    id = Column(Integer, primary_key=True)

    def insert(self):
        """insert into database"""
        self.db.session.add(self)
        self.db.session.commit()

    def model_update(self, db):
        """update item in database"""
        db.session.commit()

    def model_delete(self, db):
        """delete item from database"""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find(cls, id=None):
        """Find item by id"""
        return cls.query.filter_by(id=id).one_or_none()
