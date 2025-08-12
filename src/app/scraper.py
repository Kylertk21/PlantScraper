from .classes import *
from .models import PlantDataModel, SensorDataModel
from . import db
from flask import current_app

API_TOKEN_ID = 'es8PtscRbKJ7'
API_TOKEN_SECRET = 'aacc3745-7123-4cb5-ac1a-703cf61ee82f'
SEARCH_URL = 'https://permapeople.org/api/search'
DETAILS_URL = 'https://permapeople.org/api/plants/'

def search_plants(plant_name, pages):
    plant = PlantData()
    plant_name = plant_name.lower()

    if not plant_name:
        return []

    plant.set_api_token_id(API_TOKEN_ID)
    plant.set_api_token_secret(API_TOKEN_SECRET)
    plant.set_plants_dict(plant_name, pages, SEARCH_URL)
    plant_ids = plant.get_plant_id()
    plants = plant.plants_dict.get('plants', [])

    return [
        {
            "name": p.get("name"),
            "id": p.get("id")
        }
        for p in plants
    ]
    if not plant_ids:
        print("No plants found by that name!")
        return None
    return None


def help_menu():
    print(
        """
        Welcome to PlantScraper, enter:
        --> help to view this menu
        --> exit to terminate program
        --> search to query permapeople database by plant name
        --> retrieve to view plant details    
        """)

def retrieve_plant(plant_id):
    if plant_id:
        plant = PlantData()
        plant.set_api_token_id(API_TOKEN_ID)
        plant.set_api_token_secret(API_TOKEN_SECRET)
        plant.set_plant_data(DETAILS_URL, plant_id)
        data = plant.get_plant_data(plant_id)
        plant.populate_plant_class(data)

        plant_model = PlantDataModel(
            id=plant_id,
            name=plant.name,
            scientific_name=plant.scientific_name,
            family=plant.family,
            description=plant.description,
            link=plant.link,
            edible=plant.edible,
            edible_parts=plant.edible_parts,
            growth=plant.growth,
            water=plant.water,
            light=plant.light,
            hardiness=plant.hardiness,
            soil_type=plant.soil_type
        )

        existing = plant_model.query.get(plant_id)
        if not existing:
            db.session.add(plant_model)
            db.session.commit()


        return {
            "plant_id": plant_id,
            "name": plant.name,
            "scientific_name": plant.scientific_name,
            "family": plant.family,
            "description": plant.description,
            "link": plant.link,
            "edible_parts": plant.edible,
            "growth_rate": plant.growth,
            "water_requirements": plant.water,
            "light_requirements": plant.light,
            "hardiness_rating": plant.hardiness,
            "soil_type": plant.soil_type
        }

    else:
        return None

def parse_sensor_data(data):
    if data:
        sensor_readings = Sensor()
        sensor_readings.set_sensor_id(data['sensor_id'])
        sensor_readings.sunlight = (data['readings']['sunlight'])
        sensor_readings.water = (data['readings']['water'])

        sensor_model = SensorDataModel(
            sensor_id = sensor_readings.get_sensor_id(),
            light_reading = sensor_readings.sunlight(),
            water_reading = sensor_readings.water()
        )

        with current_app.app_context():
            db.session.add(sensor_model)
            db.session.commit()

        return {
            "sensor_id": sensor_readings.sensor_id,
            "time" : sensor_readings.time,
            "water": sensor_readings.water,
            "sunlight": sensor_readings.sunlight
        }
    else:
        return None

def main():

    help_menu()
    while True:
        command = input("PSC > ")
        if command == "help":
            help_menu()
        elif command == "search":
            plant_name = input("Plant Name?: ")
            pages = input("Pages?: ")
            search_plants(plant_name, pages)
        elif command == "retrieve":
            plant_id = input("Plant ID?: ")
            retrieve_plant(plant_id)

if __name__ == "__main__":
    main()































