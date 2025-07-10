from classes import PlantData
import json

API_TOKEN_ID = 'es8PtscRbKJ7'
API_TOKEN_SECRET = 'aacc3745-7123-4cb5-ac1a-703cf61ee82f'
SEARCH_URL = 'https://permapeople.org/api/search'
DETAILS_URL = 'https://permapeople.org/api/plants/'

def search_plants(plant_name, pages):
    plant = PlantData()
    plant_name = plant_name.lower()
    if not plant_name:
        return "Empty parameters passed!"

    plant.set_api_token_id(API_TOKEN_ID)
    plant.set_api_token_secret(API_TOKEN_SECRET)
    plant.set_plants_dict(plant_name, pages, SEARCH_URL)

    plant_ids = plant.get_plant_id()
    if not plant_ids:
        print("No plants found by that name!")
        return None

    print("\nSearch Results: ")
    for i, p in enumerate(plant.plants_dict['plants']):
        name = p.get('name')
        pid = p.get('id')
        print(f"{i + 1}: {name} (ID: {pid})")

    selection = Input("Enter plant number to view details: ")
    try:


    elif plant_name in plant.get_plant_id():
        plant.set_plant_data(DETAILS_URL, plant_name)
        plant.populate_plant_class(plant.plant_data)
        print(plant.common_name)
        return plant

    else:
        plant.set_plants_dict(plant_name, pages, SEARCH_URL)
        plant.set_plant_data(DETAILS_URL, plant.plant_id[0])
        plant.populate_plant_class(plant.plant_data)
        print(plant.common_name)
        return plant


def help_menu():
    print(
        """
        Welcome to PlantScraper, enter:
        --> help to view this menu
        --> exit to terminate program
        --> search to query permapeople database by plant name
        --> retrieve to view plant details    
        """)

def retrieve_plant(plant_name):
    if plant_name:
        plant = PlantData(plant_name)
        plant.set_api_token_id(API_TOKEN_ID)
        plant.set_api_token_secret(API_TOKEN_SECRET)


def main():
    help_menu()
    while True:
        command = input("PSC > ")
        if command == "help":
            help_menu()
        elif command == "search":
            plant_name = input("Plant Name?: ")
            pages = input("Pages?: ")
            print (search_plants(plant_name, pages))
        elif command == "retrieve":
            retrieve_plant(input("Plant Name / ID?: "))




if __name__ == "__main__":
    main()


