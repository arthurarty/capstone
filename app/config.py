import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    """Parent configuration class."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for development"""
    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    """Configurations for testing"""
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
