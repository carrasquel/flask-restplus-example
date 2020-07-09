# -*- coding: utf-8 -*-
# app/server/instance.py

import os

from flask import Flask, Blueprint
from flask_restplus import Api, Namespace
from flask_sqlalchemy import SQLAlchemy

# configure our database
DATABASE = {
    'name': 'id.db'
}
SQLALCHEMY_DATABASE_URI = 'sqlite:///id.db'

DEBUG = True
PORT = 5000
SECRET_KEY = 'thisisnotsafe'

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}


class API(Api):

    def __init__(self, *args, **kwargs):

        super(API, self).__init__(*args, **kwargs)

    def get_namespace(self, name):

        namespaces = self.namespaces

        for namespace in namespaces:

            if namespace.name == name:
                
                return namespace

def create_api(app):

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api = API(blueprint, version='1.0', 
            title='MARIBEL API',
            description='Modelo Automatizado de Riesgos de Incidentes Basado en Estadísticas Legadas', 
            doc='/docs',
            authorizations=authorizations
        )

    app.register_blueprint(blueprint)

    ns_auth = Namespace('auth', description='Namespace for user authentication')
    api.add_namespace(ns_auth, path='/auth')

    ns_admin = Namespace('events', description='Namespace for events')
    api.add_namespace(ns_admin, path='/events')

    ns_forms = Namespace('todos', description='Namespace for to-dos')
    api.add_namespace(ns_forms, path='/todos')

    return api


class Server(object):
    
    def __init__(self):

        self.app = Flask(__name__)
        self.app.config.from_object(__name__)
        self.db = SQLAlchemy(self.app)

        # API
        
        self.api = create_api(self.app)

    def get_api(self):

        return self.api

    def get_app(self):

        return self.app

    def get_namespace(self, name):

        return self.api.get_namespace(name)

    def run(self):
        
        port = self.app.config["PORT"]
        self.app.run(port=port, host="0.0.0.0")

server = Server()
