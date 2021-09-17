from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def predict(self, features):
        pass
