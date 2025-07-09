import requests

class PlantData:
    """
    Data structure for holding plant data
    """
    def __init__(self, api_token=None, base_url=None, plants_list:dict=None, plant_data:dict=None,
                 plant_id:list=[], common_name=None, scientific_name=None, other_name=None, sunlight=None, sunlight_dur=None,
                 pruning=None, pruning_count=None, seeds=None, propogation=None, hardiness=None,
                 flowering_season=None, indoor=None, care=None, water_quality=None, water_period=None,
                 water_vol=None, water_depth=None, water_temp=None, water_ph=None):
        self.api_token = api_token
        self.base_url = base_url
        self.plants_list = plants_list
        self.plant_data = plant_data
        self.plant_id = plant_id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.other_name = other_name
        self.sunlight = sunlight
        self.sunlight_dur = sunlight_dur
        self.pruning = pruning
        self.pruning_count = pruning_count
        self.seeds = seeds
        self.propagation = propogation
        self.hardiness = hardiness
        self.flowering_season = flowering_season
        self.indoor = indoor
        self.care = care
        self.water_quality = water_quality
        self.water_period = water_period
        self.water_vol = water_vol
        self.water_depth = water_depth
        self.water_temp = water_temp
        self.water_ph = water_ph

    def set_api_token(self, api_token):
        if api_token is not None:
            self.api_token = api_token
        else: print("Input API token empty!")

    def _get_api_token(self):
        return self.api_token

    def set_base_url(self, base_url):
        if base_url is not None:
            self.base_url = base_url
        else: print("Input base URL empty!")

    def get_base_url(self):
        return self.base_url

    def set_plant_id(self, plant_id):
        if plant_id is not None:
            self.plant_id = plant_id
        else: print("Input plant ID empty!")

    def get_plant_id(self):
        return self.plant_id

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

    def set_other_name(self, other_name):
        if other_name is not None:
            self.other_name = other_name
        else: print("Input other name empty!")

    def get_other_name(self):
        return self.other_name

    def set_sunlight(self, sunlight):
        if sunlight is not None:
            self.sunlight = sunlight
        else: print("Input sunlight empty!")

    def get_sunlight(self):
        return self.sunlight

    def set_pruning(self, pruning):
        if pruning is not None:
            self.pruning = pruning
        else: print("Input pruning empty!")

    def get_pruning(self):
        return self.pruning

    def set_pruning_count(self, pruning_count):
        if pruning_count is not None:
            self.pruning_count = pruning_count
        else: print("Input pruning count empty!")

    def get_pruning_count(self):
        return self.pruning_count

    def set_seeds(self, seeds):
        if seeds is not None:
            self.seeds = seeds
        else: print("Input seeds empty!")

    def get_seeds(self):
        return self.seeds

    def set_propogation(self, propogation):
        if propogation is not None:
            self.propagation = propogation
        else: print("Input propogation empty!")

    def get_propogation(self):
        return self.propagation

    def set_hardiness(self, hardiness):
        if hardiness is not None:
            self.hardiness = hardiness
        else: print("Input hardiness empty!")

    def get_hardiness(self):
        return self.hardiness

    def set_flowering_season(self, flowering_season):
        if flowering_season is not None:
            self.flowering_season = flowering_season
        else: print("Input flowering season empty!")

    def get_flowering_season(self):
        return self.flowering_season

    def set_indoor(self, indoor):
        if indoor is not None:
            self.indoor = indoor
        else: print("Input indoor empty!")

    def get_indoor(self):
        return self.indoor

    def set_care(self, care):
        if care is not None:
            self.care = care
        else: print("Input care empty!")

    def get_care(self):
        return self.care

    def set_water_quality(self, water_quality):
        if water_quality is not None:
            self.water_quality = water_quality
        else: print("Input water quality empty!")

    def get_water_quality(self):
        return self.water_quality

    def set_water_period(self, water_period):
        if water_period is not None:
            self.water_period = water_period
        else: print("Input water period empty!")

    def get_water_period(self):
        return self.water_period

    def set_water_vol(self, water_vol):
        if water_vol is not None:
            self.water_vol = water_vol
        else: print("Input water vol empty!")

    def get_water_vol(self):
        return self.water_vol

    def set_water_temp(self, water_temp):
        if water_temp is not None:
            self.water_temp = water_temp
        else: print("Input water temp empty!")

    def get_water_temp(self):
        return self.water_temp

    def set_water_ph(self, water_ph):
        if water_ph is not None:
            self.water_ph = water_ph
        else: print("Input water ph empty!")

    def get_water_ph(self):
        return self.water_ph

    def set_plants_list(self, query, page=1, url=""):
        """
        Queries Perenual API for list of plants based on query parameter,
        sets self.plants_list to a dictionary of the returned data
        :param query:
        :param page:
        :param url:
        :return:
        """
        api_token = self._get_api_token()
        if api_token and query and url:
            params = {
                'key' : api_token,
                'q' : query,
                'page' : page
            }
            try:
                response = requests.get(url, params=params)
                data = response.json()

                if not hasattr(self, 'plants_list') or self.plants_list is None:
                    self.plants_list = {}

                if not hasattr(self, 'plant_id') or self.plant_id:
                    self.plant_id = []

                self.plants_list = data

                if 'data' in data:
                    self.plants_list['data'].extend(data['data'])

                    for plant in data['data']:
                        plant_id = plant.get('id')
                        if plant_id is not None and plant_id not in self.plant_id:
                            print("populating with plant id...")
                            self.plant_id.append(plant_id)
                        elif plant_id is None:
                            print("No plant id found!")
                        elif plant_id in self.plant_id:
                            print("plant id already exists skipping...")
                else:
                    print("No data returned!")

            except requests.Timeout as e:
                print(e)

        else:
            print("missing parameters for set_plants_list!")

    def get_plants_list(self):
        return self.plants_list

    def set_plant_data(self, url, plant_id):
        """
        Queries perenual API for plant details based on plant_id,
        sets self.plant_data to a dictionary of the returned data
        :param plant_id:
        :param url:
        :return:
        """
        api_token = self._get_api_token()
        if api_token and plant_id is not None:
            if not hasattr(self, 'plant_data') or self.plant_data is None:
                self.plant_data = {}

            params = {
                'key' : api_token,
                'id' : plant_id
            }
            try:
                response = requests.get(url, params=params)
                self.plant_data[plant_id]  = response.json() #stores plant data based on passed plant_id

            except requests.Timeout as e:
                print(e)

        elif api_token is None:
            print("api token empty!")

        elif self.plant_id is None:
            print("plant id empty!")

    def get_plant_data(self, plant_id):
        return self.plant_data[plant_id]

    def populate_plant_data(self, plant_data):


    def filter_data(self, plants_list, plant_filter):# TODO: sanitize and filter raw data based on query, return filtered list
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


