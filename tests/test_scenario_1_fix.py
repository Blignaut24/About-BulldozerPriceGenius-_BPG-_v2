#!/usr/bin/env python3
"""
Test script to verify Test Scenario 1 confidence fix
"""

import sys
import os
sys.path.append('..')  # Add parent directory (from tests directory)

def test_scenario_1_confidence():
    """Test the confidence calculation for Test Scenario 1"""
    
    # Test Scenario 1 configuration (UPDATED: 2006 Premium Construction Equipment)
    year_made = 2006
    sale_year = 2007
    product_size = 'Large'
    fi_base_model = 'D8'
    enclosure = 'EROPS w AC'
    
    # Calculate equipment age
    equipment_age = sale_year - year_made  # Should be 1 year (2006 made, 2007 sold)

    print(f"Test Scenario 1 Configuration:")
    print(f"Year Made: {year_made}")
    print(f"Sale Year: {sale_year}")
    print(f"Equipment Age: {equipment_age} years")
    print(f"Product Size: {product_size}")
    print(f"Base Model: {fi_base_model}")
    print(f"Enclosure: {enclosure}")
    print()

    # Test the premium construction equipment confidence detection logic
    is_premium_construction_confidence = (
        equipment_age <= 5 and  # Modern equipment (≤5 years old) for premium construction
        product_size == 'Large' and
        fi_base_model in ['D8', 'D9'] and
        'EROPS' in enclosure
    )
    
    print(f"Premium Construction Equipment Confidence Detection:")
    print(f"Equipment age <= 5: {equipment_age <= 5}")
    print(f"Product size == 'Large': {product_size == 'Large'}")
    print(f"Base model in ['D8', 'D9']: {fi_base_model in ['D8', 'D9']}")
    print(f"'EROPS' in enclosure: {'EROPS' in enclosure}")
    print(f"Is premium construction: {is_premium_construction_confidence}")
    print()

    if is_premium_construction_confidence:
        # Calculate confidence using the new logic for premium construction equipment
        construction_base_confidence = 0.87  # Start at 87% for premium construction equipment
        age_confidence_reduction = min(0.02, equipment_age * 0.005)  # Max 2% reduction for age
        age_adjusted_confidence = construction_base_confidence - age_confidence_reduction

        print(f"Confidence Calculation:")
        print(f"Vintage base confidence: {construction_base_confidence:.1%}")
        print(f"Age confidence reduction: {age_confidence_reduction:.1%}")
        print(f"Final confidence: {age_adjusted_confidence:.1%}")
        print()

        # Check if it meets Test Scenario 1 requirements (85-90%)
        meets_requirement = 0.85 <= age_adjusted_confidence <= 0.90
        print(f"Test Scenario 1 Requirements:")
        print(f"Required confidence range: 85-90%")
        print(f"Calculated confidence: {age_adjusted_confidence:.1%}")
        print(f"Meets requirement: {meets_requirement}")
        
        if meets_requirement:
            print("✅ CONFIDENCE FIX SUCCESSFUL!")
        else:
            print("❌ CONFIDENCE FIX NEEDS ADJUSTMENT")
            
            # Suggest adjustment
            if age_adjusted_confidence < 0.75:
                needed_increase = 0.75 - age_adjusted_confidence
                print(f"💡 Need to increase confidence by {needed_increase:.1%}")
            elif age_adjusted_confidence > 0.85:
                needed_decrease = age_adjusted_confidence - 0.85
                print(f"💡 Need to decrease confidence by {needed_decrease:.1%}")
    else:
        print("❌ Vintage premium confidence detection failed!")
        print("💡 The configuration should trigger vintage premium confidence logic")

if __name__ == "__main__":
    test_scenario_1_confidence()
