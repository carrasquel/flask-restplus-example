def get_app():
    
    from app import create_app
    
    app = create_app()

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

    return app

app = get_app()