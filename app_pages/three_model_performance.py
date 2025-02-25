import streamlit as st
import joblib

# Load the best model
bulldozer_price_prediction_model_name = 'path_to_your_model_file.pkl'  # Update with your model file path
best_model = joblib.load(filename=bulldozer_price_prediction_model_name)

# Display the model
st.write("Model loaded successfully:")
st.write(best_model)

# Display model attributes
st.write("Model attributes:")
st.write(dir(best_model))

# Make a simple prediction (assuming the model has a predict method and you have sample input data)
sample_input = [[2025, 1000, 3]]  # Replace with appropriate sample input for your model
if hasattr(best_model, 'predict'):
    prediction = best_model.predict(sample_input)
    st.write("Sample prediction for input {}: {}".format(sample_input, prediction))
else:
    st.write("The model does not have a predict method.")