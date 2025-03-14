import streamlit as st


def ml_pipeline_body():
    """Development of the ML Pipeline"""

    # === HEADER SECTION ===
    st.subheader("*ML Pipeline*")

    # === INTRODUCTION ===
    # Overview of ML pipeline concept
    st.info(
        "A **Machine Learning (ML) Pipeline** is like a recipe that turns raw data into useful predictions through a series of organized steps. Think of it as an assembly line where data moves through different stations, each performing a specific task."
    )
    st.markdown(
        """
        - [ML Pipeline Steps](#ml-pipeline-steps)
        - [Overfitting Prevention in the Current Implementation](#overfitting-prevention-in-the-current-implementation) 
        - [Why Confusion Matrices Do not Apply Here](#why-confusion-matrices-do-not-apply-here)
            - [What We Use Instead](#what-we-use-instead)
        - [Understanding R-squared in BulldozerPriceGenius](#understanding-r-squared-in-bulldozerpricegenius)
            - [What R-squared Tells Us](#what-r-squared-tells-us)
            - [Why We Use R-squared](#why-we-use-r-squared)
            - [Important Limitations](#important-limitations)
            - [Additional Checks](#additional-checks)
        """
    )
    st.write("---")

    # === ML PIPELINE STEPS ===
    st.subheader("ML Pipeline Steps")

    # Pipeline overview description
    st.write(
        "Each component works in harmony to create a robust, scalable machine learning solution that delivers consistent results. Let's explore a detailed walkthrough of the machine learning pipeline we used to predict bulldozer sale prices:"
    )

    # Step 1: Problem Definition
    st.markdown("**1. Problem Definition:**")
    st.markdown(
        """
        - **Goal:** Predict the future sale price of a bulldozer based on its characteristics and historical sales data.
        - **Problem Type:** `Regression` (predicting a continuous value - sale price).
        - **Specifics:** `Time series` or `forecasting problem` (predicting future sales based on past sales).
        """
    )

    # Step 2: Data Collection & Preparation
    st.markdown("**2. Data Collection & Preparation:**")
    st.markdown(
        """
        - **Data Source:** Kaggle Bluebook for Bulldozers competition dataset (`TrainAndValid.csv`).
        - **Data Loading:** Import data into a pandas DataFrame using `pd.read_csv()`.
        - **Data Cleaning:**
            - Parsing dates: Convert the `'saledate'` column to datetime objects
            - Sorting data: Sort the DataFrame by `'saledate'`
        - **Feature Engineering:**
            - Creating new features from `'saledate'`
            - Enhancing predictive power with relevant features
        """
    )

    # Step 3: Exploratory Data Analysis
    st.markdown("**3. Exploratory Data Analysis (EDA):**")
    st.markdown(
        """
        - **Data Visualization:** Create plots to understand feature relationships
            - Example: Scatter plots, histograms, bar charts
        - **Data Insights:** Gain insights from data to guide modeling decisions
            - Example: Identifying patterns, trends, and outliers
        """
    )

    # Step 4: Data Preprocessing
    st.markdown("**4. Data Preprocessing:**")
    st.markdown(
        """
        - **Handling Missing Values:**
            - Strategies: Imputation, removal of rows/columns
        - **Feature Transformation:**
            - Convert categorical features to numerical
                - Technique: Using `pandas categories` and `.cat.codes`
            - Scale numerical features as needed
        """
    )

    # Step 5: Model Selection
    st.markdown("**5. Model Selection:**")
    st.markdown(
        """
        - **Choosing an Algorithm:**
            - Considerations: Dataset size, problem type, algorithm characteristics
            - Example: `RandomForestRegressor`
        - **Model Instantiation:** Create instance of chosen model
        """
    )

    # Step 6: Model Training
    st.markdown("**6. Model Training:**")
    st.markdown(
        """
        - **Splitting Data:** Divide into training and validation sets
        - **Fitting the Model:**
            - Train using training data
            - Provide input `features (X)` and `target variable (y)`
        """
    )

    # Step 7: Model Evaluation
    st.markdown("**7. Model Evaluation:**")
    st.markdown(
        """
        - **Predicting on Validation Set:** Test model performance
        - **Evaluation Metric:** Calculate `RMSLE`
        - **Comparison with Baseline:** Compare with average predictions
        """
    )

    # Step 8: Model Tuning
    st.markdown("**8. Model Tuning & Optimization:**")
    st.markdown(
        """
        - **Hyperparameter Tuning:**
            - Techniques: Grid search, randomized search, cross-validation
        - **Feature Selection:** Identify important features
        """
    )

    # Step 9: Deployment
    st.markdown("**9. Deployment & Prediction:**")
    st.markdown(
        """
        - **Train on Full Data:** Use combined dataset
        - **Predict on Test Data:** Make final predictions
        """
    )
    st.write("---")

    # === OVERFITTING PREVENTION SECTION ===
    st.subheader("Overfitting Prevention in the Current Implementation")
    st.write(
        """
        The notebooks in this **BulldozerPriceGenius (BPG)** currently focuses on data preprocessing and exploratory data analysis (EDA) using `RandomForestRegressor`. While it doesn't explicitly implement overfitting prevention techniques, the RandomForestRegressor itself helps prevent overfitting in two ways:
        """
    )
    st.markdown(
        """
        - **Built-in Protection**: It combines multiple decision trees, which naturally reduces overfitting compared to using a single tree
        - **Feature Randomization**: It randomly selects features when building trees, which helps prevent the model from memorizing training data
        """
    )

    st.write(
        """
        The current implementation therefore provides basic **overfitting protection** through `RandomForestRegressor`.
        """
    )
    st.write("---")

    # === CONFUSION MATRIX SECTION ===
    st.subheader("Why Confusion Matrices Do not Apply Here")
    st.write(
        """
        The **BulldozerPriceGenius (BPG) notebooks** use a `price prediction model` that works with continuous numerical values (such as $50,000 or $75,000), not categories. `Confusion matrices`, in contrast, are designed for classification problems where predictions fit into distinct categories (like "spam" versus "not spam").
        """
    )

    st.subheader("What We Use Instead")
    st.write(
        "For **price predictions**, we need `regression metrics` that measure how close our predictions are to actual values:"
    )
    st.markdown(
        """
        - **MSE (Mean Squared Error)**: Shows the average amount our predictions miss by
        - **RMSE (Root Mean Squared Error)**: Similar to MSE but in actual dollar values
        - **MAE (Mean Absolute Error)**: Shows the average difference between predicted and actual prices
        - **R-squared**: Tells us how well our model explains price changes
        """
    )
    st.write(
        """
        These metrics help us understand how accurate our price predictions are in practical terms.
        """
    )
    st.write("---")

    # === R-SQUARED SECTION ===
    st.subheader("Understanding R-squared in BulldozerPriceGenius")
    st.write(
        """
        **R-squared** (`R²`) measures how well our model predicts bulldozer prices based on their features. Think of it as a **"prediction accuracy score"**.
        """
    )

    st.subheader("What R-squared Tells Us")
    st.markdown(
        """
        - `R²` goes from `0%` to `100%`
        - `100%` means perfect **predictions**
        - `0%` means **poor predictions**
        """
    )

    st.subheader("Why We Use R-squared")
    st.write("We chose `R²` for three main reasons:")
    st.markdown(
        """
        - **Simple to Understand**: Shows accuracy as a clear percentage
        - **Industry Trusted**: Standard tool for price prediction
        - **Progress Tracking**: Helps us improve our model
        """
    )

    st.subheader("Important Limitations")
    st.markdown(
        """
        - Can't detect prediction bias on its own
        - More features might inflate the score
        - Doesn't guarantee accurate predictions
        """
    )

    st.subheader("Additional Checks")
    st.write(
        "That's why we also use `MAE` and `RMSLE` to double-check our model's performance."
    )
    st.write("---")

    # === STYLING ===
    # Custom CSS for better list formatting and reduced line spacing
    st.markdown(
        """
        <style>
        [data-testid="stMarkdownContainer"] ul {
            padding-left: 40px;
        }
        [data-testid="stMarkdownContainer"] li {
            margin-bottom: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
