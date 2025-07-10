from flask import Flask, render_template, request
from src.scraper import *
import __main__
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("plant")
    results = []

    if query:
        results = search_plants(query, 1)

    return render_template("results.html, plants=results, query=query")

@app.route("/plant/<plant_id>")
def plant_details(plant_id):
    data = retrieve_plant(plant_id)
    return render_template("details.html", plant=data)