# Import required libraries
import streamlit as st
from app_pages.dark_theme import apply_dark_theme


class MultiPage:
    """
    A class to handle multi-page Streamlit applications
    Allows creation and management of multiple pages within a single Streamlit app
    """
    
    def __init__(self, app_name):
        """
        Initialize MultiPage class
        Args:
            app_name (str): Name of the Streamlit application
        """
        self.app_name = app_name
        self.pages = []  # List to store page configurations

    def add_page(self, title, func):
        """
        Add a new page to the application
        Args:
            title (str): Title of the page
            func (callable): Function that renders the page content
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Configure and run the multi-page application
        Sets up page configuration and renders selected page
        """
        # Note: Page configuration moved to app.py to avoid duplicate set_page_config() calls

        # Apply dark theme globally
        apply_dark_theme()

        st.title(f"{self.app_name} 🚜")
        
        # Create sidebar navigation
        page = st.sidebar.selectbox(
            "Select a page", 
            self.pages, 
            format_func=lambda page: page["title"]
        )
        
        # Execute selected page function
        page["function"]()