import streamlit as st

from ui.pages.abstract_page import AbstractPage


class NotFoundPage(AbstractPage):
    def render(self):
        rt = self._root

        rt.error('Страница "{}" не найдена.'.format(st.session_state.get("page")))
        rt.button("На главную", on_click=st.session_state.clear)
