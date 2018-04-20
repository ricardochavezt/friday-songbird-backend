# -*- coding: utf-8 -*-

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
# esta linea carga todos los modelos, así es como detectamos los cambios
# en la BD
from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

