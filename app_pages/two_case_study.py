import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv_file_path):
    return pd.read_csv(csv_file_path)

def case_study_body():
    st.header("Case Study")
    st.subheader("Exploratory Data Analysis (EDA)")
    st.write(
        """
        The BulldozerPriceGenius app aims to help users understand the factors that influence bulldozer prices. The project has two main data science objectives under **Business Requirements**:
        """
    )
    # Display the main business goals of the project
    st.success(
        """
        - **Objective 1**: Analyze the distribution of sale prices to understand how bulldozer values are spread out
        - **Objective 2**: Study sales patterns over time to identify any seasonal trends or recurring patterns in bulldozer pricing
        """
    )
    
    st.write(
        """
        Through these analyses, the project will provide insights that help users better understand what drives bulldozer market values.
        """
    )

    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(csv_file_path)

    if st.checkbox("Inspect dataframe"):
        st.dataframe(df)
        
    st.subheader("View SalePrice distribution")
    st.write(
        """
        A histogram serves as our primary visualization tool for understanding bulldozer price distributions, directly meeting Objective 1 of analyzing price distribution patterns. This straightforward yet powerful graph helps us analyze how sale prices are spread across different ranges, revealing key patterns in our dataset.
        """
    )

    if st.checkbox("Visualize Sale Price Distribution Histogram"):
        st.write(
            """
            **What to Look For:**

            - Shape of distribution - whether prices are evenly spread out or clustered around certain values
            - Price ranges - identify the most common price points and any outliers
            - Skewness - whether prices tend to lean towards higher or lower values

            **Business Value:**

            - Helps understand typical price ranges for bulldozers
            - Identifies unusual or extreme prices that might need investigation
            - Provides insights for pricing strategies and market analysis

            This analysis is fundamental for understanding the target variable in this regression problem, which will help achieve the business requirement of understanding what influences bulldozer prices.
            """
        )
        fig, ax = plt.subplots()
        df.SalePrice.plot.hist(ax=ax, xlabel="Sale Price ($)")
        st.pyplot(fig)

    st.subheader("View Median SalePrice by Month")
    st.write(
        """
        The line plot visualization displays median bulldozer prices across different months, showing clear price trends over time. This visual representation helps us easily spot monthly pricing patterns and identify any seasonal fluctuations in the market, fulfilling objective 2 of exploring sales trends over time. Through this analysis, we can better understand when bulldozer prices tend to rise or fall throughout the year, providing valuable insights into market seasonality.
        """
    )

    if st.checkbox("Visualize Median Sale Price by Month"):
        st.write(
            """
            **What to Look For:**

            - Seasonal trends - identify any recurring patterns in prices over different months
            - Price fluctuations - observe how prices change over time

            **Business Value:**

            - Helps understand seasonal trends in bulldozer prices
            - Provides insights for inventory and sales strategies
            """
        )
        fig, ax = plt.subplots()
        df.groupby(["saleMonth"])["SalePrice"].median().plot(ax=ax)
        ax.set_xlabel("Month")
        ax.set_ylabel("Median Sale Price ($)")
        st.pyplot(fig)

    st.subheader("View SalePrice against SaleMonth (First 10,000 samples)")
    st.write(
        """
        A scatter plot displaying the first 10,000 samples of sale prices plotted against sale months addresses the second objective. This visualization clearly reveals the relationship between when bulldozers were sold and their prices. The pattern of scattered points helps identify any seasonal trends or price fluctuations over time.
        """
    )

    if st.checkbox("Visualize Sale Price against Sale Month (First 10,000 samples)"):
        fig, ax = plt.subplots()
        ax.scatter(x=df["saleMonth"][:10000], y=df["SalePrice"][:10000])
        ax.set_xlabel("Sale Month")
        ax.set_ylabel("Sale Price ($)")
        st.pyplot(fig)

    st.subheader("View Median SalePrice by State")
    st.write(
        """
        A bar plot showing median bulldozer prices across different states helps meet objective 2 of our analysis. This visualization clearly highlights geographic price differences and can help identify how regional market conditions and seasonal patterns affect sales prices in different locations. By comparing each state's median price to the overall median, we can gain valuable insights into regional pricing strategies and market trends.
        """
    )

    if st.checkbox("Visualize Median Sale Price by State"):
        st.write(
            """
            **What to Look For:**

            - Median prices by state - identify which states have higher or lower median prices
            - Comparison to overall median - see how each state's median price compares to the overall median

            **Business Value:**

            - Helps understand regional price differences
            - Provides insights for regional pricing strategies
            """
        )
        median_prices_by_state = df.groupby(["state"])["SalePrice"].median()
        median_sale_price = df["SalePrice"].median()

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.bar(x=median_prices_by_state.index, height=median_prices_by_state.values)
        ax.set_xlabel("State")
        ax.set_ylabel("Median Sale Price ($)")
        plt.xticks(rotation=90, fontsize=7)
        ax.axhline(y=median_sale_price, color="red", linestyle="--", label=f"Median Sale Price: ${median_sale_price:,.0f}")
        ax.legend()
        st.pyplot(fig)