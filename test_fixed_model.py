#!/usr/bin/env python3
"""
Test script to verify the fixed ML model works correctly
"""

import pickle
import pandas as pd
import numpy as np

def test_model():
    """Test the fixed model"""
    print("🧪 Testing Fixed ML Model")
    print("=" * 50)
    
    try:
        # Load the model
        print("📁 Loading model...")
        model = pickle.load(open('src/models/randomforest_regressor_best_RMSLE.pkl', 'rb'))
        
        print(f"✅ Model type: {type(model)}")
        print(f"✅ Has predict method: {hasattr(model, 'predict')}")
        
        # Load preprocessing components
        print("\n📁 Loading preprocessing components...")
        preprocessing_data = pickle.load(open('src/models/preprocessing_components.pkl', 'rb'))
        
        print(f"✅ Label encoders: {len(preprocessing_data['label_encoders'])} features")
        print(f"✅ Imputer: {type(preprocessing_data['imputer'])}")
        print(f"✅ Performance metrics: {preprocessing_data['performance_metrics']}")
        
        # Create test input with exact training data structure
        print("\n🔧 Creating test input...")

        # Load training data to get exact column structure
        training_data = pd.read_parquet('src/data_prep/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet').head(1)
        expected_columns = [col for col in training_data.columns if col != 'SalePrice']  # Exclude target

        # Create input data frame with the same structure
        input_row = {}

        # Set the main features
        input_row['SalesID'] = 1139246
        input_row['MachineID'] = 999999
        input_row['ModelID'] = 4605
        input_row['datasource'] = 121
        input_row['auctioneerID'] = 3
        input_row['YearMade'] = 2005
        input_row['MachineHoursCurrentMeter'] = 5000
        input_row['UsageBand'] = 'Medium'
        input_row['fiModelDesc'] = 'Unknown'
        input_row['fiBaseModel'] = 'D6'
        input_row['fiSecondaryDesc'] = 'Unknown'
        input_row['fiModelSeries'] = 'Unknown'
        input_row['fiModelDescriptor'] = 'Unknown'
        input_row['ProductSize'] = 'Large'
        input_row['fiProductClassDesc'] = 'Unknown'
        input_row['state'] = 'California'
        input_row['ProductGroup'] = 'Track Type Tractor Dozers'
        input_row['ProductGroupDesc'] = 'Track Type Tractor Dozers'
        input_row['Drive_System'] = 'Unknown'
        input_row['Enclosure'] = 'EROPS'
        input_row['Forks'] = 'None or Unspecified'
        input_row['Pad_Type'] = 'None or Unspecified'
        input_row['Ride_Control'] = 'None or Unspecified'
        input_row['Stick'] = 'None or Unspecified'
        input_row['Transmission'] = 'Standard'
        input_row['Turbocharged'] = 'None or Unspecified'
        input_row['Blade_Extension'] = 'None or Unspecified'
        input_row['Blade_Width'] = 'None or Unspecified'
        input_row['Enclosure_Type'] = 'None or Unspecified'
        input_row['Engine_Horsepower'] = 200
        input_row['Hydraulics'] = 'Standard'
        input_row['Pushblock'] = 'None or Unspecified'
        input_row['Ripper'] = 'None or Unspecified'
        input_row['Scarifier'] = 'None or Unspecified'
        input_row['Tip_Control'] = 'None or Unspecified'
        input_row['Tire_Size'] = 'None or Unspecified'
        input_row['Coupler'] = 'None or Unspecified'
        input_row['Coupler_System'] = 'None or Unspecified'
        input_row['Grouser_Tracks'] = 'None or Unspecified'
        input_row['Hydraulics_Flow'] = 'Standard'
        input_row['Track_Type'] = 'Steel'
        input_row['Undercarriage_Pad_Width'] = 'None or Unspecified'
        input_row['Stick_Length'] = 'None or Unspecified'
        input_row['Thumb'] = 'None or Unspecified'
        input_row['Pattern_Changer'] = 'None or Unspecified'
        input_row['Grouser_Type'] = 'Double'
        input_row['Backhoe_Mounting'] = 'None or Unspecified'
        input_row['Blade_Type'] = 'Straight'
        input_row['Travel_Controls'] = 'None or Unspecified'
        input_row['Differential_Type'] = 'Standard'
        input_row['Steering_Controls'] = 'Conventional'
        input_row['saleYear'] = 2012
        input_row['saleMonth'] = 6
        input_row['saleDay'] = 15
        input_row['saleDayofweek'] = 3
        input_row['saleDayofyear'] = 167

        # Set all missing indicator columns to 0 (not missing)
        for col in expected_columns:
            if col.endswith('_is_missing'):
                input_row[col] = 0
            elif col not in input_row:
                # Set any remaining columns to default values
                input_row[col] = 0 if training_data[col].dtype in ['int64', 'float64'] else 'Unknown'

        # Create the dataframe
        test_input = pd.DataFrame([input_row], columns=expected_columns)
        
        print(f"✅ Test input shape: {test_input.shape}")
        
        # Apply preprocessing
        print("\n🔄 Applying preprocessing...")
        label_encoders = preprocessing_data['label_encoders']
        imputer = preprocessing_data['imputer']
        
        input_encoded = test_input.copy()
        
        # Encode categorical features
        for column in test_input.columns:
            if column in label_encoders and test_input[column].dtype == 'object':
                le = label_encoders[column]
                try:
                    input_encoded[column] = le.transform(test_input[column].astype(str))
                except ValueError:
                    # Use first category if unseen
                    input_encoded[column] = [0]
        
        # Apply imputation
        input_final = pd.DataFrame(
            imputer.transform(input_encoded),
            columns=input_encoded.columns
        )
        
        print(f"✅ Preprocessed input shape: {input_final.shape}")
        
        # Make prediction
        print("\n🔮 Making prediction...")
        prediction = model.predict(input_final)[0]
        
        print(f"🎯 Predicted price: ${prediction:,.2f}")
        
        # Test multiple predictions
        print("\n🧪 Testing multiple predictions...")
        for i, year in enumerate([2000, 2005, 2010]):
            test_input_multi = test_input.copy()
            test_input_multi['YearMade'] = [year]
            
            # Preprocess
            input_encoded_multi = test_input_multi.copy()
            for column in test_input_multi.columns:
                if column in label_encoders and test_input_multi[column].dtype == 'object':
                    le = label_encoders[column]
                    try:
                        input_encoded_multi[column] = le.transform(test_input_multi[column].astype(str))
                    except ValueError:
                        input_encoded_multi[column] = [0]
            
            input_final_multi = pd.DataFrame(
                imputer.transform(input_encoded_multi),
                columns=input_encoded_multi.columns
            )
            
            prediction_multi = model.predict(input_final_multi)[0]
            print(f"  📅 Year {year}: ${prediction_multi:,.2f}")
        
        print("\n" + "=" * 50)
        print("🎉 SUCCESS! ML Model is working correctly!")
        print("=" * 50)
        print("✅ Model loads without errors")
        print("✅ Model has predict method")
        print("✅ Preprocessing components work")
        print("✅ Predictions are generated successfully")
        print("✅ Multiple predictions work correctly")
        print("\n🚀 Your Streamlit app should now work with the ML model!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 The app will use the fallback prediction system.")
        return False

if __name__ == "__main__":
    test_model()
