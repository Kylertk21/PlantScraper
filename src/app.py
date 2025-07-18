from flask import Flask, render_template, request, jsonify
from scraper import *
import json

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

sensor_store = {}
app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():

    return render_template("index.html", sensors=sensor_test)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("plant")
    pages = request.args.get("pages")
    results = search_plants(query, 1) if query else []

    return render_template("results.html", plants=results, query=query, pages=pages)

@app.route("/plant/<plant_id>")
def plant_details(plant_id):
    data = retrieve_plant(plant_id)
    return render_template("details.html", plant=data)

@app.route("/api/sensor", methods=["POST"])
def receive_sensor_data():
    print("Post request received")
    if request.is_json:
        received_data = request.get_json()
        parsed = parse_sensor_data(received_data)
        print(parsed)
        sensor_id = str(parsed["sensor_id"])
        sensor_store[sensor_id] = parsed
        return jsonify({"status": "success", "data": parsed}), 200
    else:
        return jsonify({"status": "error", "message": "Incorrect data type!"}), 400

@app.route("/sensor/<sensor_id>", methods=["GET"])
def render_sensor_data(sensor_id):
    sensor = sensor_test.get(sensor_id)
    return render_template("sensors.html", sensor=sensor)




