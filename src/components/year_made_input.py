"""
YearMade Input Component for Bulldozer Price Prediction

This module provides a comprehensive YearMade input field with validation,
preprocessing, and error handling for the bulldozer price prediction web application.

YearMade is the most important feature for predicting bulldozer prices because:
- Newer bulldozers generally have higher values due to less depreciation
- Technology improvements over time affect performance and desirability
- Market demand varies significantly based on equipment age
- Maintenance costs and reliability correlate strongly with manufacturing year

Author: BulldozerPriceGenius Team
Date: 2025-07-08
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from typing import Optional, Tuple, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Streamlit expander compatibility layer
def get_expander_function():
    """Get the appropriate expander function based on Streamlit version."""
    if hasattr(st, 'expander'):
        return st.expander
    elif hasattr(st, 'beta_expander'):
        return st.beta_expander
    else:
        # Fallback for older versions
        def fallback_expander(label, expanded=False):
            from contextlib import contextmanager
            clean_label = label.replace("*", "").strip()
            show_content = st.checkbox(f"Show: {clean_label}", value=expanded)

            @contextmanager
            def expander_context():
                if show_content:
                    st.markdown("---")
                    yield
                    st.markdown("---")
                else:
                    class DummyContext:
                        def __enter__(self):
                            return self
                        def __exit__(self, *args):
                            pass
                    yield DummyContext()

            return expander_context()

        return fallback_expander

# Streamlit text_input compatibility layer for placeholder parameter
def get_text_input_with_placeholder(label, placeholder=None, help=None, key=None, value=""):
    """
    Get text_input with placeholder support, falling back gracefully for older Streamlit versions.

    Handles Quick Fill button integration by converting session state integer values to strings.

    The placeholder parameter was added in Streamlit 0.87.0. For older versions,
    we'll include the placeholder text in the help parameter instead.
    """
    # Handle Quick Fill button integration - convert session state integer values to strings
    if key and key in st.session_state:
        session_value = st.session_state[key]
        if isinstance(session_value, (int, float)):
            # Convert numeric values from Quick Fill buttons to strings
            value = str(int(session_value))  # Convert to int first to remove decimals, then to string
        elif session_value is not None:
            # Ensure other non-None values are strings
            value = str(session_value)

    # Ensure value is always a string to prevent TypeError
    if value is None:
        value = ""
    elif not isinstance(value, str):
        value = str(value)

    try:
        # Try to use placeholder parameter (Streamlit >= 0.87.0)
        if placeholder is not None:
            return st.text_input(
                label=label,
                placeholder=placeholder,
                help=help,
                key=key,
                value=value
            )
        else:
            return st.text_input(
                label=label,
                help=help,
                key=key,
                value=value
            )
    except TypeError as e:
        if "placeholder" in str(e):
            # Fallback for older Streamlit versions - combine placeholder with help text
            combined_help = help
            if placeholder and help:
                combined_help = f"{help}\n\nExample: {placeholder}"
            elif placeholder:
                combined_help = f"Example: {placeholder}"

            return st.text_input(
                label=label,
                help=combined_help,
                key=key,
                value=value
            )
        elif "bad argument type for built-in operation" in str(e):
            # Handle the specific error from Quick Fill buttons
            st.error(f"❌ Input error: Expected text input but received {type(value).__name__}: {value}")
            st.info("🔄 Using fallback input method...")
            # Return empty string to prevent crash
            return st.text_input(
                label=label,
                help=help,
                key=f"{key}_fallback" if key else None,
                value=""
            )
        else:
            # Re-raise if it's a different TypeError
            raise

expander = get_expander_function()
logger = logging.getLogger(__name__)


class YearMadeProcessor:
    """
    Handles YearMade preprocessing for bulldozer price prediction.
    
    YearMade is treated as a standard numerical feature because:
    - It has a natural ordering (older to newer)
    - The numerical relationship is meaningful for ML algorithms
    - No special encoding is needed unlike categorical features
    - Direct correlation with price makes numerical treatment optimal
    """
    
    def __init__(self):
        """Initialize the YearMade processor with imputer for missing values."""
        # Use median strategy as it's robust to outliers and represents typical year
        self.imputer = SimpleImputer(
            missing_values=np.nan,
            strategy='median'
        )
        self.is_fitted = False
        self.training_median = None
        self.training_min = None
        self.training_max = None
        
    def fit(self, year_made_data: pd.Series) -> 'YearMadeProcessor':
        """
        Fit the processor on training YearMade data.
        
        Args:
            year_made_data: Series of YearMade values from training data
            
        Returns:
            self: Fitted processor instance
        """
        try:
            # Store training statistics for validation
            valid_years = year_made_data[year_made_data > 1970]  # Filter placeholder values
            self.training_median = valid_years.median()
            self.training_min = valid_years.min()
            self.training_max = valid_years.max()
            
            # Fit imputer on all data (including placeholders for consistency)
            year_data_reshaped = year_made_data.values.reshape(-1, 1)
            self.imputer.fit(year_data_reshaped)
            
            self.is_fitted = True
            logger.info(f"YearMade processor fitted. Range: {self.training_min}-{self.training_max}, Median: {self.training_median}")
            
        except Exception as e:
            logger.error(f"Error fitting YearMade processor: {str(e)}")
            raise
            
        return self
    
    def transform(self, year_made: Union[int, float, str]) -> np.ndarray:
        """
        Transform a single YearMade value for prediction.
        
        Args:
            year_made: YearMade value to transform
            
        Returns:
            Transformed YearMade as numpy array with consistent int64 dtype
            
        Raises:
            ValueError: If processor is not fitted
        """
        if not self.is_fitted:
            raise ValueError("YearMade processor must be fitted before transformation")
        
        try:
            # Convert to integer if possible, handle missing values
            if pd.isna(year_made):
                processed_year = np.nan
            else:
                processed_year = int(float(year_made))
            
            # Reshape for sklearn and ensure consistent data type
            year_array = np.array([[processed_year]], dtype=np.float64)
            
            # Apply imputation if needed
            imputed = self.imputer.transform(year_array)
            
            # Convert back to int64 for consistency with training data
            # This ensures feature order and data types match the trained model
            result = imputed.astype(np.int64).flatten()
            
            return result
            
        except Exception as e:
            logger.error(f"Error transforming YearMade {year_made}: {str(e)}")
            # Return median as safe fallback
            if self.training_median:
                return np.array([int(self.training_median)], dtype=np.int64)
            else:
                return np.array([1995], dtype=np.int64)  # Safe default based on data analysis


def validate_year_made(year_input: str, sale_year: Optional[int] = None) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Validate YearMade input from user with comprehensive error checking.

    Args:
        year_input: Raw input string from user
        sale_year: Optional sale year for logical validation

    Returns:
        Tuple of (is_valid, parsed_value, error_message)
    """
    if not year_input or year_input.strip() == "":
        return False, None, "YearMade is required. Please enter the year the bulldozer was manufactured."
    
    try:
        # Remove whitespace and convert to float first (handles decimal inputs)
        cleaned_input = year_input.strip()
        float_value = float(cleaned_input)
        
        # Check if it's actually an integer
        if not float_value.is_integer():
            return False, None, "YearMade must be a whole number (year). Decimal values are not allowed."
        
        int_value = int(float_value)
        
        # Validate against extended training data range (1974-2018 to support Test Scenarios 8-12)
        # Updated range to support all test scenarios including ultra-modern equipment
        if int_value < 1974:
            return False, None, "Only years between 1974-2018 are accepted for YearMade input. Please enter a year within this range for accurate predictions."

        if int_value > 2018:
            return False, None, "Only years between 1974-2018 are accepted for YearMade input. Please enter a year within this range for accurate predictions."

        # Check logical relationship with sale year if provided
        if sale_year and int_value > sale_year:
            years_diff = int_value - sale_year
            return False, None, (
                f"YearMade ({int_value}) cannot be after Sale Year ({sale_year}). "
                f"Equipment cannot be sold {years_diff} year{'s' if years_diff > 1 else ''} "
                f"before it was manufactured. Please enter a year {sale_year} or earlier."
            )

        # All years within 1974-2018 are valid with no warnings
        warning_message = None

        return True, int_value, warning_message
        
    except ValueError:
        return False, None, "Invalid input. YearMade must be a numeric year (e.g., 1995, 2005)."
    except Exception as e:
        return False, None, f"Unexpected error validating YearMade: {str(e)}"


