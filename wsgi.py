def get_app():
    
    from app import create_app

    return create_app()

app = get_app()