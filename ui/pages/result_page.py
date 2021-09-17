import streamlit as st

from ui.pages.abstract_page import AbstractPage


class ResultPage(AbstractPage):
    def _update_state(self):
        st.session_state.update(page="form")

    def render(self):
        rt = self._root

        data = st.session_state["form_data"]
        rt.write(data)
        rt.button("Назад", on_click=self._update_state)
