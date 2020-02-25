import os

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.models.base_model import BaseModel


load_dotenv()

database_path = os.getenv('DB_URL')

db = SQLAlchemy(model_class=BaseModel)


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    from app.views import actor
    app.register_blueprint(actor.bp)

    return app
