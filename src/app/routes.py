from flask import Blueprint, render_template, request, jsonify, current_app
from .scraper import *
from .models import PlantDataModel, SensorDataModel
from datetime import datetime

routes = Blueprint('routes', __name__)

sensor_test = {
    "1": {
        "sensor_id": "Mint",
        "readings": {
            "light_reading": "Full sun, partial sun/shade",
            "water_reading": "Moist"
        }
    },
    "2": {
        "sensor_id": "Juniper",
        "readings": {
            "light_reading": "partial sun/shade",
            "water_reading": "dry"
        }
    }
}

@routes.route("/", methods=["GET"])
def index():
    return render_template("index.html", sensors=sensor_test)

@routes.route("/search", methods=["GET"])
def search():
    query = request.args.get("plant")
    pages = request.args.get("pages")
    results = search_plants(query, 1) if query else []

    return render_template("results.html", plants=results, query=query, pages=pages)

@routes.route("/plant/<plant_id>")
def plant_details(plant_id):
    data = PlantDataModel.query.filter_by(id=plant_id).first()
    if data is None:
        with current_app.app_context():
            data = retrieve_plant(plant_id)

        plant_dict = {column.name: getattr(data, column.name) for column in data.__table__.columns}

    return render_template("details.html", plant=plant_dict)

@routes.route("/api/sensor", methods=["POST"])
def receive_sensor_data():
    if request.is_json:
        received_data = request.get_json()

        if not received_data or 'sensor_id' not in received_data or 'readings' not in received_data:
            return jsonify({"error": "Invalid Data"}), 400

        current_time = datetime.now()
        parsed = parse_sensor_data(received_data)
        sensor_id = str(parsed["sensor_id"])

        new_entry = SensorDataModel(
            sensor_id=sensor_id,
            sunlight=["sunlight"],
            water=parsed["water"],
            time=current_time
        )

        db.session.add(new_entry)
        db.session.commit()

        records = SensorDataModel.query.filter_by(sensor_id=sensor_id).order_by(SensorDataModel.time.desc()).all()

        if len(records) > 10:
            delete = records[10:] #delete records older than the 10 newest
            for old_record in delete:
                db.session.delete(old_record)
            db.session.commit()

        return jsonify({
            "message": "Sensor data saved",
            "timestamp": current_time.isoformat()
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Incorrect data type!"
        }), 400

@routes.route("/api/sensor/<sensor_id>", methods=["GET"])
def get_sensor_data(sensor_id):
    sensors = SensorDataModel.query.filter_by(sensor_id=sensor_id).order_by(SensorDataModel.time.desc()).all()

    if not sensors:
        return jsonify({
            "error": "Sensor data not found"
        }), 404

    return jsonify(
        {
        "sensor_id": sensor.sensor_id,
        "water": sensor.water,
        "sunlight": sensor.sunlight,
        "time": sensor.time
    }
        for sensor in sensors
    )

@routes.route("/sensor/<sensor_id>", methods=["GET"])
def render_sensor_data(sensor_id):
    latest = (
        SensorDataModel.query
        .filter_by(sensor_id=sensor_id)
        .order_by(SensorDataModel.time.desc())
        .first()
    )

    if not latest:
        return render_template("sensors.html", sensor=None, sensor_id=sensor_id)

    return render_template("sensors.html", sensor=latest)




