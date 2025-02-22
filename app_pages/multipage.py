import streamlit as st

class MultiPage:
    def __init__(self, app_name):
        self.app_name = app_name
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.selectbox('Select a page', self.pages, format_func=lambda page: page['title'])
        page['function']()