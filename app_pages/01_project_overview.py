import streamlit as st

st.title("BulldozerPriceGenius(BPG)")

st.image("static/images/bulldozer_ai-min.webp")

st.header("Project Overview")

st.subheader(
    "BulldozerPriceGenius BPG: Know Your Equipment's Worth, Make Smarter Auction Decisions."
)

st.write(f"Tired of guessing what your bulldozer is worth? BulldozerPriceGenius (BPG) is revolutionizing heavy equipment valuation with cutting-edge AI technology. In partnership with Fast Iron, we're creating the industry's first Kelly Blue Book equivalent for bulldozers, empowering construction companies and dealers to make data-driven decisions that maximize their returns. Say goodbye to uncertainty and hello to precise, market-informed valuations that put you in control of your equipment's true worth.")

# Link to README file, so the users can have access to full project documentation
st.write(
    f"* For additional information, please visit and **read** the "
    f"[Project README file](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2.git)."
)

# copied from README file - "Business Requirements" section
st.subheader(
    f"Business Requirements:"
)
st.success(
    f"The project has 3 business requirements:\n"
    f"* 1 - The user needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.\n"
    f"* 2 - The user requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.\n"
    f"* 3 - The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.\n"
)

st.subheader(
    f"Project Terms & Jargon:"
)
# text based on README file - "Dataset Content" section
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
st.write(
    f"* For a complete glossary of project terms and jargon, please refer to the Kaggle "
    f"[Data Dictionary file](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
)

st.subheader(
    f"Data Set:"
)

st.info(
    f"**Data Set:**\n"
    f"* The project leverages an extensive dataset of historical bulldozer sales information, carefully sourced from Kaggle's prestigious Bluebook for Bulldozers competition.\n"
    f"* This comprehensive dataset encompasses a wide range of crucial attributes, including detailed model specifications, precise size measurements, accurate sale dates, specific location data, and numerous other relevant parameters.\n"
    f"* The dataset is split into three parts:\n"
    f"* **Train.csv**: Historical sales data up to 2011, used for training the model.\n"
    f"* **Valid.csv**: Sales data from January 1, 2012, to April 30, 2012, used for validating the model's performance..\n"
    f"* **Test.csv**: Sales data from May 1, 2012, to November 2012, used for evaluating the final model. \n"
)

st.write(
    f"* For more information about the dataset used in this project, please refer to  "
    f"[Blue Book for Bulldozers](https://www.kaggle.com/c/bluebook-for-bulldozers/data)."
)
