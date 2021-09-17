from abc import abstractmethod
import pickle

from model.abstract_model import AbstractModel


class PickledModel(AbstractModel):
    def __init__(self, path):
        with open(path, "rb") as file:
            self._model = pickle.load(file)

    def predict(self, features):
        encoded_features = self._encode_features(features)
        return self._decode_target(self._model.predict(encoded_features))

    @abstractmethod
    def _encode_features(self, features):
        pass

    @abstractmethod
    def _decode_target(self, target):
        pass
