# app/home/views.py

from flask import render_template, session, current_app

from . import home


@home.route('/')
def homepage():

    """
    Render the homepage template on the / route
    """

    return render_template('index.html', title="Welcome")
