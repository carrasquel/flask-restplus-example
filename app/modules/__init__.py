# encoding: utf-8
# app/modules/__init__.py

def init_app(app):

    from .auth import init_app as init_auth
    from .events import init_app as init_events
    from .todos import init_app as init_todos

    init_auth(app)

    