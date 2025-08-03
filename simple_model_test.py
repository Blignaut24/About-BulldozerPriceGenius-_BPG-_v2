#!/usr/bin/env python3
"""
Simple test to verify the ML model works with proper preprocessing
"""

import pickle
import pandas as pd

def test_model_simple():
    """Simple test of the model"""
    print("🧪 Simple Model Test")
    print("=" * 30)
    
    try:
        # Load model
        print("Loading model...")
        model = pickle.load(open('src/models/randomforest_regressor_best_RMSLE.pkl', 'rb'))
        print(f"✅ Model loaded: {type(model)}")
        
        # Load training data to get structure
        print("Loading training data structure...")
        training_data = pd.read_parquet('src/data_prep/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet')
        print(f"✅ Training data shape: {training_data.shape}")
        
        # Get first row as template (excluding SalePrice)
        template_row = training_data.drop('SalePrice', axis=1).iloc[0:1].copy()
        print(f"✅ Template shape: {template_row.shape}")
        
        # Modify some values for our test
        template_row['YearMade'] = 2005
        template_row['ModelID'] = 4605
        template_row['saleYear'] = 2012
        
        print("Making prediction...")
        prediction = model.predict(template_row)[0]
        print(f"🎯 Prediction: ${prediction:,.2f}")
        
        print("\n" + "=" * 30)
        print("🎉 SUCCESS! Model works!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_model_simple()