def create_year_made_input(sale_year: Optional[int] = None) -> Optional[int]:
    """
    Create a Streamlit input field for YearMade with validation and help text.

    Args:
        sale_year: Optional sale year for logical validation

    Returns:
        Validated YearMade integer or None if invalid
    """
    # Create the input field
    st.subheader("📅 YearMade Input")
    
    # Add help information explaining importance
    with expander("ℹ️ About YearMade - Most Important Feature", expanded=False):
        st.markdown("""
        **Why YearMade is the Most Important Feature for Price Prediction:**
        
        YearMade has the strongest influence on bulldozer prices because:
        
        - **Depreciation**: Newer bulldozers retain higher values due to less wear and tear
        - **Technology Advancement**: Later models often have improved engines, hydraulics, and controls
        - **Market Demand**: Buyers prefer newer equipment for reliability and efficiency
        - **Maintenance Costs**: Older bulldozers typically require more expensive repairs
        - **Regulatory Compliance**: Newer models meet current emission and safety standards
        
        **Data Insights from Training Set:**
        - **Accepted Range**: 1971 - 2014 (only years in this range are accepted)
        - **Most Common Years**: 1990s and 2000s models
        - **Price Correlation**: Strong positive correlation (0.19) with sale price
        - **Median Year**: 1996 (typical bulldozer in dataset)
        
        **How it's processed:**
        1. Treated as numerical feature (no special encoding needed)
        2. Missing values imputed with median strategy
        3. Maintains int64 data type for consistency
        4. Preserves natural ordering relationship with price
        """)
    
    # CRITICAL FIX: Get session state value and convert to string to prevent TypeError
    session_value = st.session_state.get("year_made_input")
    default_value = ""

    if session_value is not None:
        if isinstance(session_value, (int, float)):
            # Convert numeric values from Quick Fill buttons to strings
            default_value = str(int(session_value))  # Convert to int first to remove decimals, then to string
        else:
            # Ensure other non-None values are strings
            default_value = str(session_value)

    # Create the input field using compatibility function
    year_input = get_text_input_with_placeholder(
        label="Enter Year Made (1974-2018)",
        placeholder="e.g., 1995, 2005, 2010, 2018",
        help="Enter the year the bulldozer was manufactured (1974-2018). This is the most important factor in price prediction. Supports all test scenarios including ultra-modern equipment.",
        key="year_made_input",
        value=default_value
    )
    
    # Validate input if provided
    if year_input:
        is_valid, parsed_value, message = validate_year_made(year_input, sale_year)
        
        if is_valid:
            if message and message.startswith("⚠️"):
                # Show warning but still accept the value
                st.warning(message)
                st.success(f"✅ Valid YearMade: {parsed_value}")
            else:
                st.success(f"✅ Valid YearMade: {parsed_value}")
            return parsed_value
        else:
            st.error(f"❌ {message}")
            return None
    
    return None


