import streamlit as st
import pandas as pd
import sys
import os

# Add src to path for component imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from components.model_id_input import create_model_id_input
    MODELID_COMPONENT_AVAILABLE = True
except ImportError:
    MODELID_COMPONENT_AVAILABLE = False

try:
    from components.year_made_input import create_year_made_input
    YEARMADE_COMPONENT_AVAILABLE = True
except ImportError:
    YEARMADE_COMPONENT_AVAILABLE = False


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
            "YearMade",  # Added YearMade column for filtering
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

    # Section 1: General Information
    st.sidebar.subheader("Section 1: General Information")

    # Add ModelID input component if available
    if MODELID_COMPONENT_AVAILABLE:
        st.sidebar.write("**ModelID**")
        with st.sidebar:
            selected_model_id = create_model_id_input()
            if selected_model_id:
                st.sidebar.success(f"Selected ModelID: {selected_model_id}")
    else:
        st.sidebar.write("**ModelID**")
        st.sidebar.info("💡 ModelID input component not available. Install component for enhanced filtering.")

    # Add YearMade input component if available
    if YEARMADE_COMPONENT_AVAILABLE:
        st.sidebar.write("**YearMade**")
        with st.sidebar:
            selected_year_made = create_year_made_input()
            if selected_year_made:
                st.sidebar.success(f"Selected YearMade: {selected_year_made}")
    else:
        st.sidebar.write("**YearMade**")
        # Fallback input with validation when component not available
        year_input = st.sidebar.text_input(
            "Enter Year Made (1971-2014)",
            placeholder="e.g., 1995, 2005, 2010",
            help="Only years between 1971-2014 are accepted",
            key="fallback_year_input"
        )

        selected_year_made = None
        if year_input:
            try:
                year_value = int(float(year_input.strip()))
                if 1971 <= year_value <= 2014:
                    selected_year_made = year_value
                    st.sidebar.success(f"Selected YearMade: {selected_year_made}")
                else:
                    st.sidebar.error("❌ Only years between 1971-2014 are accepted for YearMade input. Please enter a year within this range for accurate predictions.")
            except ValueError:
                st.sidebar.error("❌ Please enter a valid year (integer only).")

    # Set price range boundaries
    min_price = 0
    max_price = 142000

    # Create price range selector
    st.sidebar.write("**Price Range**")
    price_range = st.sidebar.slider(
        "Select Price Range $",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price),
    )

    # Add state filter
    st.sidebar.write("**Select State**")
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

    # Apply ModelID filter if selected
    if MODELID_COMPONENT_AVAILABLE and 'selected_model_id' in locals() and selected_model_id:
        filtered_data = filtered_data[filtered_data["ModelID"] == selected_model_id]

    # Apply YearMade filter if selected (works for both component and fallback)
    if 'selected_year_made' in locals() and selected_year_made:
        # Check if YearMade column exists before filtering
        if "YearMade" in filtered_data.columns:
            filtered_data = filtered_data[filtered_data["YearMade"] == selected_year_made]
        else:
            st.error("⚠️ YearMade column not found in dataset. Please check data loading.")

    # Display price range header
    st.subheader(
        f"Bulldozers within Price Range USA Dollars: {int(price_range[0]):,} - {int(price_range[1]):,}"
    )

    # Display state selection if specific state is selected
    if selected_state != "All States":
        st.subheader(f"State: {selected_state}")

    # Display ModelID selection if specific ModelID is selected
    if MODELID_COMPONENT_AVAILABLE and 'selected_model_id' in locals() and selected_model_id:
        st.subheader(f"ModelID: {selected_model_id}")

        # Show additional ModelID information if available
        model_id_data = data[data["ModelID"] == selected_model_id]
        if not model_id_data.empty:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Records Found", len(model_id_data))
            with col2:
                if "fiModelDesc" in model_id_data.columns:
                    unique_descriptions = model_id_data["fiModelDesc"].nunique()
                    st.metric("Model Descriptions", unique_descriptions)
            with col3:
                avg_price = model_id_data["SalePrice"].mean()
                st.metric("Average Price", f"${avg_price:,.2f}")
        else:
            st.info(f"No records found for ModelID {selected_model_id} in the current dataset.")

    # Display YearMade selection if specific YearMade is selected
    if 'selected_year_made' in locals() and selected_year_made:
        st.subheader(f"YearMade: {selected_year_made}")

        # Show additional YearMade information if available
        if "YearMade" in data.columns:
            year_data = data[data["YearMade"] == selected_year_made]
        else:
            year_data = pd.DataFrame()  # Empty dataframe if column missing
        if not year_data.empty:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Records Found", len(year_data))
            with col2:
                avg_price = year_data["SalePrice"].mean()
                st.metric("Average Price", f"${avg_price:,.2f}")
            with col3:
                equipment_age = 2025 - selected_year_made
                st.metric("Equipment Age", f"{equipment_age} years")
            with col4:
                # Technology era classification
                if selected_year_made >= 2010:
                    era = "Modern"
                elif selected_year_made >= 2000:
                    era = "Recent"
                elif selected_year_made >= 1990:
                    era = "Mature"
                else:
                    era = "Vintage"
                st.metric("Technology Era", era)
        else:
            st.info(f"No records found for YearMade {selected_year_made} in the current dataset.")

    # Reorder columns to show SalePrice and state first
    cols = ["SalePrice", "state"] + [
        col for col in filtered_data.columns if col not in ["SalePrice", "state"]
    ]
    filtered_data = filtered_data[cols]

    # Show filtered data in table format
    st.dataframe(filtered_data, use_container_width=True)


if __name__ == "__main__":
    interactive_prediction_body()
