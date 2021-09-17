from abc import ABC, abstractmethod
import pickle


class Model(ABC):
    def __init__(self, path):
        with open(path, 'rb') as file:
            self._model = pickle.load(file)

    def predict(self, features):
        encoded_features = self.encoded_features(features)
        return self.decode_target(self._model.predict(encoded_features))

    @abstractmethod
    def encode_features(self, features):
        pass

    @abstractmethod
    def decode_target(self, target):
        pass
