from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db_path = os.path.join(BASE_DIR, 'data.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    db.init_app(app)

    from . import models
    from .routes import routes

    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app