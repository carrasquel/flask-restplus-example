# -*- coding: utf-8 -*-
# app/api/auth.py

from flask import request
from flask_restplus import Namespace, Resource, fields

from app.extensions.api import api
from app.modules.auth import User
from app.modules.api.utils import token_required

ns = Namespace('auth', description='Namespace for authentication')

login_model = api.model("login_model", {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})

signup_model = api.model("signup_model", {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
    'email': fields.String(required=True, description='Email')
})


@ns.route('/signup')
class AuthSignUpResource(Resource):

    @ns.expect(signup_model)
    def post(self):

        payload = api.payload

        username = payload["username"]
                
        if User.verify_username(username):
            return {"message": "User already exist"}, 401

        user = User.create(**payload)

        response = {
            "message": "User created"
        }

        return response


@ns.route('/login')
class AuthLoginResource(Resource):

    @ns.expect(login_model)
    def post(self):

        payload = api.payload

        username = payload["username"]
        password = payload["password"]
        
        if not User.verify_username(username):
            return {"message": "Invalid credentials"}, 401
        
        if not User.login(username, password):
            return {"message": "Invalid credentials"}, 401

        key = User.get_key(username)

        response = {
            "api_key": key
        }

        return response


@ns.route('/logout')
class AuthLogoutResource(Resource):
    
    @api.doc(security='apikey')
    @token_required
    def get(self):

        key = request.headers['X-API-KEY']

        User.delete_key(key)

        return {"message": "Logout succesfully"}
