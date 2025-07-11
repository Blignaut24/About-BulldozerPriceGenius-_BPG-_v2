"""
Demonstration of YearMade vs SaleYear validation logic.

This script shows how the validation prevents logically impossible scenarios
where equipment is sold before it was manufactured.
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
    sys.exit(1)


def demonstrate_validation():
    """Demonstrate the year validation logic with examples."""
    
    print("🔧 Bulldozer Price Prediction - Year Validation Demo")
    print("=" * 60)
    print()
    
    # Example 1: The user's specific scenario
    print("📋 Example 1: User's Scenario (YearMade=2014, SaleYear=2012)")
    print("-" * 50)
    
    year_made = 2014
    sale_year = 2012
    
    # Test the validation logic
    is_valid, error_msg = validate_year_logic(year_made, sale_year)
    
    print(f"Input: YearMade = {year_made}, SaleYear = {sale_year}")
    print(f"Valid: {is_valid}")
    if not is_valid:
        print(f"Error: {error_msg}")
    print()
    
    # Example 2: Valid scenarios
    print("📋 Example 2: Valid Scenarios")
    print("-" * 30)
    
    valid_examples = [
        (2000, 2005, "5-year-old equipment"),
        (1995, 2010, "15-year-old equipment"),
        (2010, 2010, "Brand new equipment"),
        (1980, 2000, "20-year-old equipment"),
    ]
    
    for year_made, sale_year, description in valid_examples:
        is_valid, error_msg = validate_year_logic(year_made, sale_year)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"{status}: YearMade={year_made}, SaleYear={sale_year} ({description})")
    
    print()
    
    # Example 3: Invalid scenarios
    print("📋 Example 3: Invalid Scenarios (Logically Impossible)")
    print("-" * 55)
    
    invalid_examples = [
        (2014, 2012, "Sold 2 years before manufacturing"),
        (2005, 2000, "Sold 5 years before manufacturing"),
        (2010, 2009, "Sold 1 year before manufacturing"),
        (2000, 1995, "Sold 5 years before manufacturing"),
    ]
    
    for year_made, sale_year, description in invalid_examples:
        is_valid, error_msg = validate_year_logic(year_made, sale_year)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"{status}: YearMade={year_made}, SaleYear={sale_year} ({description})")
        if not is_valid:
            # Show just the first line of the error for brevity
            first_line = error_msg.split('\n')[0]
            print(f"   └─ {first_line}")
    
    print()
    
    # Example 4: YearMade input validation with SaleYear context
    print("📋 Example 4: YearMade Input Validation with SaleYear Context")
    print("-" * 60)
    
    test_inputs = [
        ("2000", 2005, "Valid: Equipment made before sale"),
        ("2014", 2012, "Invalid: Equipment made after sale"),
        ("1995", None, "Valid: No sale year specified"),
        ("abc", 2005, "Invalid: Non-numeric input"),
        ("2000.5", 2005, "Invalid: Decimal year"),
    ]
    
    for year_input, sale_year, description in test_inputs:
        try:
            is_valid, parsed_value, message = validate_year_made(year_input, sale_year)
            status = "✅ VALID" if is_valid else "❌ INVALID"
            print(f"{status}: Input='{year_input}', SaleYear={sale_year}")
            print(f"   └─ {description}")
            if not is_valid and message:
                # Show just the first line of the error for brevity
                first_line = message.split('\n')[0] if '\n' in message else message
                print(f"   └─ Error: {first_line}")
            elif is_valid and parsed_value:
                print(f"   └─ Parsed as: {parsed_value}")
        except Exception as e:
            print(f"❌ ERROR: Input='{year_input}', SaleYear={sale_year}")
            print(f"   └─ Exception: {e}")
        print()
    
    # Example 5: Real-world application flow
    print("📋 Example 5: Real-World Application Flow")
    print("-" * 40)
    
    print("Simulating user entering the problematic values...")
    user_year_made = "2014"
    user_sale_year = 2012
    
    print(f"1. User enters YearMade: '{user_year_made}'")
    print(f"2. User enters SaleYear: {user_sale_year}")
    print("3. Application validates...")
    
    # Step 1: Validate YearMade
    is_valid, parsed_year_made, year_error = validate_year_made(user_year_made, user_sale_year)
    
    if not is_valid:
        print(f"❌ Validation failed at YearMade input:")
        print(f"   {year_error}")
        print("4. User sees error and must correct input before proceeding")
    else:
        print(f"✅ YearMade validation passed: {parsed_year_made}")
        
        # Step 2: Overall logic validation
        logic_valid, logic_error = validate_year_logic(parsed_year_made, user_sale_year)
        if not logic_valid:
            print(f"❌ Logic validation failed:")
            print(f"   {logic_error}")
            print("4. User sees error and must correct input before proceeding")
        else:
            print("✅ All validations passed - prediction can proceed")
    
    print()
    print("🎯 Summary")
    print("-" * 10)
    print("The validation system prevents logically impossible scenarios by:")
    print("• Checking YearMade ≤ SaleYear at input validation level")
    print("• Providing clear, actionable error messages")
    print("• Suggesting specific fixes (adjust YearMade or SaleYear)")
    print("• Showing real-time feedback in the UI")
    print("• Preventing prediction attempts with invalid data")


def interactive_demo():
    """Interactive demonstration where user can test different values."""
    
    print("\n🎮 Interactive Year Validation Demo")
    print("=" * 40)
    print("Enter different YearMade and SaleYear values to test the validation.")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            # Get YearMade input
            year_made_input = input("Enter YearMade (e.g., 2014): ").strip()
            if year_made_input.lower() == 'quit':
                break
            
            # Get SaleYear input
            sale_year_input = input("Enter SaleYear (e.g., 2012): ").strip()
            if sale_year_input.lower() == 'quit':
                break
            
            # Parse SaleYear
            try:
                sale_year = int(sale_year_input) if sale_year_input else None
            except ValueError:
                print("❌ Invalid SaleYear. Please enter a number.\n")
                continue
            
            # Validate
            is_valid, parsed_value, message = validate_year_made(year_made_input, sale_year)
            
            print(f"\nResults:")
            print(f"Valid: {is_valid}")
            if is_valid:
                print(f"Parsed YearMade: {parsed_value}")
                if sale_year:
                    equipment_age = sale_year - parsed_value
                    print(f"Equipment age at sale: {equipment_age} years")
            else:
                print(f"Error: {message}")
            
            print("-" * 40)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("\nThanks for testing the validation system!")


if __name__ == "__main__":
    # Run the demonstration
    demonstrate_validation()
    print("\n✅ Demo complete!")
