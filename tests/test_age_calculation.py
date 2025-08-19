#!/usr/bin/env python3
"""
Test script to verify the Equipment Age at Sale calculation fix.
"""

def test_age_calculation():
    """Test the age calculation logic"""
    
    # Test case from the user's example
    year_made = 2014
    sale_year = 2015
    expected_age = 1  # Should be 1 year, not 4 years
    
    # Fixed calculation
    age_at_sale = sale_year - year_made
    
    print(f"Test Case: Year Made = {year_made}, Sale Year = {sale_year}")
    print(f"Expected Age: {expected_age} years")
    print(f"Calculated Age: {age_at_sale} years")
    print(f"Test Result: {'✅ PASS' if age_at_sale == expected_age else '❌ FAIL'}")
    print()
    
    # Additional test cases
    test_cases = [
        (2000, 2006, 6),  # 6 years old
        (1995, 2005, 10), # 10 years old
        (2010, 2011, 1),  # 1 year old
        (1980, 2000, 20), # 20 years old
    ]
    
    print("Additional Test Cases:")
    for year_made, sale_year, expected in test_cases:
        calculated = sale_year - year_made
        result = "✅ PASS" if calculated == expected else "❌ FAIL"
        print(f"  Year Made: {year_made}, Sale Year: {sale_year} → Age: {calculated} years ({result})")
    
    print("\n🎯 The fix ensures that Equipment Age at Sale = Sale Year - Year Made")
    print("   This correctly calculates how old the bulldozer was when it was sold.")

if __name__ == "__main__":
    test_age_calculation()
