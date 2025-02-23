import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.one_project_overview import project_overview_body
from app_pages.two_case_study import case_study_body
<<<<<<< HEAD
from app_pages.three_model_performance import model_performance_body
from app_pages.four_interactive_prediction import interactive_prediction_body
from app_pages.five_documentation import documentation_body
=======
>>>>>>> 3f1735c2270901361b130d0590ffe3cd686add04

# Create an instance of the app
app = MultiPage(app_name="BulldozerPriceGenius(BPG)")

# Set the title
st.title("BulldozerPriceGenius(BPG)")

# App pages
app.add_page("one_project_overview", project_overview_body)
app.add_page("two_case_study", case_study_body)
<<<<<<< HEAD
app.add_page("three_model_performance", model_performance_body)
app.add_page("four_interactive_prediction", interactive_prediction_body)
app.add_page("five_documentation", documentation_body)
=======
>>>>>>> 3f1735c2270901361b130d0590ffe3cd686add04

# Run the app
app.run()