from abstract_model import AbstractModel


class RealEstateEco(AbstractModel):
    LEVEL_COEFFICENT_FLAT = 0.99
    LEVEL_COEFFICENT_HOUSE = 0.999
    MATERIAL_COEFFICENT = {
        "Другое": 0.9,
        "Панельный": 0.85,
        "Монолитный": 0.9,
        "Кирпичный": 0.95,
        "Блочный": 0.85,
        "Деревянный": 1,
    }

    def predict(self, features):
        level_coefficent = RealEstateEco.LEVEL_COEFFICENT_FLAT if features[
            'relty_type'] == 'Квартира' else RealEstateEco.LEVEL_COEFFICENT_HOUSE
        return RealEstateEco.MATERIAL_COEFFICENT[features['building_type']] * (
            level_coefficent**features['level'])