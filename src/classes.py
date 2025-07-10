import requests
from requests.utils import super_len


class PlantData:
    """
    Data structure for holding plant data
    """
    def __init__(self, api_token_id=None, api_token_secret=None, base_url=None, plants_dict:dict=None, plant_data:dict=None,
                 plant_id:list=[], common_name=None, scientific_name=None, description=None, link=None,
                 edible=None, growth=None, water=None, light=None, hardiness=None, layer=None, soil_type=None,
                 family=None):

        self.api_token_id = api_token_id
        self.api_token_secret = api_token_secret
        self.base_url = base_url
        self.plants_dict = plants_dict
        self.plant_data = plant_data
        self.plant_id = plant_id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.description = description
        self.link = link
        self.edible = edible
        self.growth = growth
        self.water = water
        self.light = light
        self.hardiness = hardiness
        self.layer = layer
        self.soil_type = soil_type
        self.family = family

    def set_api_token_id(self, api_token_id):
        if api_token_id is not None:
            self.api_token_id = api_token_id
        else: print("api_token_id is empty!")

    def _get_api_token_id(self):
        return self.api_token_id

    def set_api_token_secret(self, api_token_secret):
        if api_token_secret is not None:
            self.api_token_secret = api_token_secret
        else: print("Input API token empty!")

    def _get_api_token_secret(self):
        return self.api_token_secret

    def set_base_url(self, base_url):
        if base_url is not None:
            self.base_url = base_url
        else: print("Input base URL empty!")

    def get_base_url(self):
        return self.base_url

    def set_plant_id(self, plant_id):
        """
        Returns list of plant IDs, or empty list if not set
        :param plant_id:
        :return:
        """
        return getattr(self, 'plant_id', [])

    def get_plant_id(self, index=None):
        """
        Returns list of plant IDs, or single plant ID if index is passed
        :param index:
        :return:
        """
        if index is None:
            return self.plant_id
        else:
            return getattr(self, 'plant_id', [])[index]

    def set_common_name(self, common_name):
        if common_name is not None:
            self.common_name = common_name
        else: print("Input common name empty!")

    def get_common_name(self):
        return self.common_name

    def set_scientific_name(self, scientific_name):
        if scientific_name is not None:
            self.scientific_name = scientific_name
        else: print("Input scientific name empty!")

    def get_scientific_name(self):
        return self.scientific_name

    def set_description(self, description):
        if description is not None:
            self.description = description

    def get_description(self):
        return self.description

    def set_link(self, link):
        if link is not None:
            self.link = link

    def get_link(self):
        return self.link

    def set_edible(self, edible):
        if edible is not None:
            self.edible = edible

    def get_edible(self):
        return self.edible

    def set_growth(self, growth):
        if growth is not None:
            self.growth = growth

    def get_growth(self):
        return self.growth

    def set_water(self, water):
        if water is not None:
            self.water = water

    def get_water(self):
        return self.water

    def set_light(self, light):
        if light is not None:
            self.light = light

    def get_light(self):
        return self.light

    def set_hardiness(self, hardiness):
        if hardiness is not None:
            self.hardiness = hardiness

    def get_hardiness(self):
        return self.hardiness

    def set_layer(self, layer):
        if layer is not None:
            self.layer = layer

    def get_layer(self):
        return self.layer

    def set_soil_type(self, soil_type):
        if soil_type is not None:
            self.soil_type = soil_type

    def get_soil_type(self):
        return self.soil_type

    def set_family(self, family):
        if family is not None:
            self.family = family

    def get_family(self):
        return self.family

    def set_plants_dict(self, query, page=1, url=""):
        """
        Queries Permapeople API for list of plants based on query parameter,
        sets self.plants_dict to a dictionary of the returned data
        :param query:
        :param page:
        :param url:
        :return:
        """
        api_token_id = self._get_api_token_id()
        api_token_secret = self._get_api_token_secret()
        if api_token_id and api_token_secret and query and url:
            headers = {
                'x-permapeople-key-id' : api_token_id,
                'x-permapeople-key-secret' : api_token_secret,
            }
            query = {
                'q' : query
            }
            try:
                response = requests.post(url, headers=headers, json=query)
                response.raise_for_status()
                plants = response.json()

                if not hasattr(self, 'plants_dict') or self.plants_dict is None:
                    self.plants_dict = {'plants' : []}

                if not hasattr(self, 'plant_id') or self.plant_id:
                    self.plant_id = []

                for plant in plants['plants']:
                    if plant['id'] not in self.plant_id:
                        print('Adding plant to dict...')
                        self.plant_id.append(plant['id'])
                        self.plants_dict['plants'].append(plant)
                    else:
                        print('Plant already in list, skipping...')

            except requests.Timeout as e:
                print(e)

        else:
            print("missing parameters for set_plants_dict!")

    def get_plants_dict(self):
        return self.plants_dict

    def set_plant_data(self, base_url, plant_id):
        """
        Queries Permapeople API for plant details based on plant_id,
        sets self.plant_data to a dictionary of the returned data
        :param base_url:
        :param plant_id:
        :return:
        """
        api_token_id = self._get_api_token_id()
        api_token_secret = self._get_api_token_secret()
        if api_token_id and api_token_secret and plant_id:
            if not hasattr(self, 'plant_data') or self.plant_data is None:
                self.plant_data = {}

            headers = {
                'x-permapeople-key-id' : api_token_id,
                'x-permapeople-key-secret' : api_token_secret
            }

            query = {
                'q' : plant_id
            }
            url = f"{base_url}/{plant_id}"

            try:
                response = requests.get(url, headers=headers, json=query)
                self.plant_data[plant_id]  = response.json() #stores plant data based on passed plant_id
                print(self.plant_data)


            except requests.Timeout as e:
                print(e)

        elif api_token_secret is None:
            print("api token empty!")

        elif self.plant_id is None:
            print("plant id empty!")

    def get_plant_data(self, plant_id):
        return self.plant_data.get(plant_id, {})

    def populate_plant_class(self, plant_data):
        """
        Populates PlantData parameters with those returned from the API
        :param plant_data:
        :return:
        """
        if not isinstance(plant_data, dict):
            print("Invalid plant_data format!")
            return

        if plant_data is not None:
            self.set_common_name(plant_data.get('name'))
            self.set_scientific_name(plant_data.get('scientific_name'))
            self.set_description(plant_data.get('description'))
            self.set_link(plant_data.get('link'))

            data_list = plant_data.get('data', []) # list of data dicts
            data_dict = {item['key']: item['value'] for item in data_list} # cleans key : value pair

            self.set_edible(data_dict.get('Edible parts'))
            self.set_growth(data_dict.get('Growth'))
            self.set_water(data_dict.get('Water requirement'))
            self.set_light(data_dict.get('Light requirement'))
            self.set_soil_type(data_dict.get('Soil type'))
            self.set_family(data_dict.get('Family'))
            self.set_hardiness(data_dict.get('USDA Hardiness zone'))
            self.set_layer(data_dict.get('Layer'))




    def filter_data(self, plants_dict, plant_filter):# TODO: sanitize and filter raw data based on query, return filtered list
        return None


class Sensor():
    def __init__(self, sensor_id, sunlight, time, water, humidity, ph):
        self.sensor_id = sensor_id
        self.sunlight = sunlight
        self.time = time
        self.water = water
        self.humidity = humidity
        self.ph = ph

    def set_sensor_id(self, sensor_id):
        if sensor_id is not None:
            self.sensor_id = sensor_id

    def get_sensor_id(self):
        return self.sensor_id

    def set_sunlight(self, sunlight):
        if sunlight is not None:
            self.sunlight = sunlight

    def get_sunlight(self):
        return self.sunlight

    def set_time(self, time):
        if time is not None:
            self.time = time

    def get_time(self):
        return self.time

    def set_water(self, water):
        if water is not None:
            self.water = water

    def get_water(self):
        return self.water

    def set_humidity(self, humidity):
        if humidity is not None:
            self.humidity = humidity

    def get_humidity(self):
        return self.humidity

    def set_ph(self, ph):
        if ph is not None:
            self.ph = ph

    def get_ph(self):
        return self.ph

    def read_sensors(self):# TODO: read sensors and return raw output
        return None


