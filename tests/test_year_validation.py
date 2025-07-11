"""
Test cases for YearMade and SaleYear logical validation.

This module tests the validation logic that prevents logically impossible
scenarios where YearMade is after SaleYear.
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app_pages'))

try:
    from components.year_made_input import validate_year_made
    from four_interactive_prediction import validate_year_logic
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure the src/components and app_pages directories are in the Python path")


class TestYearLogicValidation:
    """Test cases for YearMade vs SaleYear logical validation."""
    
    def test_valid_year_combinations(self):
        """Test valid combinations where YearMade <= SaleYear."""
        valid_combinations = [
            (2000, 2005),  # Normal case: 5 years old
            (1995, 2010),  # Older equipment: 15 years old
            (2010, 2010),  # Same year (brand new)
            (1980, 2000),  # Very old equipment: 20 years old
        ]
        
        for year_made, sale_year in valid_combinations:
            is_valid, error_msg = validate_year_logic(year_made, sale_year)
            assert is_valid, f"Combination ({year_made}, {sale_year}) should be valid but got error: {error_msg}"
            assert error_msg == "", f"Valid combination should have no error message"
    
    def test_invalid_year_combinations(self):
        """Test invalid combinations where YearMade > SaleYear."""
        invalid_combinations = [
            (2014, 2012),  # The example from the user: 2 years impossible
            (2005, 2000),  # 5 years impossible
            (2010, 2009),  # 1 year impossible
            (2000, 1995),  # 5 years impossible (older sale year)
        ]
        
        for year_made, sale_year in invalid_combinations:
            is_valid, error_msg = validate_year_logic(year_made, sale_year)
            assert not is_valid, f"Combination ({year_made}, {sale_year}) should be invalid"
            assert "cannot be after" in error_msg, f"Error message should explain the logical issue"
            assert str(year_made) in error_msg, f"Error should mention YearMade {year_made}"
            assert str(sale_year) in error_msg, f"Error should mention SaleYear {sale_year}"
    
    def test_none_values(self):
        """Test validation with None values (should be valid)."""
        test_cases = [
            (None, 2005),  # No YearMade
            (2000, None),  # No SaleYear
            (None, None),  # Neither specified
        ]
        
        for year_made, sale_year in test_cases:
            is_valid, error_msg = validate_year_logic(year_made, sale_year)
            assert is_valid, f"None values should be valid: ({year_made}, {sale_year})"
            assert error_msg == "", f"None values should have no error message"
    
    def test_year_made_validation_with_sale_year(self):
        """Test YearMade validation function with sale_year parameter."""
        # Valid case
        is_valid, parsed_value, message = validate_year_made("2000", sale_year=2005)
        assert is_valid, "Valid YearMade with later SaleYear should pass"
        assert parsed_value == 2000, "Should parse correctly"
        
        # Invalid case - YearMade after SaleYear
        is_valid, parsed_value, message = validate_year_made("2014", sale_year=2012)
        assert not is_valid, "YearMade after SaleYear should fail validation"
        assert parsed_value is None, "Invalid input should return None"
        assert "cannot be after" in message, "Error should explain the logical issue"
        
        # Valid case without sale_year
        is_valid, parsed_value, message = validate_year_made("2000")
        assert is_valid, "Valid YearMade without SaleYear should pass"
        assert parsed_value == 2000, "Should parse correctly"
    
    def test_error_message_content(self):
        """Test that error messages are helpful and specific."""
        # Test the specific example from the user
        is_valid, error_msg = validate_year_logic(2014, 2012)
        
        assert not is_valid, "Should be invalid"
        assert "2014" in error_msg, "Should mention YearMade 2014"
        assert "2012" in error_msg, "Should mention SaleYear 2012"
        assert "impossible" in error_msg.lower(), "Should explain why it's impossible"
        assert "fix" in error_msg.lower(), "Should provide guidance on how to fix"
        
        # Check that it mentions the time difference
        assert "2 year" in error_msg, "Should mention the 2-year difference"
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Same year (should be valid)
        is_valid, error_msg = validate_year_logic(2010, 2010)
        assert is_valid, "Same year should be valid (brand new equipment)"
        
        # Large differences (should be valid if YearMade <= SaleYear)
        is_valid, error_msg = validate_year_logic(1980, 2020)
        assert is_valid, "Large age difference should be valid"
        
        # Large differences (should be invalid if YearMade > SaleYear)
        is_valid, error_msg = validate_year_logic(2020, 1980)
        assert not is_valid, "Impossible large difference should be invalid"


def test_integration_example():
    """
    Integration test showing how the validation would work in the real application.
    """
    # Simulate user entering the problematic values from the question
    user_year_made = "2014"
    user_sale_year = 2012
    
    # Step 1: Validate YearMade with SaleYear context
    is_valid, parsed_year_made, year_made_error = validate_year_made(user_year_made, sale_year=user_sale_year)
    
    # Should fail at YearMade validation level
    assert not is_valid, "Should catch the logical error at YearMade validation"
    assert "cannot be after" in year_made_error, "Should explain the logical issue"
    
    # Step 2: If YearMade validation passed, check overall logic
    if is_valid:
        logic_valid, logic_error = validate_year_logic(parsed_year_made, user_sale_year)
        assert not logic_valid, "Should catch at logic validation level"
    
    print("✅ Integration test passed: Invalid year combination properly caught")


if __name__ == "__main__":
    # Run the tests
    test_integration_example()
    
    # Create a test instance and run individual tests
    test_instance = TestYearLogicValidation()
    
    print("Running year logic validation tests...")
    
    try:
        test_instance.test_valid_year_combinations()
        print("✅ Valid year combinations test passed")
        
        test_instance.test_invalid_year_combinations()
        print("✅ Invalid year combinations test passed")
        
        test_instance.test_none_values()
        print("✅ None values test passed")
        
        test_instance.test_year_made_validation_with_sale_year()
        print("✅ YearMade validation with SaleYear test passed")
        
        test_instance.test_error_message_content()
        print("✅ Error message content test passed")
        
        test_instance.test_edge_cases()
        print("✅ Edge cases test passed")
        
        print("\n🎉 All tests passed! The validation logic correctly prevents impossible year combinations.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise
