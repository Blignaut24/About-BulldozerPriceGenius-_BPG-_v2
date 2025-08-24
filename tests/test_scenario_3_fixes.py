#!/usr/bin/env python3
"""
Test Scenario 3 Fixes Validation Script
Tests the Enhanced ML Model calibration fixes for large standard equipment
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app_pages.four_interactive_prediction import make_prediction
from src.external_model_loader_v2 import ExternalModelLoaderV2

def test_scenario_3_fixes():
    """Test the fixes for Test Scenario 3: Large Basic Workhorse (Standard Configuration)"""
    
    print("🚜 Test Scenario 3 Fixes Validation")
    print("=" * 60)
    print("Testing Enhanced ML Model calibration for large standard equipment")
    print()
    
    # Use the main application's model loading approach
    print("🔍 Using main application model loading approach...")
    print("✅ Model loading will be handled by prediction function")
    print()
    
    # Test Scenario 3 Configuration
    print("📋 Test Scenario 3: Large Basic Workhorse (Standard Configuration)")
    print("-" * 50)
    
    test_config = {
        'year_made': 2004,
        'product_size': 'Large',
        'state': 'Kansas',
        'sale_year': 2009,
        'sale_day_of_year': 340,
        'model_id': 6500,
        'enclosure': 'ROPS',
        'fi_base_model': 'D6',
        'coupler_system': 'Manual',
        'tire_size': 'None or Unspecified',
        'hydraulics_flow': 'Standard',
        'grouser_tracks': 'Single',
        'hydraulics': '2 Valve'
    }
    
    print("🔧 Input Parameters:")
    for key, value in test_config.items():
        print(f"   • {key.replace('_', ' ').title()}: {value}")
    print()
    
    # Expected Results
    expected_price_min = 65000
    expected_price_max = 95000
    expected_confidence_min = 82
    expected_confidence_max = 88
    
    print("🎯 Expected Results:")
    print(f"   • Price Range: ${expected_price_min:,} - ${expected_price_max:,}")
    print(f"   • Confidence: {expected_confidence_min}-{expected_confidence_max}%")
    print(f"   • Method: Enhanced ML Model")
    print()
    
    # Make Prediction
    print("🚀 Executing Enhanced ML Model Prediction...")
    try:
        result = make_prediction(
            model=None,  # Let the function load the model
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
            sale_day_of_year=test_config['sale_day_of_year'],
            preprocessing_data=None  # Let the function load preprocessing data
        )
        
        if not result['success']:
            print(f"❌ Prediction failed: {result.get('error', 'Unknown error')}")
            return False
            
        print("✅ Prediction completed successfully")
        print()
        
    except Exception as e:
        print(f"❌ Error during prediction: {str(e)}")
        return False
    
    # Analyze Results
    print("📊 PREDICTION RESULTS ANALYSIS")
    print("=" * 60)
    
    predicted_price = result['predicted_price']
    confidence_level = result['confidence_level']
    confidence_percent = int(confidence_level * 100) if confidence_level <= 1.0 else int(confidence_level)
    method = result.get('method', 'Unknown')
    
    print(f"🔥 Predicted Sale Price: ${predicted_price:,.2f}")
    print(f"🟢 Confidence Level: {confidence_percent}%")
    print(f"🔥 Method: {method}")
    print()
    
    # Show calibration details
    if 'base_prediction' in result:
        base_price = result['base_prediction']
        calibrated_base = result.get('calibrated_base_price', base_price)
        base_adjusted = result.get('base_price_adjusted', False)
        multiplier = result.get('value_multiplier', 1.0)
        
        print("🔍 Technical Details:")
        print(f"   • Original Base ML Prediction: ${base_price:,.0f}")
        if base_adjusted:
            print(f"   • Calibrated Base Price: ${calibrated_base:,.0f} ✅ ADJUSTED")
        else:
            print(f"   • Calibrated Base Price: ${calibrated_base:,.0f} (no adjustment needed)")
        print(f"   • Premium Value Multiplier: {multiplier:.2f}x")
        print(f"   • Enhanced Prediction: ${calibrated_base:,.0f} × {multiplier:.2f} = ${predicted_price:,.2f}")
        print()
    
    # Validation
    print("✅ VALIDATION RESULTS")
    print("=" * 60)
    
    validation_results = []
    
    # 1. Price Range Validation
    price_in_range = expected_price_min <= predicted_price <= expected_price_max
    validation_results.append(("Price Range", price_in_range))
    
    if price_in_range:
        print(f"✅ Price Range: PASS (${predicted_price:,.2f} within ${expected_price_min:,}-${expected_price_max:,})")
    else:
        print(f"❌ Price Range: FAIL (${predicted_price:,.2f} outside ${expected_price_min:,}-${expected_price_max:,})")
        if predicted_price < expected_price_min:
            shortfall = expected_price_min - predicted_price
            print(f"   • Shortfall: ${shortfall:,.2f} below minimum")
        else:
            excess = predicted_price - expected_price_max
            print(f"   • Excess: ${excess:,.2f} above maximum")
    
    # 2. Confidence Level Validation
    confidence_in_range = expected_confidence_min <= confidence_percent <= expected_confidence_max
    validation_results.append(("Confidence Level", confidence_in_range))
    
    if confidence_in_range:
        print(f"✅ Confidence Level: PASS ({confidence_percent}% within {expected_confidence_min}-{expected_confidence_max}%)")
    else:
        print(f"❌ Confidence Level: FAIL ({confidence_percent}% outside {expected_confidence_min}-{expected_confidence_max}%)")
    
    # 3. Method Display Validation
    method_correct = method == "Enhanced ML Model"
    validation_results.append(("Method Display", method_correct))
    
    if method_correct:
        print(f"✅ Method Display: PASS ('{method}')")
    else:
        print(f"❌ Method Display: FAIL ('{method}' instead of 'Enhanced ML Model')")
    
    # 4. System Errors Validation
    no_errors = result['success']
    validation_results.append(("No System Errors", no_errors))
    
    if no_errors:
        print("✅ System Errors: PASS (No errors detected)")
    else:
        print("❌ System Errors: FAIL (Errors detected)")
    
    print()
    
    # Overall Result
    passed_criteria = sum(1 for _, passed in validation_results if passed)
    total_criteria = len(validation_results)
    
    print("🎯 OVERALL TEST RESULT")
    print("=" * 60)
    print(f"Passed Criteria: {passed_criteria} out of {total_criteria}")
    
    if passed_criteria >= 4:  # Need at least 4/4 to pass
        print("✅ TEST SCENARIO 3: PASS")
        print("🎉 Enhanced ML Model calibration fixes successful!")
        return True
    else:
        print("❌ TEST SCENARIO 3: FAIL")
        print("⚠️  Additional calibration adjustments needed")
        return False

if __name__ == "__main__":
    success = test_scenario_3_fixes()
    sys.exit(0 if success else 1)
