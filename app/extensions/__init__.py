# encoding: utf-8
# app/extensions/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

from . import api


def init_app(app):
    """
    Application extensions initialization.
    """
    extensions = (db, api, login_manager,)

    for extension in extensions:
        extension.init_app(app)
    