from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://plantuser:icedog@localhost/plantdb'
    db.init_app(app)

    from . import models
    from .routes import routes

    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app