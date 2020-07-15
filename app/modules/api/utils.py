# encoding: utf-8

from functools import wraps

from flask import request

from app.modules.auth import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Key is missing.'}, 401

        if not User.verify_key(token):
            return {'message' : 'Invalid credentials!!!'}, 401

        return f(*args, **kwargs)

    return decorated