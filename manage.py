import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.extensions import db
from app import create_app

app = create_app()


# app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()