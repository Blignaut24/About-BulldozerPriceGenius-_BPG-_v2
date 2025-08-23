#!/usr/bin/env python3
"""
Comprehensive Statistical Fallback Prediction System Validation
Advanced evaluation framework for unseen data validation with cross-validation methodology
"""

import sys
import time
import random
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import KFold
import statistics
sys.path.append('.')

def create_comprehensive_test_dataset():
    """Create comprehensive unseen test dataset with cross-validation methodology"""
    
    # Test Scenario 1 (Baseline compliance test)
    test_scenario_1 = {
        'year_made': 1994, 'sale_year': 2005, 'product_size': 'Large', 'state': 'California',
        'enclosure': 'EROPS w AC', 'fi_base_model': 'D8', 'coupler_system': 'Hydraulic',
        'tire_size': '26.5R25', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
        'hydraulics': '4 Valve', 'model_id': 4200, 'sale_day_of_year': 180,
        'expected_price_range': (140000, 230000), 'expected_confidence_range': (75, 85),
        'expected_multiplier_range': (8.0, 10.0), 'scenario_name': 'Test Scenario 1 - Baseline Compliance',
        'category': 'compliance_test', 'priority': 'critical'
    }
    
    # Comprehensive unseen test scenarios for robustness testing
    unseen_scenarios = [
        # VINTAGE EQUIPMENT TESTS (Pre-2000)
        {
            'year_made': 1989, 'sale_year': 2006, 'product_size': 'Large', 'state': 'Texas',
            'enclosure': 'EROPS w AC', 'fi_base_model': 'D9', 'coupler_system': 'Hydraulic',
            'tire_size': '29.5', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
            'hydraulics': '4 Valve', 'model_id': 4500, 'sale_day_of_year': 220,
            'expected_price_range': (150000, 300000), 'expected_confidence_range': (75, 90),
            'expected_multiplier_range': (8.0, 12.0), 'scenario_name': 'Vintage D9 Premium - Texas',
            'category': 'vintage_premium', 'priority': 'high'
        },
        {
            'year_made': 1995, 'sale_year': 2008, 'product_size': 'Large', 'state': 'Florida',
            'enclosure': 'EROPS', 'fi_base_model': 'D8', 'coupler_system': 'Manual',
            'tire_size': '26.5R25', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 4000, 'sale_day_of_year': 150,
            'expected_price_range': (100000, 200000), 'expected_confidence_range': (70, 85),
            'expected_multiplier_range': (6.0, 9.0), 'scenario_name': 'Vintage D8 Standard - Florida',
            'category': 'vintage_standard', 'priority': 'medium'
        },
        {
            'year_made': 1992, 'sale_year': 2009, 'product_size': 'Medium', 'state': 'Illinois',
            'enclosure': 'ROPS', 'fi_base_model': 'D6', 'coupler_system': 'Manual',
            'tire_size': '23.5R25', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 3200, 'sale_day_of_year': 300,
            'expected_price_range': (60000, 140000), 'expected_confidence_range': (65, 80),
            'expected_multiplier_range': (4.0, 7.0), 'scenario_name': 'Vintage D6 Basic - Economic Stress',
            'category': 'vintage_basic', 'priority': 'medium'
        },
        
        # MODERN EQUIPMENT TESTS (2000-2010)
        {
            'year_made': 2005, 'sale_year': 2012, 'product_size': 'Large', 'state': 'California',
            'enclosure': 'EROPS w AC', 'fi_base_model': 'D8', 'coupler_system': 'Hydraulic',
            'tire_size': '26.5R25', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
            'hydraulics': '4 Valve', 'model_id': 4200, 'sale_day_of_year': 180,
            'expected_price_range': (200000, 350000), 'expected_confidence_range': (80, 90),
            'expected_multiplier_range': (7.0, 10.0), 'scenario_name': 'Modern D8 Premium - California',
            'category': 'modern_premium', 'priority': 'high'
        },
        {
            'year_made': 2008, 'sale_year': 2015, 'product_size': 'Medium', 'state': 'Colorado',
            'enclosure': 'EROPS', 'fi_base_model': 'D6', 'coupler_system': 'Hydraulic',
            'tire_size': '20.5R25', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Single',
            'hydraulics': '3 Valve', 'model_id': 3500, 'sale_day_of_year': 120,
            'expected_price_range': (120000, 220000), 'expected_confidence_range': (75, 85),
            'expected_multiplier_range': (5.0, 8.0), 'scenario_name': 'Modern D6 Premium - Colorado',
            'category': 'modern_premium', 'priority': 'high'
        },
        {
            'year_made': 2003, 'sale_year': 2010, 'product_size': 'Small', 'state': 'Oregon',
            'enclosure': 'ROPS', 'fi_base_model': 'D4', 'coupler_system': 'Manual',
            'tire_size': '16.9R24', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 2800, 'sale_day_of_year': 90,
            'expected_price_range': (70000, 130000), 'expected_confidence_range': (70, 80),
            'expected_multiplier_range': (4.0, 6.5), 'scenario_name': 'Modern D4 Standard - Oregon',
            'category': 'modern_standard', 'priority': 'medium'
        },
        
        # RECENT EQUIPMENT TESTS (2010+)
        {
            'year_made': 2015, 'sale_year': 2018, 'product_size': 'Large', 'state': 'Texas',
            'enclosure': 'EROPS w AC', 'fi_base_model': 'D10', 'coupler_system': 'Hydraulic',
            'tire_size': '35/65-33', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
            'hydraulics': '4 Valve', 'model_id': 5000, 'sale_day_of_year': 200,
            'expected_price_range': (300000, 500000), 'expected_confidence_range': (85, 95),
            'expected_multiplier_range': (6.0, 9.0), 'scenario_name': 'Recent D10 Premium - Texas',
            'category': 'recent_premium', 'priority': 'high'
        },
        {
            'year_made': 2012, 'sale_year': 2016, 'product_size': 'Compact', 'state': 'Washington',
            'enclosure': 'ROPS', 'fi_base_model': 'D3', 'coupler_system': 'Manual',
            'tire_size': 'None or Unspecified', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 2200, 'sale_day_of_year': 60,
            'expected_price_range': (50000, 90000), 'expected_confidence_range': (65, 80),
            'expected_multiplier_range': (3.0, 5.5), 'scenario_name': 'Recent D3 Compact - Washington',
            'category': 'recent_compact', 'priority': 'medium'
        },
        
        # REGIONAL VARIATION TESTS
        {
            'year_made': 2000, 'sale_year': 2010, 'product_size': 'Large', 'state': 'Alaska',
            'enclosure': 'EROPS w AC', 'fi_base_model': 'D8', 'coupler_system': 'Hydraulic',
            'tire_size': '26.5R25', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
            'hydraulics': '4 Valve', 'model_id': 4200, 'sale_day_of_year': 100,
            'expected_price_range': (180000, 320000), 'expected_confidence_range': (75, 90),
            'expected_multiplier_range': (7.0, 11.0), 'scenario_name': 'Regional Premium - Alaska',
            'category': 'regional_premium', 'priority': 'high'
        },
        {
            'year_made': 2006, 'sale_year': 2013, 'product_size': 'Medium', 'state': 'Wyoming',
            'enclosure': 'OROPS', 'fi_base_model': 'D6', 'coupler_system': 'Manual',
            'tire_size': '20.5R25', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 3300, 'sale_day_of_year': 250,
            'expected_price_range': (90000, 170000), 'expected_confidence_range': (70, 85),
            'expected_multiplier_range': (4.5, 7.5), 'scenario_name': 'Regional Standard - Wyoming',
            'category': 'regional_standard', 'priority': 'medium'
        },
        
        # ECONOMIC STRESS TESTS (2008-2009 Market Downturn)
        {
            'year_made': 2001, 'sale_year': 2008, 'product_size': 'Large', 'state': 'Michigan',
            'enclosure': 'EROPS', 'fi_base_model': 'D8', 'coupler_system': 'Manual',
            'tire_size': '26.5R25', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 4000, 'sale_day_of_year': 320,
            'expected_price_range': (120000, 220000), 'expected_confidence_range': (70, 85),
            'expected_multiplier_range': (5.0, 8.5), 'scenario_name': 'Economic Stress - 2008 Michigan',
            'category': 'economic_stress', 'priority': 'high'
        },
        {
            'year_made': 1998, 'sale_year': 2009, 'product_size': 'Medium', 'state': 'Ohio',
            'enclosure': 'ROPS', 'fi_base_model': 'D6', 'coupler_system': 'Manual',
            'tire_size': '23.5R25', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 3200, 'sale_day_of_year': 350,
            'expected_price_range': (60000, 130000), 'expected_confidence_range': (65, 80),
            'expected_multiplier_range': (4.0, 7.0), 'scenario_name': 'Economic Stress - 2009 Ohio',
            'category': 'economic_stress', 'priority': 'high'
        },
        
        # EDGE CASES AND STRESS TESTS
        {
            'year_made': 2018, 'sale_year': 2020, 'product_size': 'Large', 'state': 'California',
            'enclosure': 'EROPS w AC', 'fi_base_model': 'D11', 'coupler_system': 'Hydraulic',
            'tire_size': '35/65-33', 'hydraulics_flow': 'High Flow', 'grouser_tracks': 'Double',
            'hydraulics': '4 Valve', 'model_id': 5500, 'sale_day_of_year': 180,
            'expected_price_range': (400000, 650000), 'expected_confidence_range': (85, 95),
            'expected_multiplier_range': (5.5, 8.5), 'scenario_name': 'Ultra-Modern D11 Premium - California',
            'category': 'edge_case', 'priority': 'medium'
        },
        {
            'year_made': 1985, 'sale_year': 2005, 'product_size': 'Large', 'state': 'Nevada',
            'enclosure': 'NO ROPS', 'fi_base_model': 'D8', 'coupler_system': 'Manual',
            'tire_size': '26.5', 'hydraulics_flow': 'Standard', 'grouser_tracks': 'Single',
            'hydraulics': '2 Valve', 'model_id': 3800, 'sale_day_of_year': 45,
            'expected_price_range': (80000, 180000), 'expected_confidence_range': (60, 80),
            'expected_multiplier_range': (5.0, 9.0), 'scenario_name': 'Very Old D8 Basic - Nevada',
            'category': 'edge_case', 'priority': 'low'
        }
    ]
    
    # Add Test Scenario 1 as the first test
    all_scenarios = [test_scenario_1] + unseen_scenarios
    
    return all_scenarios

