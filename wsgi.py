import os

def get_app():
    
    from app import create_app
    
    app = create_app()

    database_uri = value = os.getenv("DATABASE_URL", 'sqlite:///database.db')

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    return app

app = get_app()