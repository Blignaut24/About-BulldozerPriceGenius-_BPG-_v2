"""
ModelID Input Component for Bulldozer Price Prediction

This module provides a comprehensive ModelID input field with validation,
preprocessing, and error handling for the bulldozer price prediction web application.

Author: BulldozerPriceGenius Team
Date: 2025-07-08
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from typing import Optional, Tuple, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelIDProcessor:
    """
    Handles ModelID preprocessing for bulldozer price prediction.
    
    This class provides functionality to:
    - Encode ModelID as categorical feature using OrdinalEncoder
    - Handle unseen ModelID values by marking them as NaN
    - Use SimpleImputer to replace NaN values with appropriate defaults
    - Maintain correct feature order in the prediction pipeline
    """
    
    def __init__(self):
        """Initialize the ModelID processor with encoders and imputers."""
        self.ordinal_encoder = OrdinalEncoder(
            handle_unknown='use_encoded_value',
            unknown_value=np.nan,
            encoded_missing_value=-1
        )
        self.imputer = SimpleImputer(
            missing_values=np.nan,
            strategy='most_frequent'
        )
        self.is_fitted = False
        self.known_model_ids = set()
        
    def fit(self, model_ids: pd.Series) -> 'ModelIDProcessor':
        """
        Fit the processor on training ModelID data.
        
        Args:
            model_ids: Series of ModelID values from training data
            
        Returns:
            self: Fitted processor instance
        """
        try:
            # Store known ModelIDs for validation
            self.known_model_ids = set(model_ids.dropna().unique())
            
            # Fit ordinal encoder
            model_ids_reshaped = model_ids.values.reshape(-1, 1)
            self.ordinal_encoder.fit(model_ids_reshaped)
            
            # Fit imputer on encoded values
            encoded_values = self.ordinal_encoder.transform(model_ids_reshaped)
            self.imputer.fit(encoded_values)
            
            self.is_fitted = True
            logger.info(f"ModelID processor fitted on {len(self.known_model_ids)} unique ModelIDs")
            
        except Exception as e:
            logger.error(f"Error fitting ModelID processor: {str(e)}")
            raise
            
        return self
    
    def transform(self, model_id: Union[int, float, str]) -> np.ndarray:
        """
        Transform a single ModelID value for prediction.
        
        Args:
            model_id: ModelID value to transform
            
        Returns:
            Transformed ModelID as numpy array
            
        Raises:
            ValueError: If processor is not fitted or input is invalid
        """
        if not self.is_fitted:
            raise ValueError("ModelID processor must be fitted before transformation")
        
        try:
            # Convert to integer if possible
            if pd.isna(model_id):
                processed_id = np.nan
            else:
                processed_id = int(float(model_id))
            
            # Reshape for sklearn
            model_id_array = np.array([[processed_id]])
            
            # Transform using ordinal encoder
            encoded = self.ordinal_encoder.transform(model_id_array)
            
            # Impute missing values
            imputed = self.imputer.transform(encoded)
            
            return imputed.flatten()
            
        except Exception as e:
            logger.error(f"Error transforming ModelID {model_id}: {str(e)}")
            # Return imputed default value
            default_array = np.array([[np.nan]])
            encoded_default = self.ordinal_encoder.transform(default_array)
            return self.imputer.transform(encoded_default).flatten()


def validate_model_id(model_id_input: str) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Validate ModelID input from user.
    
    Args:
        model_id_input: Raw input string from user
        
    Returns:
        Tuple of (is_valid, parsed_value, error_message)
    """
    if not model_id_input or model_id_input.strip() == "":
        return False, None, "ModelID is required. Please enter a valid integer value."
    
    try:
        # Remove whitespace and convert to float first (handles decimal inputs)
        cleaned_input = model_id_input.strip()
        float_value = float(cleaned_input)
        
        # Check if it's actually an integer
        if not float_value.is_integer():
            return False, None, "ModelID must be a whole number (integer). Decimal values are not allowed."
        
        int_value = int(float_value)
        
        # Check reasonable range based on data analysis
        if int_value < 1:
            return False, None, "ModelID must be a positive integer greater than 0."
        
        if int_value > 100000:  # Conservative upper bound
            return False, None, "ModelID seems unusually high. Please verify the value (should be between 1 and 100,000)."
        
        return True, int_value, None
        
    except ValueError:
        return False, None, "Invalid input. ModelID must be a numeric value (integer only)."
    except Exception as e:
        return False, None, f"Unexpected error validating ModelID: {str(e)}"


