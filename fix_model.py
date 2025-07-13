#!/usr/bin/env python3
"""
Script to create a proper trained RandomForest model for bulldozer price prediction.
This will replace the current numpy array with a real sklearn model.
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data():
    """Load and prepare the training data"""
    print("📊 Loading training data...")

    # Try parquet first, then CSV
    parquet_path = "src/data_prep/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet"
    csv_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"

    if os.path.exists(parquet_path):
        print(f"✅ Loading from parquet: {parquet_path}")
        data = pd.read_parquet(parquet_path)
    elif os.path.exists(csv_path):
        print(f"✅ Loading from CSV: {csv_path}")
        # Load a reasonable sample for training to avoid memory issues
        data = pd.read_csv(csv_path, nrows=50000)  # Use first 50k rows for training
        print(f"ℹ️ Using sample of 50,000 rows for training")
    else:
        raise FileNotFoundError("No training data found!")

    print(f"📈 Data shape: {data.shape}")
    print(f"📋 Columns: {list(data.columns)}")

    return data

def prepare_features_and_target(data):
    """Prepare features and target variable"""
    print("\n🔧 Preparing features and target...")
    
    # Target variable
    if 'SalePrice' in data.columns:
        target = 'SalePrice'
    elif 'saleprice' in data.columns:
        target = 'saleprice'
    else:
        # Look for any column that might be the target
        price_cols = [col for col in data.columns if 'price' in col.lower()]
        if price_cols:
            target = price_cols[0]
        else:
            raise ValueError("Cannot find target variable (SalePrice)")
    
    print(f"🎯 Target variable: {target}")
    
    # Separate features and target
    y = data[target].copy()
    X = data.drop(columns=[target]).copy()
    
    # Handle missing values in target
    valid_indices = ~y.isna()
    X = X[valid_indices]
    y = y[valid_indices]
    
    print(f"📊 Valid samples: {len(y)}")
    print(f"💰 Price range: ${y.min():,.2f} - ${y.max():,.2f}")
    
    return X, y

def encode_categorical_features(X):
    """Encode categorical features"""
    print("\n🔤 Encoding categorical features...")
    
    X_encoded = X.copy()
    label_encoders = {}
    
    for column in X.columns:
        if X[column].dtype == 'object' or X[column].dtype.name == 'category':
            print(f"  📝 Encoding {column}")
            le = LabelEncoder()
            # Handle missing values
            X_encoded[column] = X_encoded[column].fillna('Unknown')
            X_encoded[column] = le.fit_transform(X_encoded[column].astype(str))
            label_encoders[column] = le
    
    # Handle remaining missing values with median imputation
    imputer = SimpleImputer(strategy='median')
    X_encoded = pd.DataFrame(
        imputer.fit_transform(X_encoded),
        columns=X_encoded.columns,
        index=X_encoded.index
    )
    
    print(f"✅ Final feature shape: {X_encoded.shape}")
    
    return X_encoded, label_encoders, imputer

def train_random_forest(X, y):
    """Train a RandomForest model"""
    print("\n🌲 Training RandomForest model...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"📊 Training set: {X_train.shape[0]} samples")
    print(f"📊 Test set: {X_test.shape[0]} samples")
    
    # Train model
    rf_model = RandomForestRegressor(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    print("🔄 Training in progress...")
    rf_model.fit(X_train, y_train)
    
    # Evaluate model
    train_pred = rf_model.predict(X_train)
    test_pred = rf_model.predict(X_test)
    
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    
    print(f"\n📈 Model Performance:")
    print(f"  🎯 Training R²: {train_r2:.4f}")
    print(f"  🎯 Test R²: {test_r2:.4f}")
    print(f"  📏 Training RMSE: ${train_rmse:,.2f}")
    print(f"  📏 Test RMSE: ${test_rmse:,.2f}")
    
    return rf_model, (train_r2, test_r2, train_rmse, test_rmse)

def save_model_and_metadata(model, label_encoders, imputer, performance_metrics):
    """Save the trained model and preprocessing components"""
    print("\n💾 Saving model and metadata...")
    
    # Create models directory if it doesn't exist
    os.makedirs("src/models", exist_ok=True)
    
    # Save the main model
    model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"✅ Model saved to: {model_path}")
    
    # Save preprocessing components
    preprocessing_path = "src/models/preprocessing_components.pkl"
    preprocessing_data = {
        'label_encoders': label_encoders,
        'imputer': imputer,
        'performance_metrics': performance_metrics
    }
    
    with open(preprocessing_path, 'wb') as f:
        pickle.dump(preprocessing_data, f)
    
    print(f"✅ Preprocessing components saved to: {preprocessing_path}")
    
    # Test loading the saved model
    print("\n🧪 Testing saved model...")
    with open(model_path, 'rb') as f:
        loaded_model = pickle.load(f)
    
    print(f"✅ Model type: {type(loaded_model)}")
    print(f"✅ Has predict method: {hasattr(loaded_model, 'predict')}")
    
    # Test prediction
    if hasattr(loaded_model, 'predict'):
        # Create a dummy feature vector
        dummy_features = np.zeros((1, model.n_features_in_))
        dummy_prediction = loaded_model.predict(dummy_features)
        print(f"✅ Test prediction successful: ${dummy_prediction[0]:,.2f}")
    
    return model_path, preprocessing_path

def main():
    """Main function to create and save the model"""
    print("🚜 **Creating Proper RandomForest Model for Bulldozer Price Prediction**")
    print("=" * 80)
    
    try:
        # Load and prepare data
        data = load_and_prepare_data()
        X, y = prepare_features_and_target(data)
        X_encoded, label_encoders, imputer = encode_categorical_features(X)
        
        # Train model
        model, performance_metrics = train_random_forest(X_encoded, y)
        
        # Save everything
        model_path, preprocessing_path = save_model_and_metadata(
            model, label_encoders, imputer, performance_metrics
        )
        
        print("\n" + "=" * 80)
        print("🎉 **SUCCESS! Model created and saved successfully!**")
        print("=" * 80)
        print(f"📁 Model file: {model_path}")
        print(f"📁 Preprocessing file: {preprocessing_path}")
        print(f"🎯 Test R²: {performance_metrics[1]:.4f}")
        print(f"📏 Test RMSE: ${performance_metrics[3]:,.2f}")
        print("\n✅ Your Streamlit app should now work with the proper model!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 **Fallback: The app will continue to use the statistical estimation system.**")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🚀 **Next steps:**")
        print("1. Run your Streamlit app: streamlit run app.py")
        print("2. Navigate to the 'Interactive Prediction' page")
        print("3. You should now see '✅ Advanced ML Model loaded successfully!'")
    else:
        print("\n💡 **Don't worry!** The app will still work with the backup prediction system.")
