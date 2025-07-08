from classes import PlantData

API_TOKEN = 'sk-DVS3686c44646946011326'
BASE_URL = 'https://perenual.com/api/species-list'


if __name__ == "__main__":
    jade_plant = PlantData()
    jade_plant.set_api_token(API_TOKEN)
    jade_plant.grab_data("jade plant", API_TOKEN, BASE_URL)
    print (jade_plant.get_raw_data())

