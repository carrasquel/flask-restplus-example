# -*- coding: utf-8 -*-
# app/api/auth.py

from flask import request
from flask_restplus import Resource, fields
from playhouse.shortcuts import model_to_dict

from app.server import server
from app.models import User

from .utils import token_required

db = server.database

api = server.get_api()
app = server.get_app()
ns = server.get_namespace("auth")

login_model = api.model("login_model", {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})


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