def preprocess_year_made_for_prediction(
    year_made: int, 
    processor: Optional[YearMadeProcessor] = None
) -> Tuple[np.ndarray, str]:
    """
    Preprocess YearMade for model prediction with detailed status information.
    
    Args:
        year_made: Validated YearMade integer
        processor: Fitted YearMadeProcessor instance (optional)
        
    Returns:
        Tuple of (processed_array, status_message)
    """
    try:
        if processor is None:
            # Create a default processor (in real app, this should be loaded from saved model)
            st.warning("⚠️ Using default YearMade processor. In production, this should be loaded from the trained model.")
            processor = YearMadeProcessor()
            # For demo purposes, create a simple fitted processor
            sample_years = pd.Series([1995, 1998, 2000, 2005, 1990, 1985, 2010])
            processor.fit(sample_years)
        
        # Transform the YearMade
        processed_array = processor.transform(year_made)
        
        # Generate status message based on year and training range
        if processor.training_min and processor.training_max:
            if processor.training_min <= year_made <= processor.training_max:
                status = f"✅ YearMade {year_made} is within training range ({processor.training_min}-{processor.training_max}). High prediction confidence."
            elif year_made < processor.training_min:
                status = f"⚠️ YearMade {year_made} is older than training range ({processor.training_min}-{processor.training_max}). Prediction may be less accurate."
            else:
                status = f"⚠️ YearMade {year_made} is newer than training range ({processor.training_min}-{processor.training_max}). Prediction may be less accurate."
        else:
            status = f"✅ YearMade {year_made} processed successfully. Using median imputation strategy."
        
        return processed_array, status
        
    except Exception as e:
        error_msg = f"❌ Error preprocessing YearMade: {str(e)}"
        logger.error(error_msg)
        # Return safe default (median year from analysis)
        return np.array([1996], dtype=np.int64), error_msg


