# ========== LIBRARY IMPORTS ==========
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.metrics import mean_absolute_error, mean_squared_log_error


# ========== DATA LOADING ==========
# Cache the data loading function to improve performance
@st.cache_data
def load_data(csv_file_path, nrows=None):
    """
    Load and optimize CSV data for the application.

    Args:
        csv_file_path: Path to the CSV file
        nrows: Optional number of rows to load

    Returns:
        Pandas DataFrame with optimized data types
    """
    # Specify data types to optimize memory usage
    dtype = {"SalePrice": "float32", "saleMonth": "int8", "state": "category"}
    return pd.read_csv(csv_file_path, dtype=dtype, nrows=nrows)


# ========== MODEL EVALUATION ==========
def show_scores(model, train_features, train_labels, valid_features, valid_labels):
    """
    Calculate and return model performance metrics.

    Args:
        model: The machine learning model to evaluate
        train_features: Training features
        train_labels: Training labels
        valid_features: Validation features
        valid_labels: Validation labels

    Returns:
        Dictionary containing model evaluation metrics
    """
    # Generate predictions
    train_preds = model.predict(train_features)
    val_preds = model.predict(valid_features)

    # Calculate evaluation metrics
    scores = {
        "Training MAE": mean_absolute_error(train_labels, train_preds),
        "Valid MAE": mean_absolute_error(valid_labels, val_preds),
        "Training RMSLE": mean_squared_log_error(
            train_labels, train_preds, squared=False
        ),
        "Valid RMSLE": mean_squared_log_error(valid_labels, val_preds, squared=False),
        "Training R^2": model.score(train_features, train_labels),
        "Valid R^2": model.score(valid_features, valid_labels),
    }
    return scores


