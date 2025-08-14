# Pytest fixtures for database testing #
import pytest
from . import create_app, db
from .models import SensorDataModel
from datetime import datetime

class TestDatabase:
    @pytest.fixture(scope="session")
    def app(self):
        app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        with app.app_context():
            db.create_all()
        yield app
        with app.app_context():
            db.drop_all()

    @pytest.fixture()
    def client(self, app):
        return app.test_client()

    def test_sensor_insert(self):
        with app.app_context():
            sensor = SensorDataModel(
                sensor_id="Mint",
                light_reading="Shade",
                water_reading="Dry",
                time=datetime.now()
            )
            db.session.add(sensor)
            db.session.commit()

            retrieved = SensorDataModel.query.filter_by(sensor_id="Mint").first()
            assert retrieved is not None
            assert retrieved.light_reading == "Shade"


