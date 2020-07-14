# run.py

import os

# local imports
from app import create_app

app = create_app()

if __name__ == "__main__":

    app.run_app()
