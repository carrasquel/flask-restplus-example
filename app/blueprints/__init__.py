# app/home/__init__.py

from flask import Blueprint

def init_app(app):

    from .home import home_blueprint
    
    app.register_blueprint(home_blueprint)