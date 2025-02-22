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
        import streamlit as st
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio('Select a page', self.pages, format_func=lambda page: page['title'])
        page['function']()