from . import db
from datetime import datetime

class SensorDataModel(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(10), unique=True, nullable=False)
    light_reading = db.Column(db.String(100))
    water_reading = db.Column(db.String(100))
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)

class PlantDataModel(db.Model):
    __tablename__ = 'plant_data'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    scientific_name = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
    edible = db.Column(db.String)
    edible_parts = db.Column(db.String)
    growth = db.Column(db.String)
    water = db.Column(db.String)
    light = db.Column(db.String)
    hardiness = db.Column(db.String)
    layer = db.Column(db.String)
    soil_type = db.Column(db.String)
    family = db.Column(db.String)

    def __repr__(self):
        return f"<PlantData {self.name}>"