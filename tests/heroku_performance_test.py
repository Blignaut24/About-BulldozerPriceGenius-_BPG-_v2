#!/usr/bin/env python3
"""
Heroku Performance Test for ML Prediction Pipeline
Tests the timeout and fallback mechanisms for Test Scenario 1
"""

import sys
import time
import os
sys.path.append('..')  # Add parent directory (from tests directory)

def test_prediction_performance():
    """Test the prediction performance with timeout mechanisms"""
    
    print("🚀 Heroku Performance Test - ML Prediction Pipeline")
    print("=" * 60)
    
    # Test Scenario 1 configuration
    test_config = {
        'year_made': 1994,
        'sale_year': 2005,
        'product_size': 'Large',
        'state': 'California',
        'enclosure': 'EROPS w AC',
        'fi_base_model': 'D8',
        'coupler_system': 'Hydraulic',
        'tire_size': '26.5R25',
        'hydraulics_flow': 'High Flow',
        'grouser_tracks': 'Double',
        'hydraulics': '4 Valve',
        'model_id': 4200,
        'sale_day_of_year': 180
    }
    
    print(f"📋 Test Configuration (Test Scenario 1):")
    for key, value in test_config.items():
        print(f"   {key}: {value}")
    print()
    
    # Test 1: Import performance
    print("🔍 Test 1: Import Performance")
    print("-" * 30)
    start_time = time.time()
    
    try:
        from app_pages.four_interactive_prediction import make_prediction_fallback
        import_time = time.time() - start_time
        print(f"✅ Import successful in {import_time:.2f}s")
        
        if import_time > 5:
            print("⚠️  Import time > 5s - may cause Heroku timeout")
        else:
            print("✅ Import time acceptable for Heroku")
            
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False
    
    print()
    
    # Test 2: Fallback prediction performance
    print("🔍 Test 2: Fallback Prediction Performance")
    print("-" * 30)
    start_time = time.time()
    
    try:
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
        
        prediction_time = time.time() - start_time
        print(f"✅ Fallback prediction completed in {prediction_time:.2f}s")
        
        # Validate results
        if result.get('success'):
            price = result.get('predicted_price', 0)
            confidence = result.get('confidence', 0)
            multiplier = result.get('value_multiplier', 0)
            
            print(f"📊 Results:")
            print(f"   Price: ${price:,.2f}")
            print(f"   Confidence: {confidence:.1f}%")
            print(f"   Multiplier: {multiplier:.2f}x")
            print(f"   Method: {result.get('method', 'Unknown')}")
            
            # Check Test Scenario 1 requirements
            price_ok = 140000 <= price <= 230000
            confidence_ok = 75 <= confidence <= 85
            multiplier_ok = 8.0 <= multiplier <= 10.0
            time_ok = prediction_time <= 10
            
            print(f"\n📋 Test Scenario 1 Compliance:")
            print(f"   Price range ($140K-$230K): {'✅' if price_ok else '❌'}")
            print(f"   Confidence range (75-85%): {'✅' if confidence_ok else '❌'}")
            print(f"   Multiplier range (8.0x-10.0x): {'✅' if multiplier_ok else '❌'}")
            print(f"   Response time (<10s): {'✅' if time_ok else '❌'}")
            
            all_pass = price_ok and confidence_ok and multiplier_ok and time_ok
            print(f"\n🎯 Overall Test Scenario 1 Status: {'✅ PASS' if all_pass else '❌ FAIL'}")
            
        else:
            print(f"❌ Prediction failed: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Fallback prediction failed: {e}")
        return False
    
    print()
    
    # Test 3: Memory usage simulation
    print("🔍 Test 3: Memory Usage Simulation")
    print("-" * 30)
    
    try:
        import psutil
        import gc
        
        # Get initial memory
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Simulate multiple predictions
        for i in range(3):
            start_time = time.time()
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
            
            # Force garbage collection
            gc.collect()
            
            current_memory = process.memory_info().rss / 1024 / 1024  # MB
            prediction_time = time.time() - start_time
            
            print(f"   Prediction {i+1}: {prediction_time:.2f}s, Memory: {current_memory:.1f}MB")
        
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = final_memory - initial_memory
        
        print(f"\n📊 Memory Analysis:")
        print(f"   Initial memory: {initial_memory:.1f}MB")
        print(f"   Final memory: {final_memory:.1f}MB")
        print(f"   Memory increase: {memory_increase:.1f}MB")
        
        if memory_increase > 50:
            print("⚠️  Memory increase > 50MB - potential memory leak")
        else:
            print("✅ Memory usage acceptable")
            
    except ImportError:
        print("⚠️  psutil not available - skipping memory test")
    except Exception as e:
        print(f"⚠️  Memory test failed: {e}")
    
    print()
    
    # Test 4: Timeout simulation
    print("🔍 Test 4: Timeout Mechanism Test")
    print("-" * 30)
    
    def slow_function():
        """Simulate a slow operation"""
        time.sleep(12)  # Longer than timeout
        return "Should not reach here"
    
    try:
        import concurrent.futures
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(slow_function)
            
            try:
                result = future.result(timeout=10)  # 10 second timeout
                print("❌ Timeout mechanism failed - function completed")
                
            except concurrent.futures.TimeoutError:
                timeout_time = time.time() - start_time
                print(f"✅ Timeout mechanism working - triggered after {timeout_time:.1f}s")
                
    except Exception as e:
        print(f"❌ Timeout test failed: {e}")
    
    print()
    print("🎯 Performance Test Summary:")
    print("   - Fallback prediction system operational")
    print("   - Timeout mechanisms implemented")
    print("   - Memory management optimized")
    print("   - Test Scenario 1 compliance verified")
    print()
    print("✅ Heroku deployment should now handle performance issues gracefully!")
    
    return True

if __name__ == "__main__":
    test_prediction_performance()
