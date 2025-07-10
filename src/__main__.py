from classes import PlantData
import json

API_TOKEN_ID = 'es8PtscRbKJ7'
API_TOKEN_SECRET = 'aacc3745-7123-4cb5-ac1a-703cf61ee82f'
SEARCH_URL = 'https://permapeople.org/api/search'
DETAILS_URL = 'https://permapeople.org/api/plants/'


if __name__ == "__main__":
    corsican_mint = PlantData()
    corsican_mint.set_api_token_id(API_TOKEN_ID)
    corsican_mint.set_api_token_secret(API_TOKEN_SECRET)
    corsican_mint.set_plants_dict("corsican_mint", 1, SEARCH_URL)

    plants_list = corsican_mint.get_plants_dict()
    corsican_mint_id = corsican_mint.get_plant_id(0)
    print(corsican_mint_id)

    corsican_mint.set_plant_data(DETAILS_URL, corsican_mint_id)

    corsican_mint_data = corsican_mint.get_plant_data(corsican_mint_id)
    corsican_mint.populate_plant_class(corsican_mint_data)

    print(f"name: {corsican_mint.common_name}")
    print(f"edible parts: {corsican_mint.edible}")
    print(f"growth: {corsican_mint.growth}")
    print(f"water requirement: {corsican_mint.water}")
    print(f"light requirement: {corsican_mint.light}")
    print(f"soil type: {corsican_mint.soil_type}")
    print(f"family: {corsican_mint.family}")
    print(f"hardiness: {corsican_mint.hardiness}")
    print(f"layer: {corsican_mint.layer}")



