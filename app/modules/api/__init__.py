# app/api/__init__.py
from flask import Blueprint
from flask_restplus import Api, Namespace


authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

def create_api(app):

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api = Api(blueprint, version='1.0', 
            title='Events and ToDos API',
            description='Back-End RESTful example application for Front-End Practice and Development', 
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

def init_app(app):
    
    # initializations
    api = create_api(app)
    app.set_api(api)

    # local imports
    from .auth import AuthLoginResource, AuthLogoutResource