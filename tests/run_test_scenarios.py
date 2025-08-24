#!/usr/bin/env python3
"""
Test Runner for BulldozerPriceGenius Enhanced ML Model Test Scenarios
Executes automated validation of all 8 test scenarios from TEST.md

Usage:
    python run_test_scenarios.py

This script will:
1. Validate Enhanced ML Model functionality
2. Test all 8 scenarios with exact parameters from TEST.md
3. Generate pass/fail results for each scenario
4. Provide production readiness assessment
"""

import sys
import os

def main():
    """Main test runner function"""
    print("🚜 BulldozerPriceGenius - Enhanced ML Model Test Runner")
    print("=" * 70)
    
    try:
        # Import and run the automated test suite
        from automated_test_scenarios import TestScenarioValidator
        
        print("🔧 Initializing test validator...")
        validator = TestScenarioValidator()
        
        print("🚀 Starting automated test execution...")
        summary = validator.run_all_tests()
        
        # Display final summary
        print("\n" + "=" * 70)
        print("🎯 FINAL TEST SUMMARY")
        print("=" * 70)
        
        if summary["success"]:
            print("✅ SUCCESS: Enhanced ML Model validation completed")
            print(f"   {summary['passed_tests']}/{summary['total_tests']} scenarios passed")
            print(f"   Success rate: {summary['success_rate']:.1f}%")
            print("   System is ready for production use")
        else:
            print("❌ FAILURE: Enhanced ML Model validation failed")
            print(f"   {summary['passed_tests']}/{summary['total_tests']} scenarios passed")
            print(f"   Success rate: {summary['success_rate']:.1f}%")
            print("   System requires additional fixes before production")
        
        # List failed scenarios for debugging
        if summary['failed_tests'] > 0:
            print("\n🔍 Failed scenarios requiring attention:")
            for result in summary['results']:
                if not result['success']:
                    print(f"   • Scenario {result['scenario_id']}: {result['scenario_name']}")
        
        return summary["success"]
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("   Make sure all required modules are available")
        return False
        
    except Exception as e:
        print(f"❌ Test Execution Error: {e}")
        print("   Check test environment and dependencies")
        return False

if __name__ == "__main__":
    success = main()
    
    if success:
        print("\n🎉 All tests completed successfully!")
        print("Enhanced ML Model is validated and ready for production use")
        sys.exit(0)
    else:
        print("\n⚠️  Test validation failed")
        print("Review the results above and address any issues")
        sys.exit(1)
