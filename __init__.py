# run.py

import os

# local imports
def get_app():
    
    from app import create_app

    app = create_app()
    