def create_model_id_input() -> Optional[int]:
    """
    Create a Streamlit input field for ModelID with validation and help text.
    
    Returns:
        Validated ModelID integer or None if invalid
    """
    # Create the input field
    st.subheader("🔢 ModelID Input")
    
    # Add help information
    with st.expander("ℹ️ About ModelID", expanded=False):
        st.markdown("""
        **What is ModelID?**
        
        ModelID is a unique identifier that represents the specific bulldozer model in our database. 
        This categorical feature is crucial for price prediction as different models have significantly 
        different values based on their:
        
        - **Manufacturing specifications** (engine power, blade size, etc.)
        - **Market demand** and popularity
        - **Production volume** and availability
        - **Feature set** and capabilities
        
        **How it works in prediction:**
        1. Your input ModelID is treated as a categorical feature
        2. It's encoded using OrdinalEncoder for machine learning compatibility
        3. If the ModelID is new/unseen, it's handled gracefully with imputation
        4. The encoded value is used alongside other features for price prediction
        
        **Valid Range:** 1 - 100,000 (based on historical data: 28 - 37,198)
        """)
    
    # Create the input field
    model_id_input = st.text_input(
        label="Enter ModelID",
        placeholder="e.g., 4605, 3538, 3170",
        help="Enter the ModelID as a positive integer. This identifies the specific bulldozer model.",
        key="model_id_input"
    )
    
    # Validate input if provided
    if model_id_input:
        is_valid, parsed_value, error_message = validate_model_id(model_id_input)
        
        if is_valid:
            st.success(f"✅ Valid ModelID: {parsed_value}")
            return parsed_value
        else:
            st.error(f"❌ {error_message}")
            return None
    
    return None


def preprocess_model_id_for_prediction(
    model_id: int, 
    processor: Optional[ModelIDProcessor] = None
) -> Tuple[np.ndarray, str]:
    """
    Preprocess ModelID for model prediction with detailed status information.
    
    Args:
        model_id: Validated ModelID integer
        processor: Fitted ModelIDProcessor instance (optional, will create default if None)
        
    Returns:
        Tuple of (processed_array, status_message)
    """
    try:
        if processor is None:
            # Create a default processor (in real app, this should be loaded from saved model)
            st.warning("⚠️ Using default ModelID processor. In production, this should be loaded from the trained model.")
            processor = ModelIDProcessor()
            # For demo purposes, create a simple fitted processor
            sample_ids = pd.Series([4605, 3538, 3170, 4604, 3362])  # Common ModelIDs from data
            processor.fit(sample_ids)
        
        # Transform the ModelID
        processed_array = processor.transform(model_id)
        
        # Check if ModelID was seen during training
        if model_id in processor.known_model_ids:
            status = f"✅ ModelID {model_id} was seen during training. Using learned encoding."
        else:
            status = f"⚠️ ModelID {model_id} is new/unseen. Applied imputation strategy for robust prediction."
        
        return processed_array, status
        
    except Exception as e:
        error_msg = f"❌ Error preprocessing ModelID: {str(e)}"
        logger.error(error_msg)
        # Return safe default
        return np.array([0.0]), error_msg


# Example usage and testing function
def demo_model_id_component():
    """
    Demonstration function showing how to use the ModelID input component.
    This can be called from a Streamlit app for testing.
    """
    st.title("ModelID Input Component Demo")
    
    # Create the input component
    model_id = create_model_id_input()
    
    if model_id is not None:
        st.write("---")
        st.subheader("🔄 Preprocessing Results")
        
        # Show preprocessing
        processed_array, status = preprocess_model_id_for_prediction(model_id)
        
        st.info(status)
        st.write(f"**Processed Value:** {processed_array[0]:.4f}")
        st.write(f"**Array Shape:** {processed_array.shape}")
        st.write(f"**Data Type:** {processed_array.dtype}")
        
        # Show how it fits in the prediction pipeline
        st.subheader("🔗 Integration with Prediction Pipeline")
        st.code(f"""
# Example of how this integrates with your prediction pipeline:

# 1. Get user input
model_id = {model_id}

# 2. Preprocess ModelID
processed_model_id, status = preprocess_model_id_for_prediction(model_id, fitted_processor)

# 3. Combine with other features for prediction
# features = np.concatenate([other_features, processed_model_id])

# 4. Make prediction
# prediction = trained_model.predict(features.reshape(1, -1))
        """)


if __name__ == "__main__":
    # Run demo if script is executed directly
    demo_model_id_component()
