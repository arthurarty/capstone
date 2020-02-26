import os
import unittest

from dotenv import load_dotenv

from app import create_app, db

load_dotenv()


class BaseTest(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.assistant_token = os.getenv('ASSISTANT_TOKEN', 'None')
        self.director_token = os.getenv('DIRECTOR_TOKEN', 'None')
        self.producer_token = os.getenv('PRODUCER_TOKEN', 'None')

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
