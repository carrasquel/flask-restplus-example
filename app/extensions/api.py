# encoding: utf-8
# app/extensions/api.py

from flask import Blueprint
from flask_restplus import Api, Namespace
from functools import wraps


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

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        app = server.get_app()
        dbo = app.user_dbo

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Key is missing.'}, 401

        if not dbo.verify_key(token):
            return {'message' : 'Invalid credentials!!!'}, 401

        return f(*args, **kwargs)

    return decorated
