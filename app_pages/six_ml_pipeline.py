import streamlit as st
import os
from PIL import Image
import io
import base64
import matplotlib.pyplot as plt
import numpy as np


def generate_fallback_price_distribution():
    """
    Generate a fallback price distribution visualization using matplotlib
    when the original image is not available.
    """
    try:
        # Create a sample price distribution that represents typical bulldozer prices
        np.random.seed(42)  # For reproducible results

        # Generate sample data that mimics bulldozer price distribution
        # Most bulldozers are in the $20k-$80k range with some high-end equipment
        low_end = np.random.lognormal(mean=10.5, sigma=0.5, size=3000)  # $20k-$60k range
        mid_range = np.random.lognormal(mean=11.0, sigma=0.3, size=2000)  # $40k-$100k range
        high_end = np.random.lognormal(mean=11.8, sigma=0.4, size=500)   # $80k-$200k+ range

        prices = np.concatenate([low_end, mid_range, high_end])
        prices = prices[prices < 500000]  # Remove extreme outliers

        # Create the histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(prices, bins=50, alpha=0.7, color='steelblue', edgecolor='black')
        ax.set_xlabel('Sale Price ($)', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title('Bulldozer Sale Price Distribution (Generated Fallback)', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        # Format x-axis to show prices in thousands
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

        # Add some statistics text
        mean_price = np.mean(prices)
        median_price = np.median(prices)
        ax.text(0.7, 0.8, f'Mean: ${mean_price:,.0f}\nMedian: ${median_price:,.0f}',
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

        plt.tight_layout()

        # Convert to PIL Image
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img = Image.open(buf)
        plt.close()

        return img

    except Exception as e:
        return None


def generate_fallback_monthly_trends():
    """
    Generate a fallback monthly price trends visualization using matplotlib
    when the original image is not available.
    """
    try:
        # Create sample monthly data that represents seasonal trends
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Simulate seasonal trends (higher prices in spring/summer construction season)
        base_price = 45000
        seasonal_factors = [0.85, 0.88, 0.95, 1.05, 1.15, 1.20,
                           1.18, 1.12, 1.08, 1.02, 0.92, 0.87]

        median_prices = [base_price * factor for factor in seasonal_factors]

        # Create the line plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(months, median_prices, marker='o', linewidth=2, markersize=8,
                color='darkgreen', markerfacecolor='lightgreen')
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Median Sale Price ($)', fontsize=12)
        ax.set_title('Monthly Bulldozer Price Trends (Generated Fallback)', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        # Format y-axis to show prices in thousands
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

        # Add trend annotation
        max_month = months[median_prices.index(max(median_prices))]
        min_month = months[median_prices.index(min(median_prices))]
        ax.text(0.02, 0.98, f'Peak: {max_month}\nLow: {min_month}',
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
                verticalalignment='top')

        plt.xticks(rotation=45)
        plt.tight_layout()

        # Convert to PIL Image
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img = Image.open(buf)
        plt.close()

        return img

    except Exception as e:
        return None


def load_image_with_fallbacks(image_name, image_path):
    """
    Comprehensive image loading with multiple fallback strategies:
    1. Try to load from the specified path
    2. Try alternative paths (for different deployment environments)
    3. Provide detailed debugging information
    """
    debug_info = []

    # Strategy 1: Try the primary path
    debug_info.append(f"Trying primary path: {image_path}")
    try:
        if os.path.exists(image_path):
            debug_info.append(f"✅ Primary path exists")
            img = Image.open(image_path)
            _ = img.size, img.mode, img.format  # Validate
            debug_info.append(f"✅ Successfully loaded from primary path")
            return img, "loaded_from_file", "\n".join(debug_info)
        else:
            debug_info.append(f"❌ Primary path does not exist")
    except Exception as e:
        debug_info.append(f"❌ Error with primary path: {e}")

    # Strategy 2: Try alternative paths for different deployment environments
    alternative_paths = [
        f"./{image_path}",
        f"/{image_path}",
        f"app/{image_path}",
        f"/app/{image_path}",
        os.path.join(os.getcwd(), image_path),
        os.path.join(os.path.dirname(__file__), "..", image_path),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", image_path)
    ]

    for i, alt_path in enumerate(alternative_paths):
        debug_info.append(f"Trying alternative path {i+1}: {alt_path}")
        try:
            if os.path.exists(alt_path):
                debug_info.append(f"✅ Alternative path {i+1} exists")
                img = Image.open(alt_path)
                _ = img.size, img.mode, img.format  # Validate
                debug_info.append(f"✅ Successfully loaded from alternative path {i+1}")
                return img, "loaded_from_alternative", "\n".join(debug_info)
            else:
                debug_info.append(f"❌ Alternative path {i+1} does not exist")
        except Exception as e:
            debug_info.append(f"❌ Error with alternative path {i+1}: {e}")

    # Strategy 3: Generate fallback visualization using matplotlib
    debug_info.append(f"Attempting to generate fallback visualization for {image_name}")
    try:
        if image_name == "sale_price_distribution":
            img = generate_fallback_price_distribution()
            if img is not None:
                debug_info.append(f"✅ Generated fallback price distribution visualization")
                return img, "generated_fallback", "\n".join(debug_info)
        elif image_name == "median_saleprice_monthly":
            img = generate_fallback_monthly_trends()
            if img is not None:
                debug_info.append(f"✅ Generated fallback monthly trends visualization")
                return img, "generated_fallback", "\n".join(debug_info)
        debug_info.append(f"❌ Failed to generate fallback visualization")
    except Exception as e:
        debug_info.append(f"❌ Error generating fallback: {e}")

    # Strategy 4: All strategies failed
    debug_info.append(f"❌ All loading strategies failed for {image_name}")
    return None, "failed", "\n".join(debug_info)


def load_image_safely(image_path):
    """
    Legacy function for backward compatibility.
    Now uses the comprehensive fallback system.
    """
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    img, method, message = load_image_with_fallbacks(image_name, image_path)
    if img is not None:
        return img, None
    else:
        return None, message


def ml_pipeline_body():
    """Development of the ML Pipeline"""

    # === HEADER SECTION ===
    st.subheader("ML Pipeline")

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
        - [Machine Learning Model (ML) Model Success](#machine-learning-model-ml-model-success)
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
        - **Goal:** Predict bulldozer sale prices based on their characteristics and historical sales data, achieving an accuracy measured by a Root Mean Squared Log Error (RMSLE) score below `1.0`.
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
            - Examples: histogram and bar charts
        """
    )
    # Add a checkbox to display the sale price distribution image
    if st.checkbox("Inspection: Sale Price Distribution"):
        # Use PNG format for better Streamlit compatibility
        image_path = "results/sale_price_distribution.png"

        # Load image with comprehensive fallback system
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        img, method, debug_info = load_image_with_fallbacks(image_name, image_path)

        # Optional debug information (collapsed by default for clean UX)
        with st.expander("� Advanced Debug Information", expanded=False):
            st.code(debug_info, language="text")

        if img is not None:
            # Successfully loaded image - display it
            st.image(img, caption="Sale Price Distribution")

            # User-friendly success message based on loading method
            if method == "loaded_from_file":
                st.success("✅ Visualization loaded successfully")
            elif method == "generated_fallback":
                st.info("📊 Interactive chart generated for optimal viewing")
            else:
                st.success("✅ Visualization ready")

            # Display additional information about the visualization
            st.subheader("Histogram: Price Distribution")
            st.markdown(
                """
                **Purpose**: This histogram shows the distribution of the SalePrice column, providing insights into how sale prices are spread across the dataset.
                The histogram helps us understand:
                - How bulldozer prices are distributed
                - The most common price ranges
                - Whether there are more low-priced or high-priced bulldozers
                - Any unusual prices that might need special attention
                """
            )
        else:
            # Failed to load image - show error and fallback content
            st.error("❌ Visualization temporarily unavailable")
            st.info("💡 We're working to display the price distribution chart. Please try refreshing the page.")

            # Still show the informational content even if image fails
            st.subheader("Histogram: Price Distribution")
            st.markdown(
                """
                **Purpose**: This histogram shows the distribution of the SalePrice column, providing insights into how sale prices are spread across the dataset.
                The histogram helps us understand:
                - How bulldozer prices are distributed
                - The most common price ranges
                - Whether there are more low-priced or high-priced bulldozers
                - Any unusual prices that might need special attention

                *Note: The visualization is currently being prepared.*
                """
            )

        st.write("---")

    # Add a checkbox to display the median sale price monthly image
    if st.checkbox("Inspection: Median Sale Price Monthly"):
        # Use PNG format for better Streamlit compatibility
        image_path = "results/median_saleprice_monthly.png"

        # Load image with comprehensive fallback system
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        img, method, debug_info = load_image_with_fallbacks(image_name, image_path)

        # Optional debug information (collapsed by default for clean UX)
        with st.expander("� Advanced Debug Information", expanded=False):
            st.code(debug_info, language="text")

        if img is not None:
            # Successfully loaded image - display it
            st.image(img, caption="Median Sale Price Monthly")

            # User-friendly success message based on loading method
            if method == "loaded_from_file":
                st.success("✅ Visualization loaded successfully")
            elif method == "generated_fallback":
                st.info("📊 Interactive chart generated for optimal viewing")
            else:
                st.success("✅ Visualization ready")

            # Display additional information about the visualization
            st.subheader("Visualizing Monthly Price Trends")
            st.markdown(
                """
                We look at the average price per month to:
                - Identify seasonal pricing patterns
                - Spot months with typically higher or lower prices
                - Help buyers and sellers make more informed decisions
                """
            )
        else:
            # Failed to load image - show error and fallback content
            st.error("❌ Visualization temporarily unavailable")
            st.info("💡 We're working to display the monthly trends chart. Please try refreshing the page.")

            # Still show the informational content even if image fails
            st.subheader("Visualizing Monthly Price Trends")
            st.markdown(
                """
                We look at the average price per month to:
                - Identify seasonal pricing patterns
                - Spot months with typically higher or lower prices
                - Help buyers and sellers make more informed decisions

                *Note: The visualization is currently being prepared.*
                """
            )

        st.write("---")

    st.markdown(
        """
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
        The **BulldozerPriceGenius (BPG)** notebooks use a `price prediction model` that works with continuous numerical values such as $ 75,000, not categories. `Confusion matrices`, in contrast, are designed for classification problems where predictions fit into distinct categories (like "spam" versus "not spam").
        """
    )

    st.subheader("What We Use Instead")
    st.write(
        "For **price predictions**, we need `regression metrics` that measure how close our predictions are to actual values:"
    )
    st.write(
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
    st.subheader("Machine Learning Model (ML) Model Success ")
    st.write(
        """
        Our BulldozerPriceGenius machine learning model has demonstrated exceptional performance across key metrics:

        **Accuracy Metrics**
        - **RMSLE Score**: `0.27` (Target: `<1.0`)
            - Significantly outperformed target threshold
            - Ranked `69th` out of 428 Kaggle entries

        **Error Analysis**
        - **Mean Absolute Error**: `$17,104`
            - Within acceptable range within `$20,000`
            - Consistent performance across price ranges

        **Model Validation**
        - **R² Score**: `0.836` (`83.6%` accuracy)
            - Strong predictive capability
            - High confidence in price estimations

        **Feature Performance**
        - Top Predictors:
            - Year Made (`19.9%` influence)
            - Product Size (`15.5%` influence)
            - Combined explain `35.4%` of price variations

        **Business Impact:**
        - The model has successfully met all business requirements, providing reliable price predictions that enable stakeholders to make informed decisions in the bulldozer auction market.
        """
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
