"""
Test Suite for ModelID Input Component

This module contains comprehensive tests for the ModelID input validation,
preprocessing, and error handling functionality.

Usage:
    pytest tests/test_model_id_input.py -v

Author: BulldozerPriceGenius Team
Date: 2025-07-08
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from components.model_id_input import (
    ModelIDProcessor,
    validate_model_id,
    preprocess_model_id_for_prediction
)


class TestModelIDValidation:
    """Test cases for ModelID input validation."""
    
    def test_valid_integer_inputs(self):
        """Test validation of valid integer inputs."""
        valid_inputs = ["123", "4605", "3538", "1", "99999"]
        
        for input_val in valid_inputs:
            is_valid, parsed_value, error = validate_model_id(input_val)
            assert is_valid, f"Input {input_val} should be valid"
            assert isinstance(parsed_value, int), f"Parsed value should be integer"
            assert error is None, f"No error should be returned for valid input"
    
    def test_invalid_inputs(self):
        """Test validation of invalid inputs."""
        invalid_inputs = [
            ("", "ModelID is required"),
            ("   ", "ModelID is required"),
            ("abc", "Invalid input"),
            ("12.5", "must be a whole number"),
            ("-5", "must be a positive integer"),
            ("0", "must be a positive integer"),
            ("150000", "unusually high"),
        ]
        
        for input_val, expected_error_part in invalid_inputs:
            is_valid, parsed_value, error = validate_model_id(input_val)
            assert not is_valid, f"Input {input_val} should be invalid"
            assert parsed_value is None, f"Parsed value should be None for invalid input"
            assert expected_error_part.lower() in error.lower(), f"Error should contain '{expected_error_part}'"
    
    def test_edge_cases(self):
        """Test edge cases for validation."""
        # Test whitespace handling
        is_valid, parsed_value, error = validate_model_id("  123  ")
        assert is_valid
        assert parsed_value == 123
        
        # Test float that represents integer
        is_valid, parsed_value, error = validate_model_id("123.0")
        assert is_valid
        assert parsed_value == 123
        
        # Test boundary values
        is_valid, parsed_value, error = validate_model_id("1")
        assert is_valid
        assert parsed_value == 1
        
        is_valid, parsed_value, error = validate_model_id("100000")
        assert is_valid
        assert parsed_value == 100000


class TestModelIDProcessor:
    """Test cases for ModelID preprocessing functionality."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample ModelID data for testing."""
        return pd.Series([4605, 3538, 3170, 4604, 3362, 3537, 3171, 4603, 3357, 3178])
    
    @pytest.fixture
    def fitted_processor(self, sample_data):
        """Create a fitted ModelID processor."""
        processor = ModelIDProcessor()
        processor.fit(sample_data)
        return processor
    
    def test_processor_initialization(self):
        """Test ModelID processor initialization."""
        processor = ModelIDProcessor()
        assert not processor.is_fitted
        assert len(processor.known_model_ids) == 0
        assert processor.ordinal_encoder is not None
        assert processor.imputer is not None
    
    def test_processor_fitting(self, sample_data):
        """Test fitting the processor on sample data."""
        processor = ModelIDProcessor()
        fitted_processor = processor.fit(sample_data)
        
        assert fitted_processor.is_fitted
        assert len(fitted_processor.known_model_ids) == len(sample_data.unique())
        assert fitted_processor is processor  # Should return self
    
    def test_transform_known_values(self, fitted_processor, sample_data):
        """Test transformation of known ModelID values."""
        for model_id in sample_data.unique():
            result = fitted_processor.transform(model_id)
            
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
            assert not np.isnan(result[0])  # Should not be NaN for known values
    
    def test_transform_unknown_values(self, fitted_processor):
        """Test transformation of unknown ModelID values."""
        unknown_ids = [99999, 12345, 88888]
        
        for model_id in unknown_ids:
            result = fitted_processor.transform(model_id)
            
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
            # Should handle unknown values gracefully (not necessarily NaN due to imputation)
    
    def test_transform_invalid_inputs(self, fitted_processor):
        """Test transformation of invalid inputs."""
        invalid_inputs = [np.nan, None, "invalid"]
        
        for invalid_input in invalid_inputs:
            # Should not raise exception, should handle gracefully
            result = fitted_processor.transform(invalid_input)
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
    
    def test_transform_before_fitting(self):
        """Test that transform raises error when called before fitting."""
        processor = ModelIDProcessor()
        
        with pytest.raises(ValueError, match="must be fitted"):
            processor.transform(123)
    
    def test_processor_consistency(self, fitted_processor):
        """Test that processor gives consistent results for same input."""
        model_id = 4605
        
        result1 = fitted_processor.transform(model_id)
        result2 = fitted_processor.transform(model_id)
        
        np.testing.assert_array_equal(result1, result2)