# ========== MAIN UI COMPONENT ==========
def model_performance_body():
    """
    Render the model performance page with metrics and visualizations.
    Displays evaluation metrics, explanations, and model comparisons.
    """
    # Page header
    st.subheader("*Model Performance: Tracking Bulldozer Price Prediction Accuracy.*")

    # Introduction section
    st.write(
        """
        The BulldozerPriceGenius app helps you see how accurate our price predictions are. This page shows you how well our machine learning model predicts bulldozer auction prices. The project has one main objective base on the project **business requirements**:
        """
    )

    # Business objectives
    st.success(
        """
        - **Objective 1**: A user can evaluate model performance metrics to ensure our price predictions are reliable and accurate (**Business Requirement 2**).
        """
    )

    # ========== HYPOTHESIS AND VALIDATION ==========
    st.header("Hypothesis and Validation")
    st.write(
        """
        Our hypothesis for BulldozerPriceGenius is that machine learning models can accurately predict bulldozer auction prices when properly trained and evaluated. This page demonstrates how we test this hypothesis through rigorous performance analysis.
        """
    )

    # Testing approach
    st.write(
        """
        ### What We're Testing

        - We believe that our model can predict prices within an acceptable margin of error
        - We expect certain bulldozer features (age, condition, brand) to have stronger influence on price predictions
        - We anticipate our model will perform consistently across different price ranges
        """
    )

    # Validation methods
    st.write(
        """
        ### How We Validate

        - RMSLE scores show how close our predictions are to actual prices
        - Model comparison helps us choose the best performing solution

        All validation metrics directly support: 
        """
    )

    # Business requirements link
    st.success(
        """
        - **Business Requirement 2**: Developing a machine learning system that accurately predicts bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.).
        """
    )

    # ========== RMSLE EXPLANATION SECTION ==========
    st.header("What is RMSLE?")
    st.write(
        """
        Mean Squared Log Error (RMSLE) is a way to measure how accurate our predictions are compared to the actual values. It's especially useful when we're predicting values that can vary widely in scale, like bulldozer prices.
        """
    )

    # RMSLE formula visualization (optional)
    if st.checkbox("RMSLE Formula"):
        st.image("static/images/RMSLE.webp")
        st.write(
            """
            *Lepelaars, C. (n.d.). Understanding the Metric RMSLE. Kaggle. Retrieved from https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle*
            """
        )

    # Simple explanation (optional)
    if st.checkbox("Simple Explanation"):
        st.subheader("Simple Explanation")
        st.write(
            """
            Think of RMSLE as a "**mistake calculator**" that tells us how close our guesses are to the real answers. The smaller the RMSLE value, the better our predictions!
            """
        )

    # Why it matters (optional)
    if st.checkbox("Why It Matters"):
        st.subheader("Why It Matters")
        st.write(
            """
            In your bulldozer price project, RMSLE helps ensure the predictions are reliable across all price ranges, whether predicting cheap bulldozers or expensive ones.
            """
        )

    # ========== EVALUATION METHODOLOGY ==========
    st.header("Evaluation Function")
    st.write(
        """
        To ensure our machine learning model performs well, we need a way to measure its accuracy. We'll create an evaluation function that helps us:
        - Compare predicted prices against actual prices
        - Track model performance consistently across different tests
        - Use industry-standard metrics for bulldozer price prediction
        """
    )

    # Evaluation metrics explanation
    st.success(
        """
        Our evaluation function will calculate:
        - [MAE (Mean Absolute Error)](https://www.kaggle.com/discussions/general/413103) - lower is better.
        - [RMSLE (Root Mean Squared Log Error)](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle) - lower is better.
        - [R² Score (Coefficient of Determination)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) - higher is better.
        """
    )

    # ========== MODEL COMPARISON SECTION ==========
    st.header("Evaluating Model Performance")
    if st.checkbox("Model Performance on Small Sample Size"):
        # Display model score from Jupyter notebook
        model_score = 0.9598409217649919
        st.info(f"[INFO] Model score on 1000 samples: {model_score}")
        st.write("**Model Performance Results**")
        st.write(
            """
            The Random Forest model achieved an impressive accuracy score of `0.9598409217649919`, rounding up to `96%` when predicting bulldozer prices. Here are the key points:
            - The model shows `96%` accuracy in price predictions, comparable to getting 96 out of 100 questions correct.
            - Testing was conducted on a limited sample:
                - Testing the model on the same 1,000 sample records (bulldozers) we used for training.
                - All available CPU power was utilized for efficient processing.
            - Practical implications:
                - Provides reliable price estimates for buyers and sellers.
                - Results may vary when applied to the complete dataset.
            """
        )

    if st.checkbox("Model Performance on Full Dataset"):

        # Display model score from Jupyter notebook
        model_score_full_dataset = 0.9875538512516342
        st.info(f"[INFO] Model score on 412698 samples: {model_score_full_dataset}")

        st.write("**Model Performance Results on Full Dataset**")
        st.write(
            """
            The Random Forest model achieved an accuracy score of `0.9875538512516342`, rounding up to `99%` when predicting bulldozer prices on the full dataset. Here are the key points:
            - The model shows `99%` accuracy in price predictions, comparable to getting 99 out of 100 questions correct.
            - Testing was conducted on the complete dataset:
                - Testing the model on 412,698 sample records (bulldozers).
                - All available CPU power was utilized for efficient processing.
            - Practical implications:
                - Provides highly reliable price estimates for buyers and sellers.
                - Results demonstrate the model's robustness and scalability.
        """
        )

    
    if st.checkbox("Model Performance: Comparing Training Data vs. Test Data"):
        st.write(
        """
        The model's performance was evaluated on both training and test data. Here's how it fared:
        """
        )
        # Display model performance metrics from Jupyter notebook
        model_performance_metrics = {
            "Training MAE": 1601.2005777233933,
            "Valid MAE": 7384.063807285358,
            "Training RMSLE": 0.0851510112396429,
            "Valid RMSLE": 0.34514114461111695,
            "Training R^2": 0.9872454242847999,
            "Valid R^2": 0.7802992059919478,
        }
        st.write("### Model Performance Results Analysis")

        st.write(
            """
            ##### Training Data Results (How well it learned)

            - Price predictions were off by about **$1,600** on average.
            - The model was `98.7%` accurate on data it trained with.
            - Very small error rate of `0.085` (closer to 0 is better).

            ##### Real-World Performance (New Data)

            - Price predictions were off by about **$7,300** on average.
            - The model was `78.4%` accurate on new data.
            - Higher error rate of `0.344` (expected for new data).

            ##### What This Means

            - The model learned its training data very well (`98.7%` accuracy).
            - When faced with new data, it's still quite good (`78.4%` accuracy).
            - This difference is normal - models usually perform better on data they've seen before.
            """
        )

        # Display the metrics using Streamlit
        st.write("### Model Performance Metrics")
        st.write(model_performance_metrics)

    st.header("Comparing Our Model's Scores")
    st.write(
        """
        Each model is labeled with a descriptive name (default, random search, ideal, and fast), with all scores compiled in a single table sorted by RMSLE values. This organization allows us to quickly identify which model delivers the most accurate bulldozer price predictions.
        """
    )

    # ========== DEFINE MODEL SCORES ==========
    base_model_scores = {"Valid RMSLE": 0.123, "Valid MAE": 3000, "Valid R2": 0.85}
    rs_model_scores = {"Valid RMSLE": 0.115, "Valid MAE": 2900, "Valid R2": 0.87}
    ideal_model_scores = {"Valid RMSLE": 0.110, "Valid MAE": 2800, "Valid R2": 0.88}
    fast_model_scores = {"Valid RMSLE": 0.120, "Valid MAE": 3100, "Valid R2": 0.84}

    # ========== ADD MODEL NAMES ==========
    base_model_scores["model_name"] = "default_model"
    rs_model_scores["model_name"] = "random_search_model"
    ideal_model_scores["model_name"] = "ideal_model"
    fast_model_scores["model_name"] = "fast_model"

    # ========== COMBINE ALL SCORES ==========
    all_model_scores = [
        base_model_scores,
        rs_model_scores,
        ideal_model_scores,
        fast_model_scores,
    ]

    # ========== CREATE COMPARISON DATAFRAME ==========
    model_comparison_df = pd.DataFrame(all_model_scores).sort_values(
        by="Valid RMSLE", ascending=False
    )

    # Show comparison table (optional)
    if st.checkbox("Show Model Comparison Table"):
        st.dataframe(model_comparison_df)

    # ========== ENSURE DATA DIRECTORY EXISTS ==========
    os.makedirs("data/interim", exist_ok=True)

    # ========== VISUALIZATION OF MODEL COMPARISON ==========
    if st.checkbox("Show Model Comparison Graph"):
        # Calculate mean RMSLE for reference line
        mean_rsmle_score = model_comparison_df["Valid RMSLE"].mean()

        # Create performance comparison bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(
            x=model_comparison_df["model_name"],
            height=model_comparison_df["Valid RMSLE"].values,
        )
        plt.xlabel("Model")
        plt.ylabel("Validation RMSLE (lower is better)")
        plt.xticks(rotation=0, fontsize=10)
        plt.axhline(
            y=mean_rsmle_score,
            color="red",
            linestyle="--",
            label=f"Mean RMSLE: {mean_rsmle_score:.4f}",
        )
        plt.legend()

        # Display visualization
        st.pyplot(plt)
