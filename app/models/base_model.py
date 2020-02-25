from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String


class BaseModel(Model):
    """Base class for models"""
    id = Column(Integer, primary_key=True)

    def insert(self):
        """insert into database"""
        self.db.session.add(self)
        self.db.session.commit()

    def update(self):
        """update item in database"""
        self.db.session.commit()

    def delete(self):
        """delete item from database"""
        self.db.session.delete(self)
        self.db.session.commit()

    @classmethod
    def find(cls, id=None):
        """Find item by id"""
        return cls.query.filter_by(id=id).first()
