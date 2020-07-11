# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import api
from app import blueprints

db = SQLAlchemy()

# local imports
from config import app_config

# configure our database
DATABASE = {
    'name': 'id.db'
}
SQLALCHEMY_DATABASE_URI = 'sqlite:///id.db'

DEBUG = True
PORT = 5000
SECRET_KEY = 'thisisnotsafe'


class Server(Flask):
    
    def __init__(self, name):

        super(Server, self).__init__(name)

        self.app = Flask(__name__)
        self.config.from_object(__name__)
        self.db = SQLAlchemy(self)

    def set_api(self, api):

        self.api = api

    def get_api(self):

        return self.api

    def get_namespace(self, name):

        namespaces = self.api.namespaces

        for namespace in namespaces:

            if namespace.name == name:
                
                return namespace

    def run(self):
        
        port = self.config["PORT"]
        self.run(port=port, host="0.0.0.0")

def create_app(config_name):

    app = Server(__name__)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    api.init_app(app)
    blueprints.init_app(app)

    return app
