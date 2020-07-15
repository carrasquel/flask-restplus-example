# encoding: utf-8
# app/extensions/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app(app):
    """
    Application extensions initialization.
    """

    from . import api

    extensions = (db, api, login_manager,)

    for extension in extensions:
        extension.init_app(app)
    