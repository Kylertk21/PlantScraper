from classes import PlantData
import json

API_TOKEN = 'sk-DVS3686c44646946011326'
BASE_URL = 'https://perenual.com/api/species-list'
DETAILS_URL = 'https://perenual.com/api/v2/species/details'


if __name__ == "__main__":
    jade_plant = PlantData()
    jade_plant.set_api_token(API_TOKEN)
    jade_plant.set_plants_list("jade plant", 1, BASE_URL)

    plants_list = json.dumps(jade_plant.get_plants_list(), indent=2)
    jade_plant_id = jade_plant.get_plant_id()

    jade_plant.set_plant_data(DETAILS_URL, jade_plant_id)
    jade_plant_data = jade_plant.get_plant_data(jade_plant_id)

    print(jade_plant_data)

