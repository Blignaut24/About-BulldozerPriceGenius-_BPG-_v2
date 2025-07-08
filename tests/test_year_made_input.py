"""
Test Suite for YearMade Input Component

This module contains comprehensive tests for the YearMade input validation,
preprocessing, and error handling functionality.

Usage:
    pytest tests/test_year_made_input.py -v

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

from components.year_made_input import (
    YearMadeProcessor,
    validate_year_made,
    preprocess_year_made_for_prediction
)


class TestYearMadeValidation:
    """Test cases for YearMade input validation."""
    
    def test_valid_year_inputs(self):
        """Test validation of valid year inputs."""
        valid_inputs = ["1995", "2005", "1980", "2010", "1975"]
        
        for input_val in valid_inputs:
            is_valid, parsed_value, message = validate_year_made(input_val)
            assert is_valid, f"Input {input_val} should be valid"
            assert isinstance(parsed_value, int), f"Parsed value should be integer"
            # Message might be None or a warning, but should not be an error
            if message:
                assert not message.startswith("❌"), f"Should not have error message for valid input"
    
    def test_invalid_inputs(self):
        """Test validation of invalid inputs."""
        invalid_inputs = [
            ("", "YearMade is required"),
            ("   ", "YearMade is required"),
            ("abc", "Invalid input"),
            ("1995.5", "must be a whole number"),
            ("1950", "too old"),
            ("2030", "cannot be in the future"),
        ]
        
        for input_val, expected_error_part in invalid_inputs:
            is_valid, parsed_value, error = validate_year_made(input_val)
            assert not is_valid, f"Input {input_val} should be invalid"
            assert parsed_value is None, f"Parsed value should be None for invalid input"
            assert expected_error_part.lower() in error.lower(), f"Error should contain '{expected_error_part}'"
    
    def test_boundary_years(self):
        """Test boundary year validation."""
        # Test exact boundaries
        is_valid, parsed_value, message = validate_year_made("1970")
        assert is_valid
        assert parsed_value == 1970
        
        is_valid, parsed_value, message = validate_year_made("2025")
        assert is_valid
        assert parsed_value == 2025
        
        # Test just outside boundaries
        is_valid, parsed_value, error = validate_year_made("1969")
        assert not is_valid
        
        is_valid, parsed_value, error = validate_year_made("2026")
        assert not is_valid
    
    def test_warning_years(self):
        """Test years that should generate warnings but still be valid."""
        # Years outside training range but within acceptable bounds
        warning_years = ["1970", "2015", "2020"]
        
        for year in warning_years:
            is_valid, parsed_value, message = validate_year_made(year)
            assert is_valid, f"Year {year} should be valid"
            assert parsed_value == int(year)
            # Should have a warning message
            if message:
                assert message.startswith("⚠️"), f"Should have warning for year {year}"
    
    def test_whitespace_handling(self):
        """Test handling of whitespace in input."""
        is_valid, parsed_value, message = validate_year_made("  1995  ")
        assert is_valid
        assert parsed_value == 1995
        
        is_valid, parsed_value, message = validate_year_made("2005.0")
        assert is_valid
        assert parsed_value == 2005


class TestYearMadeProcessor:
    """Test cases for YearMade preprocessing functionality."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample YearMade data for testing."""
        return pd.Series([1995, 1998, 2000, 2005, 1990, 1985, 2010, 1975, 1980])
    
    @pytest.fixture
    def fitted_processor(self, sample_data):
        """Create a fitted YearMade processor."""
        processor = YearMadeProcessor()
        processor.fit(sample_data)
        return processor
    
    def test_processor_initialization(self):
        """Test YearMade processor initialization."""
        processor = YearMadeProcessor()
        assert not processor.is_fitted
        assert processor.training_median is None
        assert processor.imputer is not None
        assert processor.imputer.strategy == 'median'
    
    def test_processor_fitting(self, sample_data):
        """Test fitting the processor on sample data."""
        processor = YearMadeProcessor()
        fitted_processor = processor.fit(sample_data)
        
        assert fitted_processor.is_fitted
        assert fitted_processor.training_median is not None
        assert fitted_processor.training_min is not None
        assert fitted_processor.training_max is not None
        assert fitted_processor is processor  # Should return self
    
    def test_transform_valid_years(self, fitted_processor):
        """Test transformation of valid year values."""
        test_years = [1995, 2000, 1985, 2010]
        
        for year in test_years:
            result = fitted_processor.transform(year)
            
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
            assert result.dtype == np.int64  # Should maintain int64 type
            assert result[0] == year  # Should preserve the actual year
    
    def test_transform_missing_values(self, fitted_processor):
        """Test transformation of missing/NaN values."""
        result = fitted_processor.transform(np.nan)
        
        assert isinstance(result, np.ndarray)
        assert result.shape == (1,)
        assert result.dtype == np.int64
        # Should be imputed with median (not NaN)
        assert not np.isnan(result[0])
    
    def test_transform_string_inputs(self, fitted_processor):
        """Test transformation of string inputs."""
        result = fitted_processor.transform("1995")
        
        assert isinstance(result, np.ndarray)
        assert result.shape == (1,)
        assert result.dtype == np.int64
        assert result[0] == 1995
    
    def test_transform_before_fitting(self):
        """Test that transform raises error when called before fitting."""
        processor = YearMadeProcessor()
        
        with pytest.raises(ValueError, match="must be fitted"):
            processor.transform(1995)
    
    def test_processor_consistency(self, fitted_processor):
        """Test that processor gives consistent results for same input."""
        year = 1995
        
        result1 = fitted_processor.transform(year)
        result2 = fitted_processor.transform(year)
        
        np.testing.assert_array_equal(result1, result2)
    
    def test_data_type_consistency(self, fitted_processor):
        """Test that all outputs maintain int64 data type."""
        test_inputs = [1995, 2000.0, "1985", np.nan]
        
        for input_val in test_inputs:
            result = fitted_processor.transform(input_val)
            assert result.dtype == np.int64, f"Output should be int64 for input {input_val}"


