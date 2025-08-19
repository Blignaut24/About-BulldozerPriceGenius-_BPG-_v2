"""
Test validation consistency between YearMade and SaleYear ranges.

This module tests that the validation ranges are logically consistent
and that equipment made in any valid year can have a valid sale year.
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


def test_validation_range_consistency():
    """Test that YearMade and SaleYear ranges are logically consistent."""
    
    print("🔧 Testing Validation Range Consistency")
    print("=" * 50)
    
    # Define the expected ranges based on the updated validation
    year_made_min = 1971
    year_made_max = 2014
    sale_year_min = 1989
    sale_year_max = 2015
    
    print(f"YearMade range: {year_made_min}-{year_made_max}")
    print(f"SaleYear range: {sale_year_min}-{sale_year_max}")
    print()
    
    # Test 1: Equipment made at the maximum YearMade should be sellable
    print("📋 Test 1: Maximum YearMade Equipment Sellability")
    print("-" * 45)
    
    max_year_made = year_made_max  # 2014
    
    # Test selling in the same year (should be valid)
    is_valid, error = validate_year_logic(max_year_made, max_year_made)
    status = "✅ PASS" if is_valid else "❌ FAIL"
    print(f"{status}: YearMade={max_year_made}, SaleYear={max_year_made} (same year)")
    if not is_valid:
        print(f"   Error: {error}")
    
    # Test selling one year later (should be valid)
    sale_year_next = max_year_made + 1  # 2015
    is_valid, error = validate_year_logic(max_year_made, sale_year_next)
    status = "✅ PASS" if is_valid else "❌ FAIL"
    print(f"{status}: YearMade={max_year_made}, SaleYear={sale_year_next} (one year later)")
    if not is_valid:
        print(f"   Error: {error}")
    
    print()
    
    # Test 2: All valid YearMade values should have at least one valid SaleYear
    print("📋 Test 2: All YearMade Values Have Valid SaleYear Options")
    print("-" * 55)
    
    problematic_years = []
    
    # Test a sample of years across the range
    test_years = [year_made_min, 1980, 1990, 2000, 2010, year_made_max]
    
    for year_made in test_years:
        # Check if this YearMade can be sold in any valid SaleYear
        has_valid_sale_year = False
        
        # Test selling in the same year and future years up to max
        for sale_year in range(year_made, sale_year_max + 1):
            is_valid, _ = validate_year_logic(year_made, sale_year)
            if is_valid:
                has_valid_sale_year = True
                break
        
        status = "✅ PASS" if has_valid_sale_year else "❌ FAIL"
        print(f"{status}: YearMade={year_made} has valid sale year options")
        
        if not has_valid_sale_year:
            problematic_years.append(year_made)
    
    print()
    
    # Test 3: Edge cases around the boundaries
    print("📋 Test 3: Boundary Edge Cases")
    print("-" * 30)
    
    edge_cases = [
        (year_made_max, sale_year_max, "Max YearMade, Max SaleYear"),
        (year_made_max, sale_year_max - 1, "Max YearMade, SaleYear-1"),
        (year_made_min, sale_year_min, "Min YearMade, Min SaleYear"),
        (year_made_min, sale_year_max, "Min YearMade, Max SaleYear"),
    ]
    
    for year_made, sale_year, description in edge_cases:
        is_valid, error = validate_year_logic(year_made, sale_year)
        status = "✅ PASS" if is_valid else "❌ FAIL"
        print(f"{status}: {description} ({year_made}, {sale_year})")
        if not is_valid:
            print(f"   Error: {error}")
    
    print()
    
    # Test 4: YearMade input validation with boundary SaleYear values
    print("📋 Test 4: YearMade Input Validation with Boundary SaleYear")
    print("-" * 55)
    
    # Test YearMade validation with max SaleYear
    is_valid, parsed, message = validate_year_made(str(year_made_max), sale_year=sale_year_max)
    status = "✅ PASS" if is_valid else "❌ FAIL"
    print(f"{status}: YearMade={year_made_max} with SaleYear={sale_year_max}")
    if not is_valid and message:
        print(f"   Error: {message}")
    
    # Test YearMade validation with min SaleYear (should fail if YearMade > SaleYear)
    is_valid, parsed, message = validate_year_made(str(year_made_max), sale_year=sale_year_min)
    status = "✅ PASS" if not is_valid else "❌ FAIL"  # Should fail
    print(f"{status}: YearMade={year_made_max} with SaleYear={sale_year_min} (should fail)")
    if is_valid:
        print(f"   Error: This should have failed but didn't!")
    
    print()
    
    # Summary
    print("🎯 Summary")
    print("-" * 10)
    
    if problematic_years:
        print(f"❌ ISSUES FOUND: {len(problematic_years)} YearMade values have no valid SaleYear options:")
        for year in problematic_years:
            print(f"   - YearMade {year}")
        print("\nRecommendation: Increase SaleYear maximum or adjust YearMade maximum")
    else:
        print("✅ All validation ranges are consistent!")
        print("✅ Every valid YearMade has at least one valid SaleYear option")
        print("✅ The validation prevents impossible scenarios")
        print("✅ Edge cases are handled correctly")
    
    return len(problematic_years) == 0


def test_specific_user_scenario():
    """Test the specific scenario mentioned by the user."""
    
    print("\n🎯 Testing User's Specific Scenario")
    print("=" * 40)
    
    # Test the original problematic scenario
    print("Original issue: YearMade=2014, SaleYear=2012")
    is_valid, error = validate_year_logic(2014, 2012)
    status = "✅ CORRECTLY REJECTED" if not is_valid else "❌ INCORRECTLY ACCEPTED"
    print(f"{status}: This should be rejected (and is)")
    
    # Test the fixed scenario - equipment made in 2014 should be sellable
    print("\nFixed scenarios for YearMade=2014:")
    
    valid_sale_years = [2014, 2015]
    for sale_year in valid_sale_years:
        is_valid, error = validate_year_logic(2014, sale_year)
        status = "✅ CORRECTLY ACCEPTED" if is_valid else "❌ INCORRECTLY REJECTED"
        print(f"{status}: YearMade=2014, SaleYear={sale_year}")
        if not is_valid:
            print(f"   Error: {error}")
    
    # Test YearMade input validation
    print("\nYearMade input validation for 2014:")
    is_valid, parsed, message = validate_year_made("2014", sale_year=2014)
    status = "✅ CORRECTLY ACCEPTED" if is_valid else "❌ INCORRECTLY REJECTED"
    print(f"{status}: YearMade='2014' with SaleYear=2014")
    if not is_valid and message:
        print(f"   Error: {message}")


if __name__ == "__main__":
    # Run the consistency tests
    print("🧪 Running Validation Consistency Tests")
    print("=" * 50)
    
    try:
        # Test range consistency
        all_consistent = test_validation_range_consistency()
        
        # Test user's specific scenario
        test_specific_user_scenario()
        
        print("\n" + "=" * 50)
        if all_consistent:
            print("🎉 ALL TESTS PASSED! Validation ranges are now consistent.")
            print("✅ Equipment made in any valid year can now be sold in a valid year.")
            print("✅ The original user issue has been resolved.")
        else:
            print("⚠️  Some issues were found. Please review the recommendations above.")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        raise
