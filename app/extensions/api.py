# encoding: utf-8
# app/extensions/api.py

from flask import Blueprint
from flask_restplus import Api, Namespace


authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint, version='1.0', 
        title='Events and ToDos API',
        description='Back-End RESTful example application for Front-End Practice and Development', 
        doc='/docs',
        authorizations=authorizations
    )

def create_api(app):

    app.register_blueprint(blueprint)

    return api

def init_app(app):
    
    api = create_api(app)
