# app/__init__.py

# third-party imports
# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

from flask_restful import Api
from app.api import EventAPI, EventListAPI

# local imports
from config import app_config

# db variable initialization


def create_app(config_name):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.add_resource(EventListAPI, '/api/events/')
    api.add_resource(EventAPI, '/api/events/<int:id>')

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
