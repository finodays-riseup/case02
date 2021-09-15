def run():
    import streamlit as st
    from ui.pages import dispatch

    with st.empty():
        dispatch()
