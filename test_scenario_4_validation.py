#!/usr/bin/env python3
"""
Test Scenario 4 Validation Script
Validates the compact equipment calibration fixes for the Statistical Fallback Model
"""

import sys
import os

# Add the app_pages directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app_pages'))

try:
    from four_interactive_prediction import make_prediction_fallback
    print("✅ Successfully imported Statistical Fallback Model")
except ImportError as e:
    print(f"❌ Failed to import Statistical Fallback Model: {e}")
    sys.exit(1)

def test_scenario_4_calibration():
    """
    Test the calibration fixes for Test Scenario 4: Vintage Compact Specialist Equipment
    Configuration: 1992 D3 compact bulldozer, ROPS, Florida, sold in 2007
    """
    print("\n🧪 Testing Test Scenario 4 Calibration Fixes")
    print("=" * 60)
    
    # Test Scenario 4 configuration
    test_config = {
        'year_made': 1992,
        'sale_year': 2007,
        'product_size': 'Compact',
        'state': 'Florida',
        'enclosure': 'ROPS',
        'fi_base_model': 'D3',
        'coupler_system': 'Manual',
        'tire_size': '16.9R24',
        'hydraulics_flow': 'Standard Flow',
        'grouser_tracks': 'Single',
        'hydraulics': '2 Valve',
        'model_id': 2400,
        'sale_day_of_year': 210
    }
    
    print("📋 Test Configuration:")
    for key, value in test_config.items():
        print(f"   {key}: {value}")
    
    print("\n🎯 Expected Results:")
    print("   Price Range: $45,000 - $85,000")
    print("   Confidence Range: 75-85%")
    print("   Value Multiplier Range: 7.5x - 12.0x")
    
    try:
        # Call the Statistical Fallback Model with all parameters
        result = make_prediction_fallback(
            year_made=test_config['year_made'],
            model_id=test_config['model_id'],
            product_size=test_config['product_size'],
            state=test_config['state'],
            enclosure=test_config['enclosure'],
            fi_base_model=test_config['fi_base_model'],
            coupler_system=test_config['coupler_system'],
            tire_size=test_config['tire_size'],
            hydraulics_flow=test_config['hydraulics_flow'],
            grouser_tracks=test_config['grouser_tracks'],
            hydraulics=test_config['hydraulics'],
            sale_year=test_config['sale_year'],
            sale_day_of_year=test_config['sale_day_of_year']
        )

        print("\n📊 Actual Results:")
        predicted_price = result.get('predicted_price', 0)
        confidence = result.get('confidence', 0)
        method = result.get('method', 'Unknown')
        print(f"   Predicted Price: ${predicted_price:,.2f}")
        print(f"   Confidence Level: {confidence}%")
        print(f"   Method: {method}")

        # Debug: Print full result
        print(f"\n🔍 Debug Info:")
        for key, value in result.items():
            if key not in ['predicted_price', 'confidence', 'method']:
                print(f"   {key}: {value}")

        # Calculate value multiplier (approximate)
        base_price = 75000  # New compact base price
        multiplier = predicted_price / base_price if base_price > 0 else 0
        print(f"\n   Estimated Multiplier: {multiplier:.1f}x")
        
        # Validate results
        print("\n✅ Validation:")

        # Price range validation
        price_in_range = 45000 <= predicted_price <= 85000
        print(f"   Price in range ($45K-$85K): {'✅ PASS' if price_in_range else '❌ FAIL'}")

        # Confidence range validation
        confidence_in_range = 75 <= confidence <= 85
        print(f"   Confidence in range (75-85%): {'✅ PASS' if confidence_in_range else '❌ FAIL'}")

        # Multiplier range validation
        multiplier_in_range = 7.5 <= multiplier <= 12.0
        print(f"   Multiplier in range (7.5x-12.0x): {'✅ PASS' if multiplier_in_range else '❌ FAIL'}")

        # Overall assessment
        overall_pass = price_in_range and confidence_in_range and multiplier_in_range
        print(f"\n🎯 Overall Assessment: {'✅ PASS' if overall_pass else '❌ FAIL'}")

        if overall_pass:
            print("🎉 Compact equipment calibration fixes are working correctly!")
        else:
            print("⚠️ Compact equipment calibration still needs adjustment.")

        return overall_pass, predicted_price, multiplier
        
    except Exception as e:
        print(f"\n❌ Error during prediction: {e}")
        return False, None, None

def test_other_compact_scenarios():
    """
    Test other compact equipment scenarios to ensure no regression
    """
    print("\n🔍 Testing Other Compact Equipment Scenarios")
    print("=" * 60)
    
    test_scenarios = [
        {
            'name': 'Modern Compact (2010)',
            'year_made': 2010,
            'product_size': 'Compact',
            'state': 'California',
            'sale_year': 2015
        },
        {
            'name': 'Recent Compact (2015)',
            'year_made': 2015,
            'product_size': 'Compact',
            'state': 'Texas',
            'sale_year': 2018
        }
    ]
    
    for scenario in test_scenarios:
        print(f"\n📋 {scenario['name']}:")
        try:
            # Use simplified parameters for basic testing
            result = make_prediction_fallback(
                year_made=scenario['year_made'],
                model_id=2400,  # Default model ID
                product_size=scenario['product_size'],
                state=scenario['state'],
                enclosure='ROPS',  # Default enclosure
                fi_base_model='D3',  # Default base model for compact
                coupler_system='Manual',  # Default coupler
                tire_size='16.9R24',  # Default tire size
                hydraulics_flow='Standard Flow',  # Default hydraulics
                grouser_tracks='Single',  # Default tracks
                hydraulics='2 Valve',  # Default hydraulics
                sale_year=scenario['sale_year'],
                sale_day_of_year=210  # Default day
            )

            predicted_price = result.get('predicted_price', 0)
            base_price = 75000
            multiplier = predicted_price / base_price if base_price > 0 else 0

            print(f"   Predicted Price: ${predicted_price:,.2f}")
            print(f"   Estimated Multiplier: {multiplier:.1f}x")

            # Basic sanity check
            reasonable_price = 30000 <= predicted_price <= 150000
            reasonable_multiplier = 2.0 <= multiplier <= 15.0

            if reasonable_price and reasonable_multiplier:
                print("   Status: ✅ Reasonable")
            else:
                print("   Status: ⚠️ May need review")

        except Exception as e:
            print(f"   Error: ❌ {e}")

if __name__ == "__main__":
    print("🚜 BulldozerPriceGenius - Test Scenario 4 Calibration Validation")
    print("Testing compact equipment valuation fixes...")
    
    # Test the main scenario
    success, price, multiplier = test_scenario_4_calibration()
    
    # Test other scenarios for regression
    test_other_compact_scenarios()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 CALIBRATION VALIDATION SUCCESSFUL!")
        print("Test Scenario 4 should now pass with the implemented fixes.")
    else:
        print("⚠️ CALIBRATION VALIDATION FAILED!")
        print("Additional adjustments may be needed.")
    
    print("\n📝 Next Steps:")
    print("1. Re-run Test Scenario 4 on Page 4 Interactive Prediction")
    print("2. Verify predicted price falls within $45,000-$85,000 range")
    print("3. Confirm confidence level reaches 75-85%")
    print("4. Update TEST.md with successful results")
