import streamlit as st

from .abstract_page import AbstractPage
from .form_page import FormPage
from .result_page import ResultPage
from .not_found_page import NotFoundPage

try:
    import typing
except ImportError:
    typing = None

MAPPING = {
    "form": FormPage,
    "result": ResultPage,
}  # type:  dict[str, typing.Type[AbstractPage]]
DEFAULT_PAGE = "form"


def dispatch():
    page = st.session_state.setdefault("page", DEFAULT_PAGE)
    MAPPING.get(page)(st.container()).render()
