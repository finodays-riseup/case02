import requests
import streamlit as st

from ui.pages.abstract_page import AbstractPage
from config import API_BASE_URL


class ResultPage(AbstractPage):
    def _update_state(self):
        st.session_state.update(page="form")

    def render(self):
        rt = self._root

        data = st.session_state["form_data"]
        if data["property_type"] == "Недвижимость":
            path = "/real_estate/predict_price"
        elif data["property_type"] == "Автомобиль":
            path = "/vehicle/predict_price"
        else:
            assert False
        response = requests.post(API_BASE_URL + path, json=data)

        rt.write("Input:")
        rt.write(data)
        rt.write("API Response:")
        rt.write(response.json())
        rt.button("Назад", on_click=self._update_state)
