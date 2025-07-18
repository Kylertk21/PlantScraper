
from app import db

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(10), unique=True, nullable=False)
    light_reading = db.Column(db.String(100))
    water_reading = db.Column(db.String(100))

    def to_dict(self):
        return {

        }
