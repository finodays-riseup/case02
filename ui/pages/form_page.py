import streamlit as st

from .abstract_page import AbstractPage
from .form_options import *

INT_MAX = (1 << 53) - 1
FLOAT_MAX = 1e100


class FormPage(AbstractPage):
    def __init__(self, root):
        super().__init__(root)
        self._data = {}

    def _render_realty_inputs(self):
        d = self._data
        rt = self._root

        d["realty_type"] = rt.selectbox("Тип недвижимости", options=REALTY_TYPE_OPTIONS)
        d["material"] = rt.selectbox("Материал дома", options=MATERIAL_OPTIONS)
        if d.get("realty_type") == "Квартира":
            col1, col2 = rt.columns(2)
            d["levels"] = int(
                col1.number_input(
                    "Количество этажей", step=1, min_value=1, max_value=999, value=5
                )
            )
            d["level"] = int(
                col2.number_input(
                    "Этаж", step=1, min_value=1, max_value=d.get("levels")
                )
            )
            d["is_studio"] = bool(rt.checkbox("Студия"))
        else:
            d["levels"] = int(
                rt.number_input(
                    "Количество этажей", step=1, min_value=1, max_value=999, value=5
                )
            )

        d["rooms"] = (
            -1
            if d.get("is_studio")
            else int(
                rt.number_input("Количество комнат", step=1, min_value=1, max_value=100)
            )
        )
        col1, col2 = rt.columns(2)
        d["area"] = col1.number_input(
            "Площадь (кв. м)", step=0.1, min_value=0.0, max_value=FLOAT_MAX
        )
        d["kitchen_area"] = col2.number_input(
            "Площадь кухни (кв. м)", step=0.1, min_value=0.0, max_value=d.get("area")
        )
        col1, col2 = rt.columns(2)
        d["geo_lat"] = col1.number_input(
            "Широта", value=0.0, min_value=-90.0, max_value=90.0
        )
        d["geo_lon"] = col2.number_input(
            "Долгота", value=0.0, min_value=-180.0, max_value=180.0
        )

    def _render_vehicle_inputs(self):
        d = self._data
        rt = self._root

        col1, col2 = rt.columns([2, 1])
        d["brand"] = col1.selectbox("Марка", options=BRAND_OPTIONS)
        d["year"] = col2.number_input(
            "Год выпуска", step=1, min_value=1970, max_value=2021
        )
        if d.get("brand") != "Другое":
            col, *cols = rt.columns(3)
            d["model"] = col.selectbox(
                "Модель", options=MODEL_OPTIONS_BY_BRAND.get(d.get("brand"), [])
            )
        else:
            cols = rt.columns(2)
        d["body_type"] = cols[0].selectbox("Кузов", options=BODY_TYPE_OPTIONS)
        d["color"] = cols[1].selectbox("Цвет", options=COLOR_OPTIONS)
        d["complectation"] = rt.text_input("Комплектация")

        cols = rt.columns(3)
        d["fuel_type"] = cols[0].selectbox("Топливо", options=FUEL_TYPE_OPTIONS)
        d["engine_volume"] = cols[1].number_input(
            "Объем двигателя",
            step=0.1,
            min_value=0.0,
            max_value=0.0 if d.get("fuel_type") == "Электро" else FLOAT_MAX,
        )
        d["engine_power"] = cols[2].number_input(
            "Мощность двигателя", step=1, min_value=0
        )

        cols = rt.columns(2)
        d["drive"] = cols[0].selectbox("Привод", options=DRIVE_OPTIONS)
        d["transmission"] = cols[1].selectbox(
            "Трансмиссия", options=TRANSMISSION_OPTIONS
        )

        cols = rt.columns(3)
        d["wheel"] = cols[0].selectbox("Руль", options=WHEEL_OPTIONS)
        d["mileage"] = cols[1].number_input(
            "Пробег", step=1, min_value=0, max_value=INT_MAX
        )
        d["owners_count"] = cols[2].number_input(
            "Количество владельцев", step=1, min_value=1
        )

    def _update_state(self):
        st.session_state.update(form_data=self._data, page="result")

    def render(self):
        d = self._data
        rt = self._root

        d["property_type"] = rt.radio("Тип имущества", options=PROPERTY_TYPE_OPTIONS)
        if d.get("property_type") == "Недвижимость":
            self._render_realty_inputs()
        elif d.get("property_type") == "Автомобиль":
            self._render_vehicle_inputs()

        rt.button("Отправить", on_click=self._update_state)
