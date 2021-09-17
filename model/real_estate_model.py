from model import Model
import numpy as np
import pandas as pd
from geopy.distance import geodesic


class RealEstateModel(Model):
    COLUMNS = [
        'geo_lat', 'geo_lon', 'building_type', 'level', 'levels', 'rooms',
        'area', 'kitchen_area', 'city_center_distance', 'population'
    ]

    MATERIALS_ENCODING = {
        "Другое": 0,
        "Панельный": 1,
        "Монолитный": 2,
        "Кирпичный": 3,
        "Блочный": 4,
        "Деревянный": 5,
    }

    def __init__(self, model_path, cities_path):
        super().__init__(model_path)
        self._cities = pd.read_csv(cities_path)

    def encode_features(self, features):
        encoded_features = {}
        for column in RealEstateModel.COLUMNS:
            if column in features:
                encoded_features[column] = features[column]
            else:
                encoded_features[column] = None
        encoded_features['building_type'] = RealEstateModel.MATERIALS_ENCODING[
            encoded_features['building_type']]
        if features['is_studio']:
            encoded_features['rooms'] = 0

        distance = float("+inf")
        population = 0
        coordinates = (features['geo_lat'], features['geo_lon'])
        for (_, city) in self._cities.iterrows():
            cur_distance = geodesic((city['geo_lat'], city['geo_lon']),
                                    coordinates)
            if cur_distance < distance:
                distance = cur_distance
                population = city['population']
        encoded_features['population'] = population
        encoded_features['city_center_distance'] = distance

        return pd.DataFrame.from_dict(encoded_features)

    def decode_target(self, target):
        return np.exp(target)[0]
