# -*- coding: utf-8 -*-
# app/api/utils.py

from functools import wraps

from flask import request

from app.server import server

from app.models import UserRole, Dashboard, Pipeline
from app.models import BasicQueryPipeline, AdvancedQueryPipeline
from app.models import BasicOutput, AdvancedOutput

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

