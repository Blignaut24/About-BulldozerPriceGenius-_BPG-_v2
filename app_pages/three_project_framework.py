# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import os


# ===== HELPER FUNCTIONS =====
# Function to load data from a CSV file
def load_data(csv_file_path, nrows=None):
    return pd.read_csv(csv_file_path, nrows=nrows)


# Function to load data from a Parquet file
def load_parquet_data(parquet_file_path, nrows=None):
    return pd.read_parquet(parquet_file_path)


def safe_display_image(image_path, alt_text="Image", caption=None, fallback_message=None):
    """
    Safely display an image with fallback handling for missing files.

    Args:
        image_path (str): Path to the image file
        alt_text (str): Alternative text for accessibility
        caption (str): Optional caption for the image
        fallback_message (str): Custom message to display if image is missing
    """
    # Try multiple possible paths for the image
    possible_paths = [
        image_path,  # Original path
        f"static/images/{os.path.basename(image_path)}",  # Alternative static path
    ]

    image_found = False
    for path in possible_paths:
        if os.path.exists(path):
            try:
                st.image(path, caption=caption)
                image_found = True
                break
            except Exception:
                continue

    if not image_found:
        # Display fallback content
        if fallback_message:
            st.info(fallback_message)
        else:
            st.warning(f"📊 **{alt_text}** - Image temporarily unavailable. Please refer to the detailed methodology description below.")


