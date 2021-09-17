from model.pickled_model import PickledModel
import numpy as np
import pandas as pd

class VehicleModel(PickledModel):
    def _encode_features(self, features):
        features["age"] = 2021 - features["year"]
        features.pop("year", None)
        features.pop("model", None)
        features["complectation"] = len(features["complectation"].split(','))
        return pd.DataFrame([features])

    def _decode_target(self, target):
        return np.exp(target)[0]
