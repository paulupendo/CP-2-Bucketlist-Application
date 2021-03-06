#!/usr/bin/env python3
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.v1 import models
from app import app, databases


migrate = Migrate(app, databases)
manager = Manager(app)
manager.add_command('databases', MigrateCommand)


@manager.command
def init_db():
    os.system('createdb bucketlist_db')
    os.system('createdb test_db')
    print('Databases created')


@manager.command
def drop_db():
    os.system(
        'psql -c "DROP DATABASE IF EXISTS test_db"')
    os.system(
        'psql -c "DROP DATABASE IF EXISTS bucketlist_db"')
    print('Databases dropped')


if __name__ == '__main__':
    manager.run()