# ===== MAIN PAGE FUNCTION =====
# Main function to render the Project Framework page
def project_framework_body():
    # ===== PAGE HEADER =====
    st.subheader("*Forecasting Bulldozer Values Using Machine Learning*")
    st.write(
        """
        The **BulldozerPriceGenius (BPG)** project helps users predict bulldozer sale prices using machine learning. By analyzing historical sales data through a **time series regression model**, the app delivers accurate, data-driven valuations. Below is a diagram overview of the BPG project, and this page focuses on the **Cross Industry Standard Process for Data Mining (CRISP-DM)** workflow.
        """
    )
    safe_display_image(
        "static/images/BPG_Framework.webp",
        alt_text="BPG Project Framework Diagram",
        caption="BulldozerPriceGenius (BPG) Project Framework - CRISP-DM Methodology",
        fallback_message="📊 **BPG Project Framework**: This project follows the CRISP-DM (Cross Industry Standard Process for Data Mining) methodology, consisting of 6 phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. Each phase builds upon the previous to ensure systematic and effective machine learning model development for bulldozer price prediction."
    )

    # ===== NAVIGATION =====
    # Table of contents for easy navigation
    st.markdown(
        """
        - [1. Business Understanding](#1-business-understanding)
        - [2. Data Understanding](#2-data-understanding)
        - [3. Data Preparation](#3-data-preparation)
        - [4. Modeling](#4-modeling)
        - [5. Evaluation](#5-evaluation)
        - [6. Deployment](#6-deployment)
        - [Conclusion](#conclusion)
        """
    )
    st.write("---")
    st.header("1. Business Understanding")

    # Core business requirements
    st.subheader("Business Requirements")
    st.write(
        "The core business requirement for the BPG project that drives all decisions concerning the machine learning model is:"
    )
    st.success(
        """
        **Core Business Requirement**: Develop a machine learning model to accurately predict future sale prices of bulldozers with a Root Mean Squared Log Error (RMSLE) below 1.0.
        """
    )

    # Optional: Display detailed business requirements
    if st.checkbox("Show Business Requirements"):
        st.success(
            """
            **Business Requirement 1**: The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.

            **Business Requirement 2**: The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data with a Root Mean Squared Log Error (RMSLE) score of below 1.0.

            **Business Requirement 3**: The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
            """
        )

    st.subheader(
        "Here's a breakdown of how different stakeholders will be impacted by BulldozerPriceGenius:"
    )
    st.markdown(
        """
    **Buyers**:
    - Make more informed purchasing decisions by understanding fair market values
    - Filter and browse listings across U.S. states based on location and predicted prices
    - Reduce risk of overpaying for equipment

    **Sellers**:
    - Price bulldozers more accurately for auctions
    - Optimize timing and strategy for selling equipment
    - Avoid leaving money on the table through data-driven pricing

    **Auctioneers (Fast Iron)**:
    - Create a standardized pricing reference similar to Kelly Blue Book for bulldozers
    - Increase market transparency and efficiency
    - Improve buyer and seller confidence in auction processes

    **App Owner and Developers**:
    - Establish a valuable market position by providing essential pricing intelligence
    - Build trust through accurate predictions using comprehensive auction data analysis
    - Create recurring value through continuous model updates and market insights
    """
    )
    st.write("---")

    # ===== SECTION 2: DATA UNDERSTANDING =====
    st.header("2. Data Understanding")

    # Overview of available data
    st.subheader("What Data Do We Have?")
    st.write(
        """
        Our project uses three main datasets from [Kaggle](https://www.kaggle.com/c/bluebook-for-bulldozers/data):
        - **Training data**: Sales records up to `2011`
        - **Validation data**: Sales from `January to April 2012`
        - **Test data**: Sales from `May to November 2012`
        """
    )

    # Data quality check
    st.subheader("Data Quality Check")
    st.write(
        """
        The dataset has over `400,000` entries (bulldozer sales records).
        Here's what we found:

        - **Good Points:**
            - Large dataset with detailed information
            - Covers multiple years of sales
            - Contains various machine details
        - **Challenges:**
            - Some missing information in important fields
            - Mixed data types that need cleaning
            - Dates need to be converted to the right format
        """
    )

    # Load and display the dataset
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(csv_file_path, nrows=500)  # Load only the first 500 rows

    # Optional: Inspect missing values in the dataset
    if st.checkbox("DataFrame Inspection: Missing Values"):
        st.write("View the first `500` entries from a total of `10,000`")
        st.dataframe(df)

    # Optional: Inspect processed dataset for mixed data types
    processed_file_path = "data/processed/TrainAndValid_processed.csv"
    df_processed = load_data(
        processed_file_path, nrows=500
    )  # Limit the number of rows loaded to avoid memory issues
    if st.checkbox("DataFrame Inspection: Data Mixed Types"):
        st.write("This indicates that several columns contain mixed data types, where a single column might have both strings and integers, for example.")
        buffer = io.StringIO()
        df_processed.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    # Explanation of dataset structure
    st.subheader("What Each Part Means")
    if st.checkbox("Main Types of Information"):
        st.write("The dataset includes these main types of information:")
        st.info(
            """
            - **Basic Details**:
                - **Sales ID**: Unique number for each sale
                - **Machine ID**: Unique number for each bulldoer
                - **Sale Price**: How much the bulldozer sold for (this is what we want to predict)
            - **Machine Information**:
                - **Year Made**: When the bulldozer was built
                - **Usage Hours**: How many hours the machine has been used
                - **Usage Level**: Low, medium, or high based on hours used
            - **Sale Details**:
                - **Sale Date**: When the bulldozer was sold
                - **State**: Where the sale happened in the USA
            """
        )
    st.write("---")

    # ===== SECTION 3: DATA PREPARATION =====
    st.header("3. Data Preparation")

    # Data cleaning steps
    st.subheader("Data Cleaning")
    st.write(
        """
        1. **Parse Dates**
            - Convert `'saledate'` from string to datetime
            - Sort data chronologically
        2. **Handle Categorical Data**
            - Convert string columns to category type
            - Create numerical representations
        3. **Address Missing Values**
            - Identify columns with missing data
            - Apply appropriate imputation strategies
        """
    )

    # Optional: Check missing values in the dataset
    if st.checkbox("DataFrame Inspection: Identify columns with missing data"):
        st.write("This calculates the total missing values per column efficiently, rather than checking rows one by one.")
        parquet_file_path = (
            "data/processed/TrainAndValid_object_values_as_categories.parquet"
        )
        df_tmp = load_parquet_data(parquet_file_path)
        missing_values = df_tmp.isna().sum().sort_values(ascending=False)[:25]
        st.write(missing_values)

    # Feature engineering steps
    st.subheader("Feature Engineering")
    st.write(
        """
        1. **Date-based Features**
            - Extract year, month, day from saledate
            - Create day of week and day of year features
        2. **Categorical Encoding**
            - One-hot encoding for nominal categories
            - Label encoding for ordinal categories
        3. **Derived Features**
            - Calculate machine age at sale
            - Create usage intensity metrics
        """
    )

    # Data transformation steps
    st.subheader("Data Transformation")
    st.write(
        """
        1. **Scaling**
            - Normalize numerical features
            - Handle outliers appropriately
        2. **Final Processing**
            - Format data for model input
            - Split into training and validation sets
        3. **Quality Checks**
            - Verify data completeness
            - Validate transformations
        """
    )

    # Optional: Inspect random sample rows
    parquet_file_path = "data/processed/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet"
    df_tmp = load_parquet_data(parquet_file_path)
    if st.checkbox("Quality Checks: Inspection of Random Sample Rows"):
        st.write(df_tmp.sample(5))
    st.write("---")

    # ===== SECTION 4: MODELING =====
    st.header("4. Modeling")
    st.write(
        """
        This section focuses on selecting, training, and testing a suitable machine learning model to predict bulldozer sale prices.
        """
    )
    st.subheader("Choose Model Type")
    st.markdown(
        """
        - **Model Selection:** We picked the `Random Forest` model because it has worked well for similar projects before and is known to handle this type of data well.
        - **Choosing the Right Tool:** Given that we have a lot of data (over 100,000 examples) and need to predict prices, we looked at two main options:
            - `SGD Regressor`: A simple math model that learns by looking at one example at a time.
            - `Random Forest`: A more advanced model that uses multiple decision trees to make better predictions.
        - **Final Choice:** We went with the Random Forest model because it has a good track record with similar projects and usually gives reliable results across many different types of data.
        """
    )
    st.subheader("Train the Model")
    st.markdown(
        """
        **Data Preparation**: Before we can train our model, we need to prepare our data properly:
        """
    )
    st.markdown(
        """
        - **Convert to Numeric**: First, we need to turn all text data into numbers that our computer can understand. We do this by putting similar items into categories and giving each category a number.
        """
    )
    st.markdown(
        """
        - **Handling Missing Values**: Next, we look at any missing information in our data. When we find gaps, we either fill them in with reasonable values or use special techniques to work around them.
        """
    )
    st.markdown(
        """
        **Training Process**: The RandomForestRegressor is trained using the preprocessed data.
        """
    )
    st.markdown(
        """
        **Hyperparameter Tuning:** Parameters like the number of trees in the Random Forest can be optimized for better performance.
        """
    )
    st.subheader("Test the Model")
    st.markdown(
        """
        - **Evaluation Metric**: We use the Root Mean Squared Log Error (RMSLE) as our evaluation metric, which aligns with the Kaggle competition and sets a target accuracy goal of under 1 RMSLE.
        """
    )
    st.markdown(
        """
        - **Validation Set**: Allows for assessment of the model's generalization performance on unseen data.
        """
    )
    st.markdown(
        """
        - **Performance Comparison**: The RMSLE obtained would be compared against the Kaggle leaderboard to benchmark the model's effectiveness.
        """
    )
    st.markdown(
        """
        - **Further Testing**: After we test our model on the validation data, we'll do one final test using a separate set of data we've kept aside. This helps us better understand how well our model will work in real-life situations.
        """
    )
    st.write("---")

    # ===== SECTION 5: EVALUATION =====
    st.header("5. Evaluation")
    st.subheader("Did We Meet Our Goals?")
    st.write("**Business Requirement 1:**")
    st.markdown(
        """
        - **Goal Achievement:** The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.
        - **Achievement Status:** Yes, this goal was successfully achieved. The Random Forest model provided clear insights into the top 20 feature importance values for Best RandomForestRegressor Model.
        """
    )

    if st.checkbox("Inspection: Feature Importance"):
        st.image("results/feature_importance.webp")

    # Define the DataFrame
    data = {
        "Feature": [
            "Year Made",
            "Product Size",
            "Sale Year",
            "Model Description",
            "Model ID",
            "Other Features",
        ],
        "Importance": [
            19.9,
            15.5,
            7.7,
            5.7,
            5.6,
            45.6,
        ],  # Numeric values for percentages
    }
    df = pd.DataFrame(data)

    # Add a checkbox to display the pie chart
    if st.checkbox("Inspection: Top 5 Feature Importance Pie Chart"):
        # Create a pie chart
        fig, ax = plt.subplots()
        ax.pie(
            df["Importance"],
            labels=df["Feature"],
            autopct="%1.1f%%",
            startangle=90,
            colors=plt.cm.Paired.colors,
        )
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.

        # Display the pie chart in Streamlit
        st.pyplot(fig)
        st.subheader("**Analysis of Top Features**")
        st.markdown(
            """
            **Primary Features:**
            - **Year Made** (`19.9%`): The most significant factor, with newer bulldozers commanding higher prices.
            - **Product Size** (`15.5%`): Second most important, larger machines typically cost more.

            **Secondary Features:**
            - **Sale Year** (`7.7%`): Reflects market conditions at time of sale.
            - **Model Description** (`5.7%`): Specific model features impact pricing.
            - **Model ID** (`5.6%`): Different models have varying base prices.
            """
        )

    st.write("**Business Requirement 2:**")
    st.markdown(
        """
        - **Goal Achievement:** The project aims to predict bulldozer sale prices based on their characteristics and historical data. Success is measured using the **Root Mean Squared Log Error (RMSLE)**, with a target benchmark of achieving a score below `1.0`.
        - **Achievement Status:** The project successfully achieved its goal with an impressive RMSLE score of `0.27`, significantly outperforming the target benchmark of `1.0`.
        """
    )

    # Add a checkbox to display the output
    if st.checkbox("Inspection: Prediction vs Reality Analysis"):
        # Display the image
        st.image("results/sale_price.webp")

        # Display price comparison metrics
        st.subheader("Prediction vs Reality")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Model Prediction", f"${55495.68:,.2f}")
        with col2:
            st.metric("Actual Price", f"${72600:,.2f}")

        # Show error metrics
        st.subheader("Performance Metrics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mean Absolute Error (MAE)", f"${17104:,.2f}")
        with col2:
            st.metric("RMSLE Score", "0.27")

        # Analysis of results
        st.subheader("Analysis")
        st.write(
            """
            - RMSLE score of `0.27` indicates reasonable model performance.
            - Model provides valuable pricing guidance.
            - Some room for improvement exists.
            """
        )

        # Price accuracy conclusions
        st.subheader("Conclusion")
        st.write(
            """
            Yes, our hypothesis was validated. Our target **RMSLE score** was below `1.0`, and we achieved `0.27` — **significantly exceeding our expectations**. While we've met our goal, we can still work on reducing the `$17,104` average error to make our predictions even more precise. Users can trust the model's price estimates.
            **What does this mean?**
            - Our predictions are more accurate than expected.
            - Users can trust our model for pricing guidance.
            - The system is ready for real-world use.
            """
        )

    st.write("**Business Requirement 3:**")
    st.markdown(
        """
        - **Goal Achievement:** The user needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
        - **Achievement Status:** Yes, this goal was achieved through the development of an intuitive dashboard that allows users to filter bulldozer entries by price range and U.S. state location.
        """
    )
    # Add a checkbox to display the image
    if st.checkbox("Inspection: Interactive Dashboard Image"):
        st.image("static/images/interactive_dashboard.webp", width=None)
    st.write(
        """
        The dashboard shows a filtered list of bulldozers based on price and location.
        For example, you can see bulldozers in California priced between `$28,771` and `$109516`.
        """
    )

    st.subheader("Is It Good Enough?")
    st.markdown(
        """
        - **Stakeholder Requirements:** The app exceeded its target requirement of achieving an RMSLE score below `1.0`. In the context of the Kaggle Competition leaderboard, which included 428 entries, our model achieved an RMSLE score of `0.27`—ranking 69th overall. For comparison, the top score in the competition was `0.22909`.
        """
    )

    # Add a checkbox to display the Kaggle leaderboard image
    if st.checkbox("Inspection: Kaggle Leaderboard"):
        st.image("static/images/kaggle_leaderboard.webp", use_column_width=True)
        st.write(
            "[*Kaggle Leaderboard*](https://www.kaggle.com/c/bluebook-for-bulldozers/leaderboard)"
        )

    st.markdown(
        """
        - **Cost-Benefit Analysis:** Since the data is several years old, further improvements to the app's accuracy would offer limited value without more recent data. With current data and additional development time, the model's prediction accuracy could improve significantly, potentially advancing our position on the Kaggle Leaderboard and increasing its value to the customer.
        """
    )

    st.subheader("What Are The Areas for Possible Improvement?")
    st.markdown(
        """
        - **Data Cleaning:** We found some missing information in our data. We could improve our results by using special tools that work well with incomplete data.
        - **Adding Better Data Features:** We only used basic time-related information in our analysis. We could make our predictions better by combining existing data in new ways or adding more relevant information about bulldozers.
        - **Trying Different Tools:** We used a tool called Random Forest for our predictions. We could test other tools like CatBoost or XGBoost to see if they work better for our needs.
        """
    )

    st.write("---")

    # ===== SECTION 6: DEPLOYMENT =====
    st.header("6. Deployment")
    st.write(
        """
        The application is deployed and hosted on both [Streamlit](https://streamlit.io/) Cloud and [Heroku](https://www.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=emea_heraw&utm_content=general-branded-search-rsa&utm_term=heroku&utm_source_platform=GoogleAds&gad_source=1&gclid=CjwKCAjwnPS-BhBxEiwAZjMF0s32zmesSen1_nAdsUsoJls9kZQ89I_Rn-alHDSfSWniSlB03TYbfxoCCF8QAvD_BwE) platforms
        """
    )
    st.write("---")

    # ===== SECTION 7: Conclusion =====
    st.header("Conclusion")
    st.write("**Data Project Success Fundamentals**")
    st.write(
        """
        **Project Success Overview**

        The BulldozerPriceGenius project has successfully met all three business requirements, as demonstrated by the validation results on this page and the previous Hypothesis and Validation page. The project's success is attributed to the following key factors:

        **Model Performance**

        Using a Random Forest regression model, the project achieved its primary success metric with an RMSLE score of `0.27`, surpassing the target threshold of `1.0`. The secondary target of **Mean Absolute Error (MAE)** within `$20,000` of actual prices was also met, achieving an average error of `$17,104`.

        **Business Impact**

        The model's feature importance analysis revealed key factors influencing bulldozer prices, providing valuable insights for auction strategies. A user-friendly interface and interactive dashboard ensure accessibility for all users, meeting client requirements.

        **Validation and Future Potential**

        The project's ranking of `69th` out of `428` entries on the **Kaggle leaderboard** further validates its success. While model accuracy could be improved with additional data and feature enhancements, current results show the system is ready for real-world deployment. The project demonstrates the value of data-driven insights in optimizing auction strategies and providing accurate bulldozer price predictions.
        """
    )
    st.write("---")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    project_framework_body()
