# encoding: utf-8

from app.extensions.api import api

from .models import User

def init_app(app):

    from .resources import ns

    api.add_namespace(ns, path="/auth")