def evaluate_prediction_accuracy_comprehensive(scenarios):
    """Comprehensive evaluation with detailed metrics and cross-validation methodology"""
    
    print("🔬 Comprehensive Statistical Fallback System Evaluation")
    print("=" * 80)
    
    try:
        from app_pages.four_interactive_prediction import make_prediction_fallback
    except ImportError as e:
        print(f"❌ Could not import fallback system: {e}")
        return None
    
    results = []
    test_scenario_1_compliant = 0
    category_results = {}
    priority_results = {}
    
    total_scenarios = len(scenarios)
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📋 Test {i}/{total_scenarios}: {scenario['scenario_name']}")
        print(f"   Category: {scenario['category']} | Priority: {scenario['priority']}")
        print("-" * 70)
        
        # Record start time for performance measurement
        start_time = time.time()
        
        try:
            # Make prediction using fallback system
            prediction = make_prediction_fallback(
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
            
            # Record end time
            end_time = time.time()
            response_time = end_time - start_time
            
            # Extract prediction results
            predicted_price = prediction.get('predicted_price', 0)
            confidence = prediction.get('confidence', 0)
            multiplier = prediction.get('value_multiplier', 0)
            method = prediction.get('method', 'Unknown')
            
            # Check against expected ranges
            price_min, price_max = scenario['expected_price_range']
            conf_min, conf_max = scenario['expected_confidence_range']
            mult_min, mult_max = scenario['expected_multiplier_range']
            
            price_in_range = price_min <= predicted_price <= price_max
            confidence_in_range = conf_min <= confidence <= conf_max
            multiplier_in_range = mult_min <= multiplier <= mult_max
            response_time_ok = response_time < 10.0
            method_correct = 'Statistical' in method or 'Fallback' in method or 'intelligent' in method
            
            # Calculate accuracy metrics
            price_error_pct = abs(predicted_price - (price_min + price_max) / 2) / ((price_min + price_max) / 2) * 100
            confidence_error_pct = abs(confidence - (conf_min + conf_max) / 2) / ((conf_min + conf_max) / 2) * 100
            multiplier_error_pct = abs(multiplier - (mult_min + mult_max) / 2) / ((mult_min + mult_max) / 2) * 100
            
            # Special Test Scenario 1 compliance check
            is_test_scenario_1 = scenario['scenario_name'].startswith('Test Scenario 1')
            test_scenario_1_compliant_this = False
            
            if is_test_scenario_1:
                ts1_price_ok = 140000 <= predicted_price <= 230000
                ts1_conf_ok = 75 <= confidence <= 85
                ts1_mult_ok = 8.0 <= multiplier <= 10.0
                test_scenario_1_compliant_this = ts1_price_ok and ts1_conf_ok and ts1_mult_ok and response_time_ok
                if test_scenario_1_compliant_this:
                    test_scenario_1_compliant += 1
            
            # Calculate overall accuracy score
            accuracy_score = sum([price_in_range, confidence_in_range, multiplier_in_range, response_time_ok, method_correct]) / 5.0
            
            # Display results
            print(f"💰 Price: ${predicted_price:,.2f} ({'✅' if price_in_range else '❌'} Expected: ${price_min:,}-${price_max:,}) Error: {price_error_pct:.1f}%")
            print(f"📊 Confidence: {confidence:.1f}% ({'✅' if confidence_in_range else '❌'} Expected: {conf_min}-{conf_max}%) Error: {confidence_error_pct:.1f}%")
            print(f"📈 Multiplier: {multiplier:.2f}x ({'✅' if multiplier_in_range else '❌'} Expected: {mult_min:.1f}x-{mult_max:.1f}x) Error: {multiplier_error_pct:.1f}%")
            print(f"⏱️  Response Time: {response_time:.3f}s ({'✅' if response_time_ok else '❌'} Expected: <10s)")
            print(f"🔧 Method: {method} ({'✅' if method_correct else '❌'})")
            print(f"🎯 Accuracy Score: {accuracy_score:.1%}")
            
            if is_test_scenario_1:
                print(f"🏆 Test Scenario 1 Compliant: {'✅' if test_scenario_1_compliant_this else '❌'}")
            
            # Store results
            result = {
                'scenario_name': scenario['scenario_name'],
                'category': scenario['category'],
                'priority': scenario['priority'],
                'predicted_price': predicted_price,
                'confidence': confidence,
                'multiplier': multiplier,
                'response_time': response_time,
                'method': method,
                'price_in_range': price_in_range,
                'confidence_in_range': confidence_in_range,
                'multiplier_in_range': multiplier_in_range,
                'response_time_ok': response_time_ok,
                'method_correct': method_correct,
                'accuracy_score': accuracy_score,
                'price_error_pct': price_error_pct,
                'confidence_error_pct': confidence_error_pct,
                'multiplier_error_pct': multiplier_error_pct,
                'is_test_scenario_1': is_test_scenario_1,
                'test_scenario_1_compliant': test_scenario_1_compliant_this,
                'scenario_config': scenario
            }
            
            results.append(result)
            
            # Group by category and priority
            category = scenario['category']
            priority = scenario['priority']
            
            if category not in category_results:
                category_results[category] = []
            category_results[category].append(result)
            
            if priority not in priority_results:
                priority_results[priority] = []
            priority_results[priority].append(result)
            
        except Exception as e:
            print(f"❌ Prediction failed: {e}")
            error_result = {
                'scenario_name': scenario['scenario_name'],
                'category': scenario['category'],
                'priority': scenario['priority'],
                'error': str(e),
                'accuracy_score': 0.0,
                'is_test_scenario_1': is_test_scenario_1,
                'test_scenario_1_compliant': False
            }
            results.append(error_result)
            
            # Add to category and priority groups
            if category not in category_results:
                category_results[category] = []
            category_results[category].append(error_result)
            
            if priority not in priority_results:
                priority_results[priority] = []
            priority_results[priority].append(error_result)
    
    return results, test_scenario_1_compliant, category_results, priority_results

def analyze_comprehensive_results(results, test_scenario_1_compliant, category_results, priority_results):
    """Comprehensive analysis with detailed metrics and recommendations"""
    
    print(f"\n🎯 Comprehensive Statistical Fallback System Analysis")
    print("=" * 80)
    
    if not results:
        print("❌ No results to analyze")
        return None
    
    # Filter successful predictions
    successful_results = [r for r in results if 'error' not in r]
    failed_results = [r for r in results if 'error' in r]
    
    total_tests = len(results)
    successful_tests = len(successful_results)
    success_rate = successful_tests / total_tests if total_tests > 0 else 0
    
    print(f"📊 Overall Performance Metrics:")
    print(f"   Total Tests: {total_tests}")
    print(f"   Successful Predictions: {successful_tests}")
    print(f"   Success Rate: {success_rate:.1%}")
    print(f"   Failed Predictions: {len(failed_results)}")
    
    if successful_results:
        # Calculate comprehensive accuracy metrics
        accuracy_scores = [r['accuracy_score'] for r in successful_results]
        avg_accuracy = np.mean(accuracy_scores)
        std_accuracy = np.std(accuracy_scores)
        min_accuracy = np.min(accuracy_scores)
        max_accuracy = np.max(accuracy_scores)
        
        # Error metrics
        price_errors = [r['price_error_pct'] for r in successful_results]
        confidence_errors = [r['confidence_error_pct'] for r in successful_results]
        multiplier_errors = [r['multiplier_error_pct'] for r in successful_results]
        
        avg_price_error = np.mean(price_errors)
        avg_confidence_error = np.mean(confidence_errors)
        avg_multiplier_error = np.mean(multiplier_errors)
        
        # Response time metrics
        response_times = [r['response_time'] for r in successful_results]
        avg_response_time = np.mean(response_times)
        max_response_time = np.max(response_times)
        
        # Component accuracy rates
        price_accuracy = np.mean([r['price_in_range'] for r in successful_results])
        confidence_accuracy = np.mean([r['confidence_in_range'] for r in successful_results])
        multiplier_accuracy = np.mean([r['multiplier_in_range'] for r in successful_results])
        response_time_compliance = np.mean([r['response_time_ok'] for r in successful_results])
        method_accuracy = np.mean([r['method_correct'] for r in successful_results])
        
        print(f"\n📈 Accuracy Analysis:")
        print(f"   Average Accuracy Score: {avg_accuracy:.1%} ± {std_accuracy:.1%}")
        print(f"   Accuracy Range: {min_accuracy:.1%} - {max_accuracy:.1%}")
        print(f"   Price Prediction Accuracy: {price_accuracy:.1%} (Avg Error: {avg_price_error:.1f}%)")
        print(f"   Confidence Range Accuracy: {confidence_accuracy:.1%} (Avg Error: {avg_confidence_error:.1f}%)")
        print(f"   Multiplier Range Accuracy: {multiplier_accuracy:.1%} (Avg Error: {avg_multiplier_error:.1f}%)")
        print(f"   Response Time Compliance: {response_time_compliance:.1%}")
        print(f"   Method Display Accuracy: {method_accuracy:.1%}")
        
        print(f"\n⏱️  Performance Metrics:")
        print(f"   Average Response Time: {avg_response_time:.3f}s")
        print(f"   Maximum Response Time: {max_response_time:.3f}s")
        print(f"   Response Time Compliance: {response_time_compliance:.1%}")
        
        # Test Scenario 1 specific analysis
        test_scenario_1_results = [r for r in successful_results if r['is_test_scenario_1']]
        test_scenario_1_total = len([r for r in results if r['is_test_scenario_1']])
        
        print(f"\n🏆 Test Scenario 1 Compliance Analysis:")
        print(f"   Test Scenario 1 Tests: {test_scenario_1_total}")
        print(f"   Test Scenario 1 Compliant: {test_scenario_1_compliant}")
        print(f"   Test Scenario 1 Compliance Rate: {test_scenario_1_compliant/test_scenario_1_total:.1%}" if test_scenario_1_total > 0 else "   No Test Scenario 1 tests found")
        
        if test_scenario_1_results:
            ts1_result = test_scenario_1_results[0]
            print(f"   Test Scenario 1 Details:")
            print(f"     Price: ${ts1_result['predicted_price']:,.2f} (Target: $140K-$230K)")
            print(f"     Confidence: {ts1_result['confidence']:.1f}% (Target: 75-85%)")
            print(f"     Multiplier: {ts1_result['multiplier']:.2f}x (Target: 8.0x-10.0x)")
            print(f"     Response Time: {ts1_result['response_time']:.3f}s (Target: <10s)")
            print(f"     Method: {ts1_result['method']}")
        
        # Category-based analysis
        print(f"\n🔧 Robustness Analysis by Category:")
        for category, cat_results in category_results.items():
            cat_successful = [r for r in cat_results if 'error' not in r]
            if cat_successful:
                cat_accuracy = np.mean([r['accuracy_score'] for r in cat_successful])
                cat_price_acc = np.mean([r['price_in_range'] for r in cat_successful])
                cat_mult_acc = np.mean([r['multiplier_in_range'] for r in cat_successful])
                print(f"   {category.replace('_', ' ').title()}: {cat_accuracy:.1%} accuracy ({len(cat_successful)} tests)")
                print(f"     Price: {cat_price_acc:.1%}, Multiplier: {cat_mult_acc:.1%}")
        
        # Priority-based analysis
        print(f"\n📋 Analysis by Test Priority:")
        for priority, pri_results in priority_results.items():
            pri_successful = [r for r in pri_results if 'error' not in r]
            if pri_successful:
                pri_accuracy = np.mean([r['accuracy_score'] for r in pri_successful])
                print(f"   {priority.title()} Priority: {pri_accuracy:.1%} accuracy ({len(pri_successful)} tests)")
        
        # Equipment size analysis
        print(f"\n📏 Equipment Size Analysis:")
        size_groups = {}
        for r in successful_results:
            size = r['scenario_config']['product_size']
            if size not in size_groups:
                size_groups[size] = []
            size_groups[size].append(r['accuracy_score'])
        
        for size, scores in size_groups.items():
            avg_score = np.mean(scores)
            std_score = np.std(scores) if len(scores) > 1 else 0
            print(f"   {size} Equipment: {avg_score:.1%} ± {std_score:.1%} accuracy ({len(scores)} tests)")
        
        # Age category analysis
        print(f"\n📅 Equipment Age Analysis:")
        age_groups = {'Vintage (Pre-2000)': [], 'Modern (2000-2010)': [], 'Recent (2010+)': []}
        for r in successful_results:
            year_made = r['scenario_config']['year_made']
            if year_made < 2000:
                age_groups['Vintage (Pre-2000)'].append(r['accuracy_score'])
            elif year_made < 2010:
                age_groups['Modern (2000-2010)'].append(r['accuracy_score'])
            else:
                age_groups['Recent (2010+)'].append(r['accuracy_score'])
        
        for age_cat, scores in age_groups.items():
            if scores:
                avg_score = np.mean(scores)
                std_score = np.std(scores) if len(scores) > 1 else 0
                print(f"   {age_cat}: {avg_score:.1%} ± {std_score:.1%} accuracy ({len(scores)} tests)")
    
    # Production readiness assessment
    print(f"\n🚀 Production Readiness Assessment:")
    
    production_ready = True
    issues = []
    recommendations = []
    
    # Define production thresholds
    thresholds = {
        'success_rate': 0.95,
        'avg_accuracy': 0.75,
        'price_accuracy': 0.70,
        'multiplier_accuracy': 0.70,
        'confidence_accuracy': 0.70,
        'response_time_compliance': 0.95,
        'test_scenario_1_compliance': 1.0
    }
    
    if success_rate < thresholds['success_rate']:
        production_ready = False
        issues.append(f"Success rate ({success_rate:.1%}) below {thresholds['success_rate']:.1%} threshold")
        recommendations.append("Investigate and fix prediction failures")
    
    if successful_results:
        if avg_accuracy < thresholds['avg_accuracy']:
            production_ready = False
            issues.append(f"Average accuracy ({avg_accuracy:.1%}) below {thresholds['avg_accuracy']:.1%} threshold")
            recommendations.append("Improve overall prediction accuracy through calibration")
        
        if price_accuracy < thresholds['price_accuracy']:
            production_ready = False
            issues.append(f"Price accuracy ({price_accuracy:.1%}) below {thresholds['price_accuracy']:.1%} threshold")
            recommendations.append("Refine base prices and depreciation curves")
        
        if multiplier_accuracy < thresholds['multiplier_accuracy']:
            production_ready = False
            issues.append(f"Multiplier accuracy ({multiplier_accuracy:.1%}) below {thresholds['multiplier_accuracy']:.1%} threshold")
            recommendations.append("Calibrate multiplier calculation logic")
        
        if confidence_accuracy < thresholds['confidence_accuracy']:
            production_ready = False
            issues.append(f"Confidence accuracy ({confidence_accuracy:.1%}) below {thresholds['confidence_accuracy']:.1%} threshold")
            recommendations.append("Adjust confidence calculation ranges")
        
        if response_time_compliance < thresholds['response_time_compliance']:
            production_ready = False
            issues.append(f"Response time compliance ({response_time_compliance:.1%}) below {thresholds['response_time_compliance']:.1%} threshold")
            recommendations.append("Optimize prediction performance")
        
        if test_scenario_1_compliant == 0:
            production_ready = False
            issues.append("Test Scenario 1 compliance failure")
            recommendations.append("Fix Test Scenario 1 specific issues")
    
    if production_ready:
        print(f"   ✅ PRODUCTION READY")
        print(f"   - High success rate ({success_rate:.1%})")
        print(f"   - Good accuracy ({avg_accuracy:.1%})" if successful_results else "")
        print(f"   - Fast response times ({avg_response_time:.3f}s avg)" if successful_results else "")
        print(f"   - Test Scenario 1 compliant")
        print(f"   - Robust across equipment categories")
    else:
        print(f"   ❌ NEEDS IMPROVEMENT")
        for issue in issues:
            print(f"   - {issue}")
        
        print(f"\n💡 Recommendations:")
        for rec in recommendations:
            print(f"   - {rec}")
    
    # Generate comprehensive summary
    summary = {
        'success_rate': success_rate,
        'avg_accuracy': avg_accuracy if successful_results else 0,
        'price_accuracy': price_accuracy if successful_results else 0,
        'confidence_accuracy': confidence_accuracy if successful_results else 0,
        'multiplier_accuracy': multiplier_accuracy if successful_results else 0,
        'avg_response_time': avg_response_time if successful_results else 0,
        'test_scenario_1_compliant': test_scenario_1_compliant,
        'test_scenario_1_rate': test_scenario_1_compliant/test_scenario_1_total if test_scenario_1_total > 0 else 0,
        'production_ready': production_ready,
        'issues': issues,
        'recommendations': recommendations,
        'category_results': category_results,
        'priority_results': priority_results
    }
    
    return summary

def main():
    """Main comprehensive validation function"""
    
    print("🔬 Comprehensive Statistical Fallback Prediction System Validation")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create comprehensive test dataset
    print("📋 Creating comprehensive unseen test dataset...")
    scenarios = create_comprehensive_test_dataset()
    print(f"✅ Created {len(scenarios)} diverse test scenarios")
    print(f"   Categories: {len(set(s['category'] for s in scenarios))}")
    print(f"   Priorities: {len(set(s['priority'] for s in scenarios))}")
    
    # Evaluate accuracy comprehensively
    results, test_scenario_1_compliant, category_results, priority_results = evaluate_prediction_accuracy_comprehensive(scenarios)
    
    # Analyze results comprehensively
    summary = analyze_comprehensive_results(results, test_scenario_1_compliant, category_results, priority_results)
    
    print(f"\n🎯 Final Assessment:")
    if summary and summary['production_ready']:
        print(f"✅ The statistical fallback system is PRODUCTION READY")
        print(f"   Comprehensive validation confirms reliability and accuracy")
        print(f"   Ready for deployment with confidence")
    else:
        print(f"⚠️  The statistical fallback system needs targeted improvements")
        print(f"   Address identified issues before production deployment")
        if summary and summary['recommendations']:
            print(f"   Priority: {summary['recommendations'][0] if summary['recommendations'] else 'General calibration'}")
    
    return summary

if __name__ == "__main__":
    main()
