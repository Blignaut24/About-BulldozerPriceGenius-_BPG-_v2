import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.one_project_overview import project_overview_body

# Create an instance of the app
app = MultiPage(app_name="BulldozerPriceGenius(BPG)")

# App pages
app.add_page("one_project_overview", project_overview_body)

# Run the app
app.run()