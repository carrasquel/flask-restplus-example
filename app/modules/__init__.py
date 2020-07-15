# encoding: utf-8
# app/modules/__init__.py

def init_app(app):

    from .auth import init_app as init_auth

    init_auth(app)

    