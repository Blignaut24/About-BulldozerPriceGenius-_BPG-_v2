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
<<<<<<< HEAD
        st.title(self.app_name)
=======
>>>>>>> 3f1735c2270901361b130d0590ffe3cd686add04
        page = st.sidebar.selectbox('Select a page', self.pages, format_func=lambda page: page['title'])
        page['function']()