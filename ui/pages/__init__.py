import typing

import streamlit as st

from .abstract_page import AbstractPage
from .form_page import FormPage
from .result_page import ResultPage
from .not_found_page import NotFoundPage

MAPPING: dict[str, typing.Type[AbstractPage]] = {"form": FormPage, "result": ResultPage}
DEFAULT_PAGE = "form"


def dispatch():
    page = st.session_state.setdefault("page", DEFAULT_PAGE)
    MAPPING.get(page)(st.container()).render()
