class PlantData():
    def __init__(self, id, common_name, scientific_name, other_name, sunlight, sunlight_dur,
                 pruning, pruning_count, seeds, propogation, hardiness, flowering_season, indoor,
                 care, water_quality, water_period, water_vol, water_depth, water_temp, water_ph):
        self.id = id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.other_name = other_name
        self.sunlight = sunlight
        self.sunlight_dur = sunlight_dur
        self.pruning = pruning
        self.pruning_count = pruning_count
        self.seeds = seeds
        self.propogation = propogation
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

    def set_id(self, id):
        if id is not None:
            self.id = id

    def get_id(self):
        return self.id

    def set_common_name(self, common_name):
        if common_name is not None:
            self.common_name = common_name

    def get_common_name(self):
        return self.common_name

    def set_scientific_name(self, scientific_name):
        if scientific_name is not None:
            self.scientific_name = scientific_name

    def get_scientific_name(self):
        return self.scientific_name

    def set_other_name(self, other_name):
        if other_name is not None:
            self.other_name = other_name

    def get_other_name(self):
        return self.other_name

    def set_sunlight(self, sunlight):
        if sunlight is not None:
            self.sunlight = sunlight

    def get_sunlight(self):
        return self.sunlight

    def set_pruning(self, pruning):
        if pruning is not None:
            self.pruning = pruning

    def get_pruning(self):
        return self.pruning

    def set_pruning_count(self, pruning_count):
        if pruning_count is not None:
            self.pruning_count = pruning_count

    def get_pruning_count(self):
        return self.pruning_count

    def set_seeds(self, seeds):
        if seeds is not None:
            self.seeds = seeds

    def get_seeds(self):
        return self.seeds

    def set_propogation(self, propogation):
        if propogation is not None:
            self.propogation = propogation

    def get_propogation(self):
        return self.propogation

    def set_hardiness(self, hardiness):
        if hardiness is not None:
            self.hardiness = hardiness

    def get_hardiness(self):
        return self.hardiness

    def set_flowering_season(self, flowering_season):
        if flowering_season is not None:
            self.flowering_season = flowering_season

    def get_flowering_season(self):
        return self.flowering_season

    def set_indoor(self, indoor):
        if indoor is not None:
            self.indoor = indoor

    def get_indoor(self):
        return self.indoor

    def set_care(self, care):
        if care is not None:
            self.care = care

    def get_care(self):
        return self.care

    def set_water_quality(self, water_quality):
        if water_quality is not None:
            self.water_quality = water_quality

    def get_water_quality(self):
        return self.water_quality

    def set_water_period(self, water_period):
        if water_period is not None:
            self.water_period = water_period

    def get_water_period(self):
        return self.water_period

    def set_water_vol(self, water_vol):
        if water_vol is not None:
            self.water_vol = water_vol

    def get_water_vol(self):
        return self.water_vol

    def set_water_temp(self, water_temp):
        if water_temp is not None:
            self.water_temp = water_temp

    def get_water_temp(self):
        return self.water_temp

    def set_water_ph(self, water_ph):
        if water_ph is not None:
            self.water_ph = water_ph

    def get_water_ph(self):
        return self.water_ph

    def grab_data(self, api, id):# TODO: query api and return data
        return None

    def filter_data(self, raw, query):# TODO: sanitize and filter raw data based on query, return filtered list
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


