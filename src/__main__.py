from classes import PlantData
import json

API_TOKEN = 'sk-DVS3686c44646946011326'
BASE_URL = 'https://perenual.com/api/species-list'


if __name__ == "__main__":
    jade_plant = PlantData()
    jade_plant.set_api_token(API_TOKEN)
    jade_plant.get_plant_list("jade plant", API_TOKEN, BASE_URL)

    raw_data = json.dumps(jade_plant.get_raw_data(), indent=2)
    print(jade_plant.get_plant_id())

