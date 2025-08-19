import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.one_case_study import case_study_body  # Case Study Page
from app_pages.two_hypothesis_and_validation import hypothesis_and_validation_body  # Hypothesis & Validation Page
from app_pages.three_project_framework import project_framework_body  # Project Framework Page
from app_pages.four_interactive_prediction import interactive_prediction_body  # Interactive Prediction Page
from app_pages.five_documentation import documentation_body  # Documentation Page
from app_pages.six_ml_pipeline import ml_pipeline_body  # ML Pipeline Page

# Create an instance of the app
app = MultiPage(app_name="BulldozerPriceGenius(BPG)")  # App name displayed in the UI

# Add app pages
app.add_page("one_case_study", case_study_body)  # Add Case Study page
app.add_page("two_hypothesis_and_validation", hypothesis_and_validation_body)  # Add Hypothesis & Validation page
app.add_page("three_project_framework", project_framework_body)  # Add Project Framework page
app.add_page("four_interactive_prediction", interactive_prediction_body)  # Add Interactive Prediction page
app.add_page("five_documentation", documentation_body)  # Add Documentation page
app.add_page("six_ml_pipeline", ml_pipeline_body)  # Add ML Pipeline page

# Run the app
app.run()  # Start the Streamlit app