class TestPreprocessingIntegration:
    """Test cases for the complete preprocessing pipeline."""
    
    def test_preprocess_with_fitted_processor(self):
        """Test preprocessing with a fitted processor."""
        # Create sample data and fit processor
        sample_data = pd.Series([4605, 3538, 3170, 4604, 3362])
        processor = ModelIDProcessor()
        processor.fit(sample_data)
        
        # Test preprocessing
        model_id = 4605
        processed_array, status = preprocess_model_id_for_prediction(model_id, processor)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert isinstance(status, str)
        assert "seen during training" in status.lower()
    
    def test_preprocess_unknown_model_id(self):
        """Test preprocessing with unknown ModelID."""
        # Create sample data and fit processor
        sample_data = pd.Series([4605, 3538, 3170])
        processor = ModelIDProcessor()
        processor.fit(sample_data)
        
        # Test with unknown ModelID
        unknown_id = 99999
        processed_array, status = preprocess_model_id_for_prediction(unknown_id, processor)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert isinstance(status, str)
        assert "new/unseen" in status.lower()
    
    def test_preprocess_without_processor(self):
        """Test preprocessing without providing a processor (default behavior)."""
        model_id = 4605
        processed_array, status = preprocess_model_id_for_prediction(model_id, None)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert isinstance(status, str)
    
    def test_preprocess_error_handling(self):
        """Test error handling in preprocessing."""
        # Create a processor that will cause errors
        processor = ModelIDProcessor()
        # Don't fit it, so it should cause errors
        
        model_id = 123
        processed_array, status = preprocess_model_id_for_prediction(model_id, processor)
        
        # Should return safe defaults even on error
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert isinstance(status, str)


class TestDataTypeHandling:
    """Test cases for different data type inputs."""
    
    @pytest.fixture
    def fitted_processor(self):
        """Create a fitted processor for testing."""
        sample_data = pd.Series([100, 200, 300, 400, 500])
        processor = ModelIDProcessor()
        processor.fit(sample_data)
        return processor
    
    def test_integer_input(self, fitted_processor):
        """Test processing of integer input."""
        result = fitted_processor.transform(100)
        assert isinstance(result, np.ndarray)
        assert not np.isnan(result[0])
    
    def test_float_input(self, fitted_processor):
        """Test processing of float input that represents integer."""
        result = fitted_processor.transform(100.0)
        assert isinstance(result, np.ndarray)
        assert not np.isnan(result[0])
    
    def test_string_input(self, fitted_processor):
        """Test processing of string input."""
        result = fitted_processor.transform("100")
        assert isinstance(result, np.ndarray)
        # Should handle string conversion gracefully
    
    def test_nan_input(self, fitted_processor):
        """Test processing of NaN input."""
        result = fitted_processor.transform(np.nan)
        assert isinstance(result, np.ndarray)
        # Should handle NaN gracefully through imputation


class TestPerformanceAndMemory:
    """Test cases for performance and memory efficiency."""
    
    def test_large_dataset_fitting(self):
        """Test fitting on a large dataset."""
        # Create large sample dataset
        np.random.seed(42)
        large_data = pd.Series(np.random.randint(1, 10000, size=10000))
        
        processor = ModelIDProcessor()
        fitted_processor = processor.fit(large_data)
        
        assert fitted_processor.is_fitted
        assert len(fitted_processor.known_model_ids) <= 10000  # Should be unique values
    
    def test_batch_transformation(self):
        """Test transforming multiple values efficiently."""
        sample_data = pd.Series([100, 200, 300, 400, 500])
        processor = ModelIDProcessor()
        processor.fit(sample_data)
        
        # Transform multiple values
        test_values = [100, 999, 200, 888, 300]
        results = []
        
        for value in test_values:
            result = processor.transform(value)
            results.append(result)
        
        assert len(results) == len(test_values)
        for result in results:
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