# Example usage and testing function
def demo_year_made_component():
    """
    Demonstration function showing how to use the YearMade input component.
    This can be called from a Streamlit app for testing.
    """
    st.title("YearMade Input Component Demo")
    
    # Create the input component
    year_made = create_year_made_input()
    
    if year_made is not None:
        st.write("---")
        st.subheader("🔄 Preprocessing Results")
        
        # Show preprocessing
        processed_array, status = preprocess_year_made_for_prediction(year_made)
        
        st.info(status)
        st.write(f"**Original Value:** {year_made}")
        st.write(f"**Processed Value:** {processed_array[0]}")
        st.write(f"**Data Type:** {processed_array.dtype}")
        st.write(f"**Array Shape:** {processed_array.shape}")
        
        # Show feature importance explanation
        st.subheader("🎯 Why YearMade Matters")
        
        # Calculate approximate age and show impact
        current_year = 2025
        age = current_year - year_made
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Equipment Age", f"{age} years")
        with col2:
            # Rough depreciation estimate (10% per year for first 10 years, 5% after)
            if age <= 10:
                depreciation = min(age * 10, 100)
            else:
                depreciation = min(100 + (age - 10) * 5, 80)
            st.metric("Est. Depreciation", f"{depreciation}%")
        with col3:
            # Technology era classification
            if year_made >= 2010:
                era = "Modern"
            elif year_made >= 2000:
                era = "Recent"
            elif year_made >= 1990:
                era = "Mature"
            else:
                era = "Vintage"
            st.metric("Technology Era", era)
        
        # Show integration example
        st.subheader("🔗 Integration with Prediction Pipeline")
        st.code(f"""
# Example of how YearMade integrates with your prediction pipeline:

# 1. Get user input
year_made = {year_made}

# 2. Preprocess YearMade (maintains numerical nature)
processed_year, status = preprocess_year_made_for_prediction(year_made, fitted_processor)
# Result: {processed_array}

# 3. Combine with other features for prediction
# Note: YearMade maintains its position in the feature vector
# features = np.array([processed_year[0], other_feature1, other_feature2, ...])

# 4. Make prediction
# prediction = trained_model.predict(features.reshape(1, -1))

# Key points:
# - No special encoding needed (unlike categorical features)
# - Maintains int64 data type for consistency
# - Natural ordering preserved for ML algorithms
# - Feature order is critical for model compatibility
        """)


if __name__ == "__main__":
    # Run demo if script is executed directly
    demo_year_made_component()
