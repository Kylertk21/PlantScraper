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

    corsican_mint_name = corsican_mint.common_name
    corsican_mint_water = corsican_mint.water


