import streamlit as st
import pandas as pd


def interactive_prediction_body():
    # Load the dataset
    @st.cache_data
    def load_data():
        data_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
        data = pd.read_csv(data_path)
        return data

    # Title
    st.title("Bulldozer Price Prediction")

    # Load data
    data = load_data()

    # First, verify which columns actually exist in the dataset
    available_columns = [
        "SalePrice",
        "ProductSize",
        "saleYear",
        "ModelID",
        "fiModelDesc",
        "Enclosure",
        "fiBaseModel",
        "SalesID",
        "MachineID",
        "Coupler_System",
        "saleDayofyear",
        "Tire_Size",
        "Hydraulics_Flow",
        "state",
        "Grouser_Tracks",
        "Hydraulics",
    ]

    # Sidebar filters
    st.sidebar.header("Filters")

    min_price = 0
    max_price = 142000

    price_range = st.sidebar.slider(
        "Select Price Range $",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price),
    )

    # Filter data
    filtered_data = data[
        (data["SalePrice"] >= price_range[0]) & (data["SalePrice"] <= price_range[1])
    ]

    # Display data
    st.subheader(
        f"Bulldozers within Price Range USA Dollars: ${price_range[0]:,} - ${price_range[1]:,}"
    )

    # Display only the columns that exist in the dataset
    st.dataframe(filtered_data[available_columns], use_container_width=True)
