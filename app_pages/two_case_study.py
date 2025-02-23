# Import the Streamlit library which we'll use to create our web app
import streamlit as st
import pandas as pd

def case_study_body():
    # Add a main header for the overview section
    st.header("Case Study")

    # Add a subtitle that explains the app's purpose in one line
    st.subheader(
        "BulldozerPriceGenius BPG: Know Your Equipment's Worth, Make Smarter Auction Decisions."
    )

    # Load the CSV file
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = pd.read_csv(csv_file_path)

    # Add a checkbox to toggle the display of the CSV table
    if st.checkbox("Inspect dataframe"):
        st.dataframe(df)