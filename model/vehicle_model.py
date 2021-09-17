from model.pickled_model import PickledModel
import numpy as np
import pandas as pd


class VehicleModel(PickledModel):
    FEATURES = [
        "brand",
        "age",
        "mileage",
        "body_type",
        "color",
        "fuel_type",
        "engine_volume",
        "engine_power",
        "transmission",
        "drive",
        "wheel",
        "owners_count",
        "pts",
        "complectation",
    ]

    LOWER_CASE = [
        "body_type",
        "color",
        "transmission",
        "drive",
    ]

    def _encode_features(self, features):
        features["age"] = 2021 - features["year"]
        features["complectation"] = len(features["complectation"].split(","))
        filtered_features = {key: features.get(key, None) for key in self.FEATURES}
        for key in self.LOWER_CASE:
            filtered_features[key] = filtered_features[key].lower()
        return pd.DataFrame([filtered_features], columns=self.FEATURES)

    def _decode_target(self, target):
        return np.exp(target)[0]
