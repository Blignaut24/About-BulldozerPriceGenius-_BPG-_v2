#!/usr/bin/env python3
"""
Test Scenario 5 Validation Script
Tests the Enhanced ML Model calibration fixes for modern premium construction boom equipment.

Test Scenario 5: 2004 D8 Large bulldozer with premium features sold in Nevada during 2006 construction boom
Expected: $180,000 - $280,000 (boom period premium)
Previous Issue: $3,110,161.25 (catastrophic overvaluation)
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app_pages.four_interactive_prediction import make_prediction_fallback
    print("✅ Successfully imported Statistical Fallback Model")
except ImportError as e:
    print(f"❌ Failed to import Statistical Fallback Model: {e}")
    sys.exit(1)

def test_scenario_5_calibration():
    """
    Test the Test Scenario 5 calibration fixes for modern premium construction boom equipment.
    
    Returns:
        tuple: (success, predicted_price, confidence)
    """
    print("🧪 Testing Test Scenario 5 Calibration Fixes")
    print("=" * 60)
    
    # Test Scenario 5 Configuration (Modern Premium Construction Boom)
    test_config = {
        'year_made': 2004,
        'sale_year': 2006,
        'product_size': 'Large',
        'state': 'Nevada',
        'enclosure': 'EROPS w AC',
        'fi_base_model': 'D8',
        'coupler_system': 'Hydraulic',
        'tire_size': '26.5R25',
        'hydraulics_flow': 'High Flow',
        'grouser_tracks': 'Double',
        'hydraulics': '4 Valve',
        'model_id': 4600,
        'sale_day_of_year': 120
    }
    
    print("📋 Test Configuration:")
    for key, value in test_config.items():
        print(f"   {key}: {value}")
    
    print(f"\n🎯 Expected Results:")
    print(f"   Price Range: $180,000 - $280,000")
    print(f"   Confidence Range: 80-90%")
    print(f"   Value Multiplier Range: 7.5x - 11.0x")
    
    try:
        # Test the fallback prediction system
        result = make_prediction_fallback(**test_config)
        
        if result.get('success'):
            predicted_price = result.get('predicted_price', 0)
            confidence = result.get('confidence', 0)
            method = result.get('method', 'Unknown')
            
            print(f"\n📊 Actual Results:")
            print(f"   Predicted Price: ${predicted_price:,.2f}")
            print(f"   Confidence Level: {confidence}%")
            print(f"   Method: {method}")
            
            # Debug: Print full result
            print(f"\n🔍 Debug Info:")
            for key, value in result.items():
                if key not in ['predicted_price', 'confidence', 'method']:
                    print(f"   {key}: {value}")
            
            # Calculate value multiplier (approximate)
            base_price = 200000  # Large equipment base price
            multiplier = predicted_price / base_price if base_price > 0 else 0
            print(f"\n   Estimated Multiplier: {multiplier:.1f}x")
            
            # Validate results
            print(f"\n✅ Validation:")
            
            # Price range validation
            price_in_range = 180000 <= predicted_price <= 280000
            print(f"   Price in range ($180K-$280K): {'✅ PASS' if price_in_range else '❌ FAIL'}")
            
            # Confidence range validation
            confidence_in_range = 80 <= confidence <= 90
            print(f"   Confidence in range (80-90%): {'✅ PASS' if confidence_in_range else '❌ FAIL'}")
            
            # Multiplier range validation
            multiplier_in_range = 7.5 <= multiplier <= 11.0
            print(f"   Multiplier in range (7.5x-11.0x): {'✅ PASS' if multiplier_in_range else '❌ FAIL'}")
            
            # Overall assessment
            overall_pass = price_in_range and confidence_in_range and multiplier_in_range
            
            print(f"\n🎯 Overall Assessment: {'✅ PASS' if overall_pass else '❌ FAIL'}")
            if overall_pass:
                print("🎉 Modern premium construction boom calibration successful!")
            else:
                print("⚠️ Modern premium construction boom calibration still needs adjustment.")
            
            return overall_pass, predicted_price, multiplier
            
        else:
            print(f"❌ Prediction failed: {result.get('error', 'Unknown error')}")
            return False, 0, 0
            
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        return False, 0, 0

def test_other_modern_scenarios():
    """Test other modern equipment scenarios for regression testing."""
    print(f"\n🔍 Testing Other Modern Equipment Scenarios")
    print("=" * 60)
    
    test_scenarios = [
        {
            'name': 'Modern Standard (2005)',
            'year_made': 2005,
            'sale_year': 2007,
            'product_size': 'Large',
            'state': 'Texas',
            'enclosure': 'EROPS',
            'fi_base_model': 'D7',
            'coupler_system': 'Manual',
            'tire_size': '23.5R25',
            'hydraulics_flow': 'Standard Flow',
            'grouser_tracks': 'Single',
            'hydraulics': '2 Valve',
            'model_id': 3500,
            'sale_day_of_year': 180
        },
        {
            'name': 'Modern Premium (2003)',
            'year_made': 2003,
            'sale_year': 2006,
            'product_size': 'Large',
            'state': 'California',
            'enclosure': 'EROPS w AC',
            'fi_base_model': 'D9',
            'coupler_system': 'Hydraulic',
            'tire_size': '29.5R25',
            'hydraulics_flow': 'High Flow',
            'grouser_tracks': 'Double',
            'hydraulics': '4 Valve',
            'model_id': 5200,
            'sale_day_of_year': 90
        }
    ]
    
    for scenario in test_scenarios:
        print(f"\n📋 {scenario['name']}:")
        try:
            # Use simplified parameters for basic testing
            result = make_prediction_fallback(
                year_made=scenario['year_made'],
                model_id=scenario['model_id'],
                product_size=scenario['product_size'],
                state=scenario['state'],
                enclosure=scenario['enclosure'],
                fi_base_model=scenario['fi_base_model'],
                coupler_system=scenario['coupler_system'],
                tire_size=scenario['tire_size'],
                hydraulics_flow=scenario['hydraulics_flow'],
                grouser_tracks=scenario['grouser_tracks'],
                hydraulics=scenario['hydraulics'],
                sale_year=scenario['sale_year'],
                sale_day_of_year=scenario['sale_day_of_year']
            )
            
            predicted_price = result.get('predicted_price', 0)
            base_price = 200000
            multiplier = predicted_price / base_price if base_price > 0 else 0
            
            print(f"   Predicted Price: ${predicted_price:,.2f}")
            print(f"   Estimated Multiplier: {multiplier:.1f}x")
            
            # Basic sanity check
            reasonable_price = 150000 <= predicted_price <= 400000
            reasonable_multiplier = 5.0 <= multiplier <= 15.0
            
            if reasonable_price and reasonable_multiplier:
                print("   Status: ✅ Reasonable")
            else:
                print("   Status: ⚠️ May need review")
                
        except Exception as e:
            print(f"   Error: ❌ {e}")

if __name__ == "__main__":
    print("🚜 BulldozerPriceGenius - Test Scenario 5 Calibration Validation")
    print("Testing modern premium construction boom equipment valuation fixes...")
    
    # Test the main scenario
    success, price, multiplier = test_scenario_5_calibration()
    
    # Test other scenarios for regression
    test_other_modern_scenarios()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 CALIBRATION VALIDATION SUCCESSFUL!")
        print("Modern premium construction boom equipment properly valued.")
    else:
        print("⚠️ CALIBRATION VALIDATION FAILED!")
        print("Additional adjustments may be needed.")
    
    print("\n📝 Next Steps:")
    print("1. Re-run Test Scenario 5 on Page 4 Interactive Prediction")
    print("2. Verify predicted price falls within $180,000-$280,000 range")
    print("3. Confirm confidence level reaches 80-90%")
    print("4. Update TEST.md with successful results")
