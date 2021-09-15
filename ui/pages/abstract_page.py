from abc import ABC, abstractmethod

import streamlit as st


class AbstractPage(ABC):
    def __init__(self, root: st.delta_generator.DeltaGenerator):
        self._root = root

    def _update_state(self):
        pass

    @abstractmethod
    def render(self):
        pass
