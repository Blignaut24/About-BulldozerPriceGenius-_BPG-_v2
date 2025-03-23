import streamlit as st
import pandas as pd


def interactive_prediction_body():
    """
    Main function to handle the interactive prediction dashboard.
    Loads data, creates filters, and displays filtered results.
    """

    @st.cache_data
    def load_data():
        """Load and cache the bulldozer dataset with optimized memory usage"""
        data_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
        # Specify data types to reduce memory usage
        dtypes = {
            "SalePrice": "float32",
            "YearMade": "int16",
            "saleYear": "int16",
            "saleDayofyear": "int16",
            "ModelID": "int32",
            "SalesID": "int32",
            "MachineID": "int32",
        }
        # Read only necessary columns
        needed_columns = [
            "SalePrice",
            "state",
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
            "Grouser_Tracks",
            "Hydraulics",
        ]
        data = pd.read_csv(
            data_path, usecols=needed_columns, dtype=dtypes, memory_map=True
        )
        return data

    # Load the dataset
    data = load_data()

    # Sidebar filters
    st.sidebar.header("Filters")

    # Set price range boundaries
    min_price = 0
    max_price = 142000

    # Create price range selector
    price_range = st.sidebar.slider(
        "Select Price Range $",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price),
    )

    # Add state filter
    states = sorted(data["state"].unique())
    state_options = ["All States"] + states
    selected_state = st.sidebar.selectbox("Select State", state_options)

    # Filter dataset based on selected price range and state
    filtered_data = data[
        (data["SalePrice"] >= price_range[0]) & (data["SalePrice"] <= price_range[1])
    ]

    # Apply state filter if a specific state is selected
    if selected_state != "All States":
        filtered_data = filtered_data[filtered_data["state"] == selected_state]

    # Display price range header
    st.subheader(
        f"Bulldozers within Price Range USA Dollars: {int(price_range[0]):,} - {int(price_range[1]):,}"
    )

    # Display state selection if specific state is selected
    if selected_state != "All States":
        st.subheader(f"State: {selected_state}")

    # Reorder columns to show SalePrice and state first
    cols = ["SalePrice", "state"] + [
        col for col in filtered_data.columns if col not in ["SalePrice", "state"]
    ]
    filtered_data = filtered_data[cols]

    # Show filtered data in table format
    st.dataframe(filtered_data, use_container_width=True)


if __name__ == "__main__":
    interactive_prediction_body()
