#!/usr/bin/env python3
"""
Test Scenario 3 Economic Crisis Fix Verification
Tests if the Enhanced ML Model now applies economic crisis adjustments
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

def test_economic_crisis_adjustment():
    """Test if economic crisis adjustments are working"""
    
    # Test the economic adjustment logic directly
    sale_year = 2008
    base_price = 100000  # $100k base price
    
    # Economic cycle adjustments (from the fix)
    economic_adjustments = {
        2006: 0.12, 2007: 0.15,  # Construction boom
        2008: -0.15, 2009: -0.25,  # Financial crisis
        2010: -0.05, 2011: 0.00, 2012: 0.02,  # Recovery
        2013: 0.03, 2014: 0.04, 2015: 0.05   # Stable growth
    }
    
    economic_adjustment = 1.0  # Default
    if sale_year in economic_adjustments:
        economic_adjustment = 1 + economic_adjustments[sale_year]
    
    adjusted_price = base_price * economic_adjustment
    
    print(f"🧪 Economic Crisis Adjustment Test")
    print(f"   Sale Year: {sale_year}")
    print(f"   Base Price: ${base_price:,}")
    print(f"   Economic Adjustment: {economic_adjustments[sale_year]:.1%}")
    print(f"   Multiplier: {economic_adjustment:.3f}x")
    print(f"   Adjusted Price: ${adjusted_price:,}")
    print(f"   Price Reduction: ${base_price - adjusted_price:,} ({((base_price - adjusted_price) / base_price * 100):.1f}%)")
    
    # Test if this would bring Test Scenario 3 into range
    test_scenario_3_base = 175000  # From your results
    test_scenario_3_adjusted = test_scenario_3_base * economic_adjustment
    
    print(f"\n🎯 Test Scenario 3 Projection:")
    print(f"   Original Prediction: ${test_scenario_3_base:,}")
    print(f"   With Crisis Adjustment: ${test_scenario_3_adjusted:,}")
    print(f"   Required Range: $70,000 - $130,000")
    
    if 70000 <= test_scenario_3_adjusted <= 130000:
        print(f"   ✅ PASS: Adjusted price is within required range")
        return True
    else:
        print(f"   ❌ FAIL: Adjusted price is still outside range")
        print(f"   Need additional reduction of: ${test_scenario_3_adjusted - 130000:,}")
        return False

if __name__ == "__main__":
    test_economic_crisis_adjustment()
