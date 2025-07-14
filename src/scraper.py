from classes import *
import json
from flask import Flask

API_TOKEN_ID = 'es8PtscRbKJ7'
API_TOKEN_SECRET = 'aacc3745-7123-4cb5-ac1a-703cf61ee82f'
SEARCH_URL = 'https://permapeople.org/api/search'
DETAILS_URL = 'https://permapeople.org/api/plants/'

app = Flask("Plant Scraper Hub")



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
    """
    print("\nSearch Results: ")
    for i, p in enumerate(plant.plants_dict['plants']):
        name = p.get('name')
        pid = p.get('id')
        print(f"{i + 1}: {name} (ID: {pid})")

    selection = input("Enter plant number to view details: ")
    try:
        index = int(selection) - 1
        index_id = plant.get_plant_id(index)
        retrieve_plant(index_id)

    except (IndexError, ValueError):
        print("Invalid selection!")
        return None
    """

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

        return {
            "Plant ID": plant_id,
            "Common Name": plant.common_name,
            "Scientific Name": plant.scientific_name,
            "Family": plant.family,
            "Description": plant.description,
            "Link": plant.link,
            "Edible Parts": plant.edible,
            "Growth Rate": plant.growth,
            "Water Requirements": plant.water,
            "Light Requirements": plant.light,
            "Hardiness Rating": plant.hardiness,
            "Soil Type": plant.soil_type
        }

    else:
        return None

def parse_sensor_data(data):
    if data:
        sensor_readings = Sensor()
        sensor_readings.set_sensor_id(data['sensor_id'])
        sensor_readings.set_sunlight(data['readings']['sunlight'])
        #sensor_readings.set_time(data['readings']['time'])
        sensor_readings.set_water(data['readings']['water'])

        #TODO: assign relative values to readings (sensor side or server side)

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































