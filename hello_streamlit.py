import streamlit as st

# Add a title
st.title("My First Streamlit App")

# Add some text
st.write("Hello! This is a test app.")

# Add a parameter from command line args
import sys
if len(sys.argv) > 1:
    st.write("Command line arguments:", sys.argv[1:])
else:
    st.write("No command line arguments provided")
