import streamlit as st

from model.model import Model
from ui.pages.abstract_page import AbstractPage


@st.cache
def get_real_estate_model() -> Model:
    raise NotImplementedError()


@st.cache
def get_vehicle_model() -> Model:
    raise NotImplementedError()


class ResultPage(AbstractPage):
    def _update_state(self):
        st.session_state.update(page="form")

    def render(self):
        rt = self._root

        data = st.session_state["form_data"]
        model = None
        if data["property_type"] == "Недвижимость":
            model = get_real_estate_model()
        elif data["property_type"] == "Автомобиль":
            model = get_vehicle_model()

        rt.write(model.predict(data))
        rt.button("Назад", on_click=self._update_state)
