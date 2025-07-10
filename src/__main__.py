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

    selection = input("Enter plant number to view details: ")
    try:
        index = int(selection) - 1
        index_id = plant.get_plant_id(index)
        retrieve_plant(index_id)

    except (IndexError, ValueError):
        print("Invalid selection!")
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

        print(f"Plant ID: {plant_id}")
        print(f"Common Name: {plant.common_name}")
        print(f"Scientific Name: {plant.scientific_name}")
        print(f"Family: {plant.family}")
        print(f"Description: {plant.description}")
        print(f"Link: {plant.link}")
        print(f"Edible Parts: {plant.edible}")
        print(f"Growth Rate: {plant.growth}")
        print(f"Water Requirements: {plant.water}")
        print(f"Light Requirements: {plant.light}")
        print(f"Hardiness Rating: {plant.hardiness}")
        print(f"Soil Type: {plant.soil_type}")

    else:
        print("No plant_id supplied!")

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































