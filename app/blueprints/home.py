# app/blueprints/home.py

from flask import render_template, session, current_app

home = Blueprint('home', __name__)

@home.route('/')
def homepage():

    """
    Render the homepage template on the / route
    """

    return render_template('index.html', title="Welcome")
