# Import the Streamlit library which we'll use to create our web app
import streamlit as st

# Set the main title of the web app
st.title("BulldozerPriceGenius(BPG)")

# Display the logo/header image
st.image("static/images/bulldozer_ai-min.webp")

# Add a main header for the overview section
st.header("Project Overview")

# Add a subtitle that explains the app's purpose in one line
st.subheader(
    "BulldozerPriceGenius BPG: Know Your Equipment's Worth, Make Smarter Auction Decisions."
)

# Brief description of what the app does
st.write(f"BulldozerPriceGenius helps predict how much bulldozers will sell for at auctions. It uses data from past sales on Kaggle to make accurate price predictions, helping buyers and sellers make better decisions in the construction equipment market.")

# Add a link to documentation for users who want more details
st.write(
    f"* For additional information, please visit and **read** the "
    f"[Project README file](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2.git)."
)

# Display the main business goals of the project
st.subheader(
    f"Business Requirements:"
)
st.success(
    f"The project has 3 business requirements:\n"
    f"* 1 - The user needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.\n"
    f"* 2 - The user requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.\n"
    f"* 3 - The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.\n"
)

# Define important terms so users understand the industry language
st.subheader(
    f"Project Terms & Jargon:"
)

# List of key terms and their definitions
st.info(
    f"**Project Terms & Jargon:**\n"
    f"* **AuctioneerID**: The company that conducted the auction sale (different from data source).\n"
    f"* **Bluebook**: A pricing guide used in the heavy equipment industry that provides estimated values for machinery like bulldozers. Similar to Kelley Blue Book for cars.\n"
    f"* **Data Source**: Where the sale information came from (some sources provide more detailed information than others).\n"
    f"* **MachineID**: A unique number for each bulldozer (note: one bulldozer can be sold multiple times).\n"
    f"* **Machine Hours**: How many hours the bulldozer has been used when sold (if recorded).\n"
    f"* **ModelID**: A unique number that identifies the specific model of bulldozer.\n"
    f"* **Sale Date**: When the bulldozer was sold.\n"
    f"* **Sale Price**: How much the bulldozer sold for in US dollars.\n"
    f"* **Usage Band**: How much the bulldozer has been used compared to similar models (low, medium, or high).\n"
    f"* **User**: A person who interacts with the software application - typically auctioneers, buyers, or sellers.\n"
    f"* **Year Made**: The year the bulldozer was manufactured.\n"
)

# This helps users understand the technical terminology
st.write(
    f"* For a complete glossary of project terms and jargon, please refer to the Kaggle "
    f"[Data Dictionary file](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
)

# Explain where our data comes from and how it's organized
st.subheader(
    f"Data Set:"
)

# Description of the dataset and its different parts
# Shows users what information we're using to make predictions
st.info(
    f"**Data Set:**\n"
    f"* The project leverages an extensive dataset of historical bulldozer sales information, carefully sourced from Kaggle's prestigious Bluebook for Bulldozers competition.\n"
    f"* This comprehensive dataset encompasses a wide range of crucial attributes, including detailed model specifications, precise size measurements, accurate sale dates, specific location data, and numerous other relevant parameters.\n"
    f"* The dataset is split into three parts:\n"
    f"* **Train.csv**: Historical sales data up to 2011, used for training the model.\n"
    f"* **Valid.csv**: Sales data from January 1, 2012, to April 30, 2012, used for validating the model's performance..\n"
    f"* **Test.csv**: Sales data from May 1, 2012, to November 2012, used for evaluating the final model. \n"
)

# Add a link for users who want to learn more about the data
st.write(
    f"* For more information about the dataset used in this project, please refer to  "
    f"[Blue Book for Bulldozers](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
)