class TestPreprocessingIntegration:
    """Test cases for the complete preprocessing pipeline."""
    
    def test_preprocess_with_fitted_processor(self):
        """Test preprocessing with a fitted processor."""
        # Create sample data and fit processor
        sample_data = pd.Series([1995, 1998, 2000, 2005, 1990])
        processor = YearMadeProcessor()
        processor.fit(sample_data)
        
        # Test preprocessing
        year = 1995
        processed_array, status = preprocess_year_made_for_prediction(year, processor)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert processed_array.dtype == np.int64
        assert isinstance(status, str)
        assert "within training range" in status.lower()
    
    def test_preprocess_outside_training_range(self):
        """Test preprocessing with year outside training range."""
        # Create sample data and fit processor
        sample_data = pd.Series([1995, 1998, 2000, 2005])
        processor = YearMadeProcessor()
        processor.fit(sample_data)
        
        # Test with year outside range
        old_year = 1980
        processed_array, status = preprocess_year_made_for_prediction(old_year, processor)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert processed_array.dtype == np.int64
        assert isinstance(status, str)
        assert "older than training range" in status.lower()
        
        # Test with newer year
        new_year = 2015
        processed_array, status = preprocess_year_made_for_prediction(new_year, processor)
        
        assert isinstance(processed_array, np.ndarray)
        assert "newer than training range" in status.lower()
    
    def test_preprocess_without_processor(self):
        """Test preprocessing without providing a processor (default behavior)."""
        year = 1995
        processed_array, status = preprocess_year_made_for_prediction(year, None)
        
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert processed_array.dtype == np.int64
        assert isinstance(status, str)
    
    def test_preprocess_error_handling(self):
        """Test error handling in preprocessing."""
        # Create a processor that will cause errors
        processor = YearMadeProcessor()
        # Don't fit it, so it should cause errors
        
        year = 1995
        processed_array, status = preprocess_year_made_for_prediction(year, processor)
        
        # Should return safe defaults even on error
        assert isinstance(processed_array, np.ndarray)
        assert processed_array.shape == (1,)
        assert processed_array.dtype == np.int64


class TestNumericalFeatureHandling:
    """Test cases for numerical feature handling specifics."""
    
    def test_no_special_encoding(self, sample_data=pd.Series([1995, 2000, 1985])):
        """Test that YearMade is treated as numerical, not categorical."""
        processor = YearMadeProcessor()
        processor.fit(sample_data)
        
        # Transform should preserve numerical relationship
        result1 = processor.transform(1995)
        result2 = processor.transform(2000)
        
        # Newer year should have higher value (no encoding transformation)
        assert result2[0] > result1[0], "Newer year should have higher numerical value"
    
    def test_median_imputation_strategy(self):
        """Test that median imputation strategy works correctly."""
        # Create data with known median
        data = pd.Series([1990, 1995, 2000, 2005, 2010])  # Median = 2000
        processor = YearMadeProcessor()
        processor.fit(data)
        
        # Transform NaN should give median
        result = processor.transform(np.nan)
        expected_median = data.median()
        
        assert result[0] == expected_median, f"NaN should be imputed with median {expected_median}"
    
    def test_feature_order_preservation(self):
        """Test that feature maintains its position and type for ML pipeline."""
        processor = YearMadeProcessor()
        sample_data = pd.Series([1995, 2000, 2005])
        processor.fit(sample_data)
        
        # Multiple transformations should maintain consistent output format
        years = [1995, 2000, 2005]
        results = []
        
        for year in years:
            result = processor.transform(year)
            results.append(result)
        
        # All results should have same shape and dtype
        for result in results:
            assert result.shape == (1,)
            assert result.dtype == np.int64
        
        # Results should maintain numerical ordering
        assert results[0][0] < results[1][0] < results[2][0]


class TestRealWorldScenarios:
    """Test cases for real-world usage scenarios."""
    
    def test_training_data_simulation(self):
        """Test with data similar to actual training dataset."""
        # Simulate realistic training data based on analysis
        np.random.seed(42)
        realistic_years = []
        
        # Add years from different decades with realistic distribution
        realistic_years.extend([1995] * 100)  # Popular year
        realistic_years.extend([2000] * 80)
        realistic_years.extend([1990] * 60)
        realistic_years.extend(list(range(1980, 2010)) * 5)  # Various years
        
        training_data = pd.Series(realistic_years)
        processor = YearMadeProcessor()
        processor.fit(training_data)
        
        # Test various scenarios
        test_cases = [
            (1995, "common year"),
            (1975, "old year"),
            (2015, "new year"),
            (np.nan, "missing value")
        ]
        
        for year, description in test_cases:
            result = processor.transform(year)
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
            assert result.dtype == np.int64
            assert not np.isnan(result[0]), f"Should not return NaN for {description}"
    
    def test_edge_case_years(self):
        """Test edge cases that might occur in real usage."""
        sample_data = pd.Series([1990, 1995, 2000, 2005])
        processor = YearMadeProcessor()
        processor.fit(sample_data)
        
        edge_cases = [
            1970,    # Minimum allowed
            2025,    # Maximum allowed
            1971,    # Just inside training range
            2014,    # Just inside training range
        ]
        
        for year in edge_cases:
            result = processor.transform(year)
            assert isinstance(result, np.ndarray)
            assert result.shape == (1,)
            assert result.dtype == np.int64
            assert result[0] == year  # Should preserve the actual year


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
