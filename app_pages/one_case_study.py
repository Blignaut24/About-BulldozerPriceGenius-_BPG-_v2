import streamlit as st


def case_study_body():
    """Case Study for Bulldozer Price Prediction"""

    # === HEADER SECTION ===
    # Application title and description
    st.subheader("*Know Your Equipment's Worth, Make Smarter Auction Decisions.*")
    st.write(
        "BulldozerPriceGenius helps predict how much bulldozers will sell for at auctions. It uses data from past sales on Kaggle to make accurate price predictions, helping buyers and sellers make better decisions in the construction equipment market."
    )
    st.markdown(
        """
        - [Business Objective](#business-objective)
        - [Business Requirements](#business-requirements)
        - [Key Benefits](#key-benefits)
        - [Project Terms:](#project-terms)
        - [Success Metrics](#success-metrics)
        - [Delivery Method](#delivery-method)
        - [Data Set](#data-set)
        - [Data Privacy](#data-privacy)
        """
    )

    st.write("---")

    # === BUSINESS INFORMATION ===
    # Business objective section
    st.subheader("Business Objective")
    st.write(
        "Develop an AI-powered system to predict bulldozer auction prices by analyzing historical sales data and equipment specifications."
    )
    st.write("---")

    # Core business requirements
    st.subheader("Business Requirements")
    st.success(
        """
        **Business Requirement 1**: The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.
        
        **Business Requirement 2**: The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.
        
        **Business Requirement 3**: The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
        """
    )
    st.write("---")

    # === KEY FEATURES AND BENEFITS ===
    # List of main benefits
    st.subheader("Key Benefits")
    st.markdown(
        """
        - Enable data-driven buying and selling decisions
        - Optimize auction pricing strategies
        - Minimize financial risks in transactions 
        """
    )
    st.write("---")

    # === TECHNICAL DOCUMENTATION ===
    # Project terminology and definitions
    st.subheader("Project Terms:")
    if st.checkbox("Show `Project Terms` Glossary"):
        st.info(
            """
            • **AuctioneerID**: The company that conducted the auction sale (different from data source)
            
            • **Bluebook**: A pricing guide used in the heavy equipment industry that provides estimated values for machinery like bulldozers. Similar to Kelley Blue Book for cars
            
            • **Data Source**: Where the sale information came from (some sources provide more detailed information than others)
            
            • **MachineID**: A unique number for each bulldozer (note: one bulldozer can be sold multiple times)
            
            • **Machine Hours**: How many hours the bulldozer has been used when sold (if recorded)
            
            • **ModelID**: A unique number that identifies the specific model of bulldozer
            
            • **Sale Date**: When the bulldozer was sold
            
            • **Sale Price**: How much the bulldozer sold for in US dollars
            
            • **Usage Band**: How much the bulldozer has been used compared to similar models (low, medium, or high)
            
            • **User**: A person who interacts with the software application - typically auctioneers, buyers, or sellers
            
            • **Year Made**: The year the bulldozer was manufactured
            """
        )

    # External reference link
    st.write(
        "*For a complete glossary of project terms and jargon, please refer to the Kaggle* "
        "[*Data Dictionary file*](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
    )
    st.write("---")

    # === PERFORMANCE METRICS ===
    # Success criteria and measurements
    st.subheader("Success Metrics")
    st.markdown(
        """
        - **Primary**: `Root Mean Squared Log Error (RMSLE)` below 1.0
        - **Secondary**: `Mean Absolute Error (MAE)` within $20,000 of actual prices
        """
    )
    st.write("---")

    # === IMPLEMENTATION DETAILS ===
    # Delivery specifications
    st.subheader("Delivery Method")
    st.markdown(
        """
        - Interactive visualization interface
        - Data-driven insights display
        - Access for both technical and non-technical users
        """
    )
    st.write("---")

    # === DATA ARCHITECTURE ===
    # Dataset information and structure
    st.subheader("Data Set")
    st.write(
        """
        The project leverages an extensive dataset of historical bulldozer sales information, carefully sourced from Kaggle's prestigious Bluebook for Bulldozers competition.

        This comprehensive dataset encompasses a wide range of crucial attributes, including detailed model specifications, precise size measurements, accurate sale dates, specific location data, and numerous other relevant parameters.
        """
    )

    st.markdown(
        """
        **The dataset is split into three parts:**
        - `Train.csv`: Historical sales data up to **2011**, used for training the model
        - `Valid.csv`: Sales data from **January 1, 2012,** to **April 30, 2012,** used for validating the model's performance
        - `Test.csv`: Sales data from **May 1, 2012, to November 2012,** used for evaluating the final model
        """
    )

    # Additional data source reference
    st.write(
        "*For more information about the dataset used in this project, please refer to* "
        "[Blue Book for Bulldozers](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
    )
    st.write("---")

    # === COMPLIANCE AND PRIVACY ===
    # Data privacy information
    st.subheader("Data Privacy")
    st.write(
        "`No ethical or privacy concerns` as data is from a public Kaggle competition"
    )

    # === ADDITIONAL RESOURCES ===
    # Reference documentation
    st.write(
        "*For additional information, please visit and read the* "
        "[*Project README file*](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2.git)."
    )
    st.write("---")
