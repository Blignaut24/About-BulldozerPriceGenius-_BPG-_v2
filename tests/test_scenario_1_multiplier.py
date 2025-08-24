#!/usr/bin/env python3
"""
Test script to verify Test Scenario 1 multiplier calculation
"""

import sys
import os
sys.path.append('..')  # Add parent directory (from tests directory)

def test_scenario_1_multiplier():
    """Test the multiplier calculation for Test Scenario 1"""
    
    # Test Scenario 1 configuration
    year_made = 1994
    sale_year = 2005
    product_size = 'Large'
    fi_base_model = 'D8'
    enclosure = 'EROPS w AC'
    hydraulics_flow = 'High Flow'
    hydraulics = '4 Valve'
    coupler_system = 'Hydraulic'
    grouser_tracks = 'Double'
    state = 'California'
    sale_day_of_year = 180
    
    print(f"Test Scenario 1 Configuration:")
    print(f"Year Made: {year_made}")
    print(f"Sale Year: {sale_year}")
    print(f"Product Size: {product_size}")
    print(f"Base Model: {fi_base_model}")
    print(f"Enclosure: {enclosure}")
    print(f"Hydraulics Flow: {hydraulics_flow}")
    print(f"Hydraulics: {hydraulics}")
    print(f"Coupler System: {coupler_system}")
    print(f"Grouser Tracks: {grouser_tracks}")
    print(f"State: {state}")
    print()
    
    # Calculate equipment age
    equipment_age = sale_year - year_made  # Should be 11 years
    
    # Test the vintage premium multiplier detection logic
    is_vintage_premium = (
        year_made <= 1995 and
        product_size == 'Large' and
        fi_base_model in ['D8', 'D9'] and
        'EROPS' in enclosure
    )
    
    print(f"Vintage Premium Multiplier Detection:")
    print(f"Year made <= 1995: {year_made <= 1995}")
    print(f"Product size == 'Large': {product_size == 'Large'}")
    print(f"Base model in ['D8', 'D9']: {fi_base_model in ['D8', 'D9']}")
    print(f"'EROPS' in enclosure: {'EROPS' in enclosure}")
    print(f"Is vintage premium: {is_vintage_premium}")
    print()
    
    if is_vintage_premium:
        print(f"Vintage Premium Multiplier Logic:")
        print(f"Test Scenario 1 requires multiplier between 8.0x - 10.0x")
        print(f"Current logic: final_multiplier = min(9.0, max(7.5, final_multiplier))")
        print(f"This ensures multiplier is clamped to 7.5x - 9.0x range")
        print()
        
        # Test different input multipliers
        test_multipliers = [5.0, 7.0, 8.5, 9.5, 12.0]
        
        print(f"Testing multiplier clamping:")
        for test_mult in test_multipliers:
            clamped_mult = min(9.0, max(7.5, test_mult))
            meets_requirement = 8.0 <= clamped_mult <= 10.0
            status = "✅" if meets_requirement else "❌"
            print(f"Input: {test_mult:.1f}x → Clamped: {clamped_mult:.1f}x → Meets 8.0x-10.0x: {status}")
        
        print()
        print(f"Analysis:")
        print(f"- The current clamping logic (7.5x - 9.0x) overlaps with the requirement (8.0x - 10.0x)")
        print(f"- However, it may be too restrictive on the upper end (9.0x vs 10.0x)")
        print(f"- Your reported 9.00x multiplier suggests the logic is working correctly")
        print(f"- The issue might be elsewhere in the calculation chain")
        
    else:
        print("❌ Vintage premium multiplier detection failed!")
        print("💡 The configuration should trigger vintage premium multiplier logic")

if __name__ == "__main__":
    test_scenario_1_multiplier()
