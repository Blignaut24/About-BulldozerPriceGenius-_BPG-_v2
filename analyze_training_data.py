#!/usr/bin/env python3
"""
Analyze the training data structure to understand the feature mismatch.
"""

import pandas as pd
import pickle
import os

def analyze_training_data():
    """Analyze the training data structure."""
    print("🔍 Analyzing Training Data Structure")
    print("=" * 40)
    
    try:
        # Load training data
        training_data = pd.read_parquet('src/data_prep/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet')
        
        print(f"📊 Training data shape: {training_data.shape}")
        print(f"📋 Number of features: {len(training_data.columns) - 1}")  # Exclude SalePrice
        
        # Get feature columns (exclude target)
        feature_columns = [col for col in training_data.columns if col != 'SalePrice']
        
        print(f"\n📋 First 20 feature columns:")
        for i, col in enumerate(feature_columns[:20]):
            dtype = training_data[col].dtype
            print(f"   {i+1:2d}. {col} ({dtype})")
        
        print(f"\n📋 Last 20 feature columns:")
        for i, col in enumerate(feature_columns[-20:]):
            dtype = training_data[col].dtype
            print(f"   {len(feature_columns)-19+i:2d}. {col} ({dtype})")
        
        # Check for specific columns mentioned in the error
        error_columns = ['Backhoe_Mounting', 'Blade_Extension', 'Blade_Type']
        print(f"\n🔍 Checking for error-mentioned columns:")
        for col in error_columns:
            if col in feature_columns:
                print(f"   ✅ {col}: Present")
            else:
                print(f"   ❌ {col}: Missing")
        
        # Check for columns that were in our test input
        test_columns = ['YearMade', 'ProductSize', 'state', 'Enclosure', 'fiBaseModel', 
                       'Coupler_System', 'Tire_Size', 'Hydraulics_Flow', 'Grouser_Tracks', 
                       'Hydraulics', 'SaleYear', 'saledate']
        print(f"\n🔍 Checking for test input columns:")
        for col in test_columns:
            if col in feature_columns:
                print(f"   ✅ {col}: Present")
            else:
                print(f"   ❌ {col}: Missing")
        
        return feature_columns
        
    except Exception as e:
        print(f"❌ Failed to load training data: {e}")
        return None

def analyze_preprocessing_components():
    """Analyze the preprocessing components."""
    print("\n🔍 Analyzing Preprocessing Components")
    print("=" * 40)
    
    try:
        with open('src/models/preprocessing_components.pkl', 'rb') as f:
            preprocessing_data = pickle.load(f)
        
        print(f"📋 Components: {list(preprocessing_data.keys())}")
        
        # Analyze label encoders
        label_encoders = preprocessing_data['label_encoders']
        print(f"📊 Label encoders: {len(label_encoders)} encoders")
        if len(label_encoders) > 0:
            print(f"🔑 Encoder columns: {list(label_encoders.keys())}")
        else:
            print("⚠️ No label encoders found!")
        
        # Analyze imputer
        imputer = preprocessing_data['imputer']
        print(f"📊 Imputer type: {type(imputer).__name__}")
        
        # Try to get feature names from imputer
        if hasattr(imputer, 'feature_names_in_'):
            feature_names = imputer.feature_names_in_
            print(f"📊 Imputer expects {len(feature_names)} features")
            print(f"📋 First 10 expected features: {list(feature_names[:10])}")
            print(f"📋 Last 10 expected features: {list(feature_names[-10:])}")
            return feature_names
        else:
            print("⚠️ Imputer doesn't have feature_names_in_ attribute")
            return None
            
    except Exception as e:
        print(f"❌ Failed to load preprocessing components: {e}")
        return None

def compare_features(training_features, imputer_features):
    """Compare training data features with imputer expected features."""
    print("\n🔍 Comparing Feature Sets")
    print("=" * 30)
    
    if training_features is None or imputer_features is None:
        print("❌ Cannot compare - missing feature information")
        return
    
    training_set = set(training_features)
    imputer_set = set(imputer_features)
    
    print(f"📊 Training data features: {len(training_set)}")
    print(f"📊 Imputer expected features: {len(imputer_set)}")
    
    # Find differences
    only_in_training = training_set - imputer_set
    only_in_imputer = imputer_set - training_set
    common_features = training_set & imputer_set
    
    print(f"📊 Common features: {len(common_features)}")
    print(f"📊 Only in training data: {len(only_in_training)}")
    print(f"📊 Only in imputer: {len(only_in_imputer)}")
    
    if only_in_training:
        print(f"\n📋 Features only in training data (first 10):")
        for feature in list(only_in_training)[:10]:
            print(f"   - {feature}")
    
    if only_in_imputer:
        print(f"\n📋 Features only in imputer (first 10):")
        for feature in list(only_in_imputer)[:10]:
            print(f"   - {feature}")
    
    # Check if they match exactly
    if training_set == imputer_set:
        print("\n✅ Feature sets match perfectly!")
        return True
    else:
        print("\n❌ Feature sets do not match!")
        return False

def main():
    """Analyze the feature mismatch issue."""
    print("BulldozerPriceGenius - Feature Mismatch Analysis")
    print("=" * 50)
    print("Investigating preprocessing components compatibility")
    print()
    
    # Analyze training data
    training_features = analyze_training_data()
    
    # Analyze preprocessing components
    imputer_features = analyze_preprocessing_components()
    
    # Compare features
    features_match = compare_features(training_features, imputer_features)
    
    print("\n" + "=" * 50)
    print("📊 Analysis Summary:")
    print(f"   Training data loaded: {'✅' if training_features else '❌'}")
    print(f"   Preprocessing components loaded: {'✅' if imputer_features else '❌'}")
    print(f"   Feature sets match: {'✅' if features_match else '❌'}")
    
    if not features_match:
        print("\n🔧 Recommended Actions:")
        print("1. Regenerate preprocessing components with current training data")
        print("2. Or update feature engineering to match imputer expectations")
        print("3. Or use basic preprocessing as fallback (current behavior)")
    
    return features_match

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
