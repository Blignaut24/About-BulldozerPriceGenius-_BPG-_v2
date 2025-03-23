# BulldozerPriceGenuis (BPG)

#### "**BulldozerPriceGenuis (BPG)**: _Know Your Equipment's Worth, Make Smarter Auction Decisions_

<img src="static/images/bulldozer_ai-min.webp" width="40%" style="display: block; margin: 0 auto;">

In the complex world of heavy equipment auctions, construction companies and dealers face a persistent challenge: accurately determining the value of their bulldozers. The uncertainty can lead to missed opportunities and financial losses.

Enter BulldozerPriceGenius (BPG), your trusted partner in bulldozer valuation. We've developed an advanced AI-powered system that leverages data analysis to predict auction prices with precision. Our user-friendly interface allows you to browse and filter bulldozer listings across U.S. states, with predicted sale prices in USD. By analyzing comprehensive datasets from real auctions and considering crucial factors like equipment usage, features, location, and market conditions, we eliminate the guesswork from pricing.

In collaboration with Fast Iron, we're revolutionizing the industry by creating the equivalent of a Kelly Blue Book for bulldozers. This means you can now:

- Make confident pricing decisions backed by data
- Browse and filter listings by location and predicted price
- Understand your equipment's true market value
- Optimize your auction strategy for maximum returns

#### _"Stop leaving money on the table. Let BulldozerPriceGenius transform your uncertain pricing decisions into data-driven success stories."_

# Table of Content


- [BulldozerPriceGenuis (BPG)](#bulldozerpricegenuis-bpg)
      - ["**BulldozerPriceGenuis (BPG)**: _Know Your Equipment's Worth, Make Smarter Auction Decisions_](#bulldozerpricegenuis-bpg-know-your-equipments-worth-make-smarter-auction-decisions)
      - [_"Stop leaving money on the table. Let BulldozerPriceGenius transform your uncertain pricing decisions into data-driven success stories."_](#stop-leaving-money-on-the-table-let-bulldozerpricegenius-transform-your-uncertain-pricing-decisions-into-data-driven-success-stories)
- [Table of Content](#table-of-content)
- [Introduction](#introduction)
- [Dataset Content 💾](#dataset-content-)
- [Project Terms \& Jargon 📖](#project-terms--jargon-)
  - [Prediction-Related Terms](#prediction-related-terms)
  - [Data Organization](#data-organization)
  - [Technical Tools](#technical-tools)
  - [File Types](#file-types)
- [Business Context 👔](#business-context-)
- [Business Requirements 💼](#business-requirements-)
- [ML Business Case (10 Key Components) 🧩](#ml-business-case-10-key-components-)
  - [1. What is the business objective requiring a ML solution?](#1-what-is-the-business-objective-requiring-a-ml-solution)
  - [2. Can traditional data analysis be used?](#2-can-traditional-data-analysis-be-used)
  - [3. Does the customer need a dashboard or an API endpoint?](#3-does-the-customer-need-a-dashboard-or-an-api-endpoint)
  - [4. What does success look like?](#4-what-does-success-look-like)
    - [1. Model Accuracy](#1-model-accuracy)
    - [2. Market Performance](#2-market-performance)
    - [3. Business Impact](#3-business-impact)
  - [5. Can you break down the project into Epics and User Stories?](#5-can-you-break-down-the-project-into-epics-and-user-stories)
  - [6. Ethical or Privacy concerns?](#6-ethical-or-privacy-concerns)
  - [7. What level of prediction performance is needed?](#7-what-level-of-prediction-performance-is-needed)
  - [8. What are the project inputs and intended outputs?](#8-what-are-the-project-inputs-and-intended-outputs)
  - [9. Does the data suggest a particular model?](#9-does-the-data-suggest-a-particular-model)
  - [10. How will the customer benefit?](#10-how-will-the-customer-benefit)
- [Project Hypothesis and Validation 📽️](#project-hypothesis-and-validation-️)
  - [Hypothesis](#hypothesis)
  - [Validation Approach](#validation-approach)
    - [Data Splitting Strategy](#data-splitting-strategy)
    - [Performance Measurement: How We Measure Success?](#performance-measurement-how-we-measure-success)
    - [Model Evaluation Process](#model-evaluation-process)
- [The rationale to map the business requirements to the Data Visualizations and ML tasks 🗺️](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks-️)
    - [Price Prediction](#price-prediction)
    - [Market Trends](#market-trends)
    - [Smart Pricing](#smart-pricing)
  - [How Our Tools Help Us](#how-our-tools-help-us)
- [Epics and User Stories 📜](#epics-and-user-stories-)
- [Dashboard Design (Streamlit App User Interface) 🎨](#dashboard-design-streamlit-app-user-interface-)
  - [Page 1](#page-1)
  - [Page 2](#page-2)
  - [Page 3](#page-3)
  - [Page 4](#page-4)
  - [Page 5](#page-5)
- [Tools 🛠️](#tools-️)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Other Technologies](#other-technologies)
- [Testing 🧪](#testing-)
  - [Manual Testing](#manual-testing)
  - [Validation](#validation)
  - [Automated Unit Tests](#automated-unit-tests)
- [Bug Reports 🐞](#bug-reports-)
  - [Known bugs ❌](#known-bugs-)
  - [Fixed bugs ✅](#fixed-bugs-)
- [Deployment 🚢](#deployment-)
  - [Git LFS Setup Guide](#git-lfs-setup-guide)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [For Existing Projects](#for-existing-projects)
    - [Important Notes](#important-notes)
  - [Heroku](#heroku)
  - [Forking and Cloning](#forking-and-cloning)
- [Credits ⭐](#credits-)
  - [Content](#content)
  - [Tutorials](#tutorials)
  - [Media](#media)
- [Acknowledgements 📢](#acknowledgements-)


# Dataset Content 💾

- The project leverages an extensive dataset of historical bulldozer sales information, carefully sourced from [Kaggle's prestigious Bluebook for Bulldozers competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview).
- This comprehensive dataset encompasses a wide range of crucial attributes, including detailed model specifications, precise size measurements, accurate sale dates, specific location data, and numerous other relevant parameters.
- For an exhaustive understanding of the data structure, please consult the comprehensive [data dictionary](https://www.kaggle.com/c/bluebook-for-bulldozers/data?select=Data+Dictionary.xlsx) available on the Kaggle competition page.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Project Terms & Jargon 📖
Here are the main terms you'll encounter in this project:

## Prediction-Related Terms

- **Regression**: Making predictions about numbers (like guessing house prices).
- **Time Series**: Using past information to predict future events (like weather forecasting).
- [**Mean Squared Log Error (RMSLE)**](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle): A way to measure how accurate our predictions are.
- [**Mean Absolute Error (MAE)**](https://www.kaggle.com/discussions/general/413103): A way to measure how accurate our predictions are.
- [**R² Score (Coefficient of Determination)**](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html): R² Score tells us how well our model predicts prices. It shows how much of the price differences can be explained by the features we used in our model.


## Data Organization

- **Data Dictionary**: A guide that explains what each piece of information means.
- **Target Variable**: What we're trying to predict (in this case, bulldozer prices).
- **Independent Variables**: The information we use to make predictions (like age or model of bulldozer).
- [**Feature Engineering**](https://www.kaggle.com/learn/feature-engineering): Creating new useful information from existing data.
- [**Correlation Analysis**](https://www.geeksforgeeks.org/what-is-correlation-analysis/): Studied how different features relate to each other to find which ones are closely connected and overlapping.
- [**Linear Regression**](https://www.kaggle.com/code/sudhirnl7/linear-regression-tutorial): Is a statistical method that predicts one value based on another by finding the best straight line that fits through all the data points.

## Technical Tools

- **Datetime**: A way to work with dates and times in Python
- [**Model Driven Data Exploration(EDA)**](https://www.ibm.com/think/topics/exploratory-data-analysis): Looking at data to understand patterns (like making charts and graphs).
- [**Random Forest**](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html): A powerful prediction tool that combines multiple simpler predictions.
- **NaN**: Stands for "Not a Number" - used when data is missing
- [**Recursive Feature Elimination (RFE)**](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html): A feature selection method that recursively removes less important features by training a model (like Random Forest) and ranking features based on their importance scores. It helps identify the most relevant features for prediction.
- [**Principal Component Analysis (PCA)**](https://www.kaggle.com/code/ryanholbrook/principal-component-analysis): A method that takes complex data and makes it simpler by reducing the number of variables while keeping the most important information. It helps find patterns in data and makes it easier to work with.
- [**Feature Selection**](https://www.kaggle.com/code/prashant111/comprehensive-guide-on-feature-selection): Used two methods to pick out the most important features for our model: RFE (which removes less useful features one by one) and PCA (which combines features to find the most important patterns in the data).
- [**Hyperparameter Tuning**](https://www.kaggle.com/code/shreayan98c/hyperparameter-tuning-tutorial): Is the process of finding the best settings for a machine learning model, similar to adjusting the knobs on a radio to get the clearest signal.
- [**Decision Trees**](https://www.kaggle.com/code/satishgunjal/tutorial-decision-tree): A decision tree is like a flowchart that makes predictions by following a series of yes/no questions about your data, similar to how you might make decisions in a game of "20 Questions".
- [**Feature Importance**](https://www.kaggle.com/code/raskoshik/feature-importance-how-not-fool-yourself): Helps us understand which characteristics of our data have the strongest influence on predictions, like identifying which parts of a recipe contribute most to its taste.

## File Types

- **CSV**: A simple file type that stores data in a table format
- **Parquet**: A more advanced file type that saves space and works quickly
- **Feather**: Another fast file type for storing data

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Business Context 👔
 Bulldozer auctions generate significant revenue in the construction and heavy machinery industry. Accurate price predictions are crucial for both buyers and sellers to make informed decisions. A fictional auction company has requested a data practitioner to analyze historical auction data to determine key price factors and develop a prediction system for future auctions.

 <p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Business Requirements 💼
• [**Business Requirement 1**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Business+Requirement&pane=issue&itemId=97853714&issue=Blignaut24%7CAbout-BulldozerPriceGenius-_BPG-_v2%7C10) - The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.

• [**Business Requirement 2**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Business+Requirement&pane=issue&itemId=97854211&issue=Blignaut24%7CAbout-BulldozerPriceGenius-_BPG-_v2%7C11) - The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data with a **Root Mean Squared Log Error (RMSLE)** score of below `1`.

• [**Business Requirement 3**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Business+Requirement&pane=issue&itemId=97854418&issue=Blignaut24%7CAbout-BulldozerPriceGenius-_BPG-_v2%7C12) - The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

#  ML Business Case (10 Key Components) 🧩 

## 1. What is the business objective requiring a ML solution?
    
The primary business objective is to develop an AI-powered system that accurately predicts bulldozer auction prices. By analyzing historical sales data and equipment specifications, this solution aims to:
    
  - **Key Business Benefits:**
    - Enable data-driven buying and selling decisions
    - Optimize auction pricing strategies
    - Minimize financial risks in transactions
    
    Machine learning is essential for this objective due to four critical factors:
    
    - **Pattern Complexity:** The system must analyze numerous variables and non-linear relationships that traditional methods cannot handle effectively
    - **Data Volume:** Processing 400,000+ records requires ML's superior computational efficiency compared to conventional analysis
    - **Dynamic Learning:** ML algorithms can continuously adapt to new auction data, ensuring sustained accuracy
    - **Advanced Prediction:** Only machine learning can deliver the high-precision price forecasting needed for this application
    
## 2. Can traditional data analysis be used?  
Traditional data analysis plays a vital role in this project through two main components:
    
- **Data Exploration and Understanding**
  - Analyzing patterns and relationships in the data
  - Identifying key price influences through statistical analysis
  - Visualizing relationships between features and prices
- **Data Preparation and Quality**
  - Cleaning and standardizing data
  - Creating meaningful features from raw data
  - Optimizing data structures for efficiency
    
While traditional analysis provides essential insights, it's not enough on its own. Machine learning techniques, particularly Random Forest Regression, are needed to capture complex pricing patterns and make accurate predictions.
    
This hybrid approach combines the interpretability of traditional analysis with the predictive power of machine learning.
    
## 3. Does the customer need a dashboard or an API endpoint? 
Based on the business requirements and stakeholder needs, we recommend implementing a comprehensive dashboard solution that offers:
    
  - **Interactive Visualization:** - A user-friendly interface that 
    displays bulldozer listings, which can be filtered by predicted sale prices (in USD) and locations across U.S. states
  - **Data-Driven Insights:** Clear, intuitive display of key pricing 
    factors that justify predicted sale prices
  - **Cross-Team Accessibility:** An intuitive interface suitable for
    both technical and business users, supporting collaborative decision-making

## 4. What does success look like?
Success metrics for this project include:
  - Success is measured by achieving accurate price predictions, which 
    we evaluate using the **Root Mean Squared Log Error (RMSLE)** metric.
  - **Success target**: RMSLE below 1.0.
  - Measures how closely predicted prices match actual sale prices 
    using **Mean Absolute Error (MAE)**.
  
    
## 5. Can you break down the project into Epics and User Stories?
  
  Yes, the project can be broken down into [Epics and User Stories](https://github.com/users/Blignaut24/projects/23/views/2).
    
## 6. Ethical or Privacy concerns?
    
  No, there are no ethical or privacy concerns about this data as it is fictitious data from a [Kaggle competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview). 
    
## 7. What level of prediction performance is needed?
    
  We use Root Mean Squared Log Error (RMSLE) as our key performance metric, with a target of achieving an RMSLE below 1.00 to ensure highly accurate price predictions. Our secondary metric is Mean Absolute Error (MAE), where we aim to keep the difference between predicted and actual bulldozer prices within $20,000 in the Model's Performance Analysis. 

**Why RMSLE?**

  We chose RMSLE because it works well with our wide range of bulldozer prices and puts more emphasis on avoiding price underestimation, which is crucial for our business case.

**Why MAE?**

  Using Mean Absolute Error (MAE) as a secondary metric in BulldozerPriceGenius is beneficial because it shows the average difference between predicted and actual prices in dollar terms. This makes it very intuitive and easy to understand for business stakeholders, as seeing that predictions are within $20,000 of actual prices provides a clear, concrete measure of accuracy that anyone can grasp.

  Additionally, MAE is particularly useful because:

  - It provides a more interpretable measure of error in the actual currency units (USD)
  - It helps validate the model's practical business value by showing the typical margin of error in dollar terms
  - It complements the primary RMSLE metric by offering a different perspective on model performance
    
## 8. Project Inputs and Outputs

- **Input Features:**
  - Equipment specifications (year, model, series)
  - Sale conditions and location (U.S. states)
  - Technical specifications (engine, hours, condition)

- **User Interface:**
  - Interactive visualization dashboard
  - Filterable listings by location and price range
  - User-friendly display of bulldozer information

- **Model Output:**
  - Predicted auction price in USD
  - Price filtering capabilities
  - Location-based search across U.S. states

- **Workflow:**
  - User selects desired filters and parameters
  - System processes equipment details
  - Interface displays filtered results with predictions
## 9. Does the data suggest a particular model?
  - **Data Characteristics:**
    - Regression problem with continuous price predictions
    - Large dataset (400,000+ samples)
    - Mixed numerical and categorical features
    - Contains missing values
  - **Suggested Model: Random Forest Regressor**
      - Handles mixed data types effectively
      - Robust against missing values
      - Performs well on large datasets
      - Captures complex pricing patterns
## 10. How will the customer benefit?
The customer will benefit in several key ways:
    
- **Financial Benefits**
      - More accurate pricing decisions
      - Reduced risk of over/underpaying
      - Potential for increased profits
- **Operational Improvements**
      - Data-driven decision making
      - Faster transaction processes
      - Better market understanding
- **Market Advantages**
      - Greater market transparency
      - More efficient negotiations
      - Improved buyer-seller confidence 


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Project Hypothesis and Validation 📽️ 

## Addressing Business Requirement 1:
By proving or disproving these hypotheses, the client can gain a deeper understanding of the factors that significantly influence bulldozer auction prices. This knowledge can be applied to:

- **Optimize auction strategies:** Adjust auction timing, location, and marketing based on factors that drive higher prices.
- **Provide better guidance:** Inform sellers about optimal listing strategies and advise buyers on fair market value estimations.
- **Enhance transparency:** Provide data-driven insights to both sellers and buyers, improving the overall auction experience.

### Hypothesis 1: Age and Usage Impact on Bulldozer Pricing
**Hypothesis:** We believe that two main factors have the biggest impact on bulldozer prices at auctions:

- How old the bulldozer is (when it was made)?
- How much it has been used (total hours of operation)?

**Why we think this:** When buying used heavy machinery like bulldozers, people usually care most about the machine's age and how much it has been used. We can check this by looking at the relationship between these factors and the selling price.

**Validation**: To check this hypothesis, we will:  

1. Train our machine learning model (Random Forest)
2. Look at which features are most important for predicting prices
3. Pay special attention to two main factors:
    - When the bulldozer was made (`YearMade`)
    - How many hours it has been used (`MachineHoursCurrentMeter`)
4. Create bar charts to show how important each factor is in determining the price

### Hypothesis 2: Regional Price Variations Across States
**Hypothesis:** We believe that bulldozer prices change depending on which state they're sold in. **Why we think this:** Different states have their own local markets, and prices can vary because:

- Some states have more people wanting to buy bulldozers
- Each state uses bulldozers for different kinds of work
- States have different economic conditions that affect what buyers can spend

**Validation:** Group sales data by state and analyze the median selling prices for each location. Create visualizations (such as bar graphs or box plots) to identify patterns in bulldozer prices across different states.

## Addressing Business Requirement 2:
By successfully proving this hypothesis, the client gains confidence in the accuracy, scalability, and adaptability of the machine learning system for predicting bulldozer prices. This system can then be integrated into their auction processes to:

- **Provide accurate price estimations:** Enable informed decision-making for buyers and sellers.
- **Automate price recommendations:** Streamline the price setting process for auction listings.
- **Enhance efficiency:** Reduce manual effort and improve operational efficiency in the auction process.

### Hypothesis 3: Model Generalization and Temporal Robustness

**Hypothesis:** We want to make sure our price prediction system works well even with new data. To test this, we'll check if it can accurately predict prices using data collected after we trained the system. **Why this matters:** This shows whether our system can keep making good predictions as we get new bulldozer data over time.

**Validation**: We will evaluate the model's performance using a separate test dataset (like the Kaggle test dataset). By comparing the model's accuracy on both test and validation data, we can determine whether it reliably predicts prices for new, unseen bulldozer data.

**Data Splitting Strategy**

- `Training set`: Model learning
- `Validation set`: Parameter tuning and performance assessment
- `Test set`: Final evaluation of real-world prediction capability



<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# The rationale to map the business requirements to the Data Visualizations and ML tasks 🗺️

## **Business Requirement 1:** Understand factors influencing bulldozer auction prices.

- **Data Visualizations:**
    - **Feature Importance Bar Chart:** This chart will show which features are most important in determining bulldozer prices (like year made, etc.) — this makes it easy to see what affects the price the most.
    - **Scatter Plots:** These plots show how features like the sale date relate to bulldozer prices. For example, a scatter plot of sale dates against prices helps visualize price trends over time, with each point representing an individual sale transaction.

- **ML tasks:**
    - **Feature Engineering:** Creating helpful combinations of existing data (for example, we can combine when a machine was made and how many hours it was used to figure out how old it is). This helps us better understand what affects bulldozer prices.
    - **Feature Selection:** Choosing which details about the bulldozers are most helpful for predicting prices. We do this by using special tools that tell us which features matter most, like how old the bulldozer is or what brand it is.
    - **Model Training:** Teaching our computer system to predict bulldozer prices by showing it lots of past sales examples. We use a special method called Random Forest that helps the system learn what makes prices go up or down.

**Reasoning:**

By visualizing the data and using ML tasks to analyze feature importance and relationships, we can help the client understand the key factors driving bulldozer auction prices. This information can be used to optimize auction strategies and provide better guidance to sellers and buyers.

## **Business Requirement 2:** Accurate price prediction system using historical data.

- **Data Visualizations:**
    - **Bar Chart with Median Line:** A bar chart with median line visualization displays performance metrics, making it easy to identify which items perform above or below the average benchmark.
    - **Tables:** Help us organize information neatly and make it easier to spot patterns. For example, a Model Comparison Table shows key performance metrics (RMSLE, R-squared, MAE) for different models side by side, making it simple to compare their effectiveness and select the best algorithm for price prediction.
- **ML tasks:**
    - **Model Selection:** Choosing the most appropriate regression model based on the characteristics of the dataset and the desired performance metrics (e.g., RMSLE).
    - **Model Evaluation:** Assessing the model's performance using metrics such as RMSLE and R-squared to quantify its accuracy and reliability.
    - **Model Deployment and Monitoring:** Putting the model into real-world use and keeping track of how well it's working, so we can make sure it stays accurate as we get new bulldozer data.

**Reasoning:**

By using ML tasks to build and evaluate a robust prediction model and visualizing its performance, we can meet the client's requirement for an accurate and scalable price prediction system. This will enable the client to make informed decisions based on data-driven insights.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## ML Business Case 💼

**Business Objective:** Develop an AI-powered system to predict bulldozer auction prices by analyzing historical sales data and equipment specifications.

**Key Benefits:**

- Enable data-driven buying and selling decisions
- Optimize auction pricing strategies
- Minimize financial risks in transactions

**Technical Solution:**

- **Random Forest Regression model** to handle mixed data types and missing values
- Dataset includes 400,000+ records with equipment specifications, sale conditions, and technical details

**Success Metrics:**

- **Primary:** Root Mean Squared Log Error (RMSLE) below `1.0`
- **Secondary:** Mean Absolute Error (MAE) within `$20,000` of actual prices

**Delivery Method:** Comprehensive dashboard with:

- Interactive visualization interface
- Data-driven insights display
- Access for both technical and non-technical users

**Data Privacy:** No ethical or privacy concerns as data is from a public Kaggle competition.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

#  Epics and User Stories 📜
The project was divided into 5 Epics covering Data Analysis and Machine Learning tasks. User stories were created within each Epic to implement an agile methodology in the [Git project](https://github.com/users/Blignaut24/projects/23/views/1).

## [**Epic 1 - Data Ingestion and Preprocessing**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Epic+1)

• **User Story** - As a data scientist, I can ingest the bulldozer sales data from a CSV file so that it's available for analysis and modeling. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can create new features from the 'saledate' column to enhance model training capabilities. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can handle missing values in the dataset to ensure data quality for modeling. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can convert categorical string columns to numerical representations for machine learning compatibility. (**Business Requirement 2**)

## [**Epic 2 - Exploratory Data Analysis (EDA)**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Epic+2)

• **User Story** - As a data scientist, I can visualize the distribution of the SalePrice column to understand the target variable characteristics (**Business Requirement 1**).

• **User Story** - As a data scientist, I can explore sales trends over time to identify patterns and seasonality in the data (**Business Requirement 1**).

## [**Epic 3 - Machine Learning Modeling**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Epic+3%3A+Mac)

• **User Story** - As a data scientist, I can train a Random Forest Regression model to predict bulldozer sale prices (**Business Requirement 2**).

• **User Story** - As a data scientist, I can evaluate model performance to ensure accurate price predictions (**Business Requirement 2**).

• **User Story** - As a data scientist, I can save the trained model for future use and deployment. (**Business Requirement 2**)

## [**Epic 4 - Dashboard Planning, Designing, and Development**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Epic+4+-)
• **User Story** - As a bulldozer auction participant, I can filter bulldozer listings by price and location so that I can quickly find relevant equipment within my budget and preferred region. (**Business Requirement 3**).



## [**Epic 5 - Dashboard Deployment and Release**](https://github.com/users/Blignaut24/projects/23/views/2?filterQuery=Epic+5+-)
- **User Story** - As a user interested in bulldozer pricing
I can access and interact with the BulldozerPriceGenius dashboard through a Streamlit app deployed on Heroku
So that I can explore price predictions and market insights without installing any software locally. (**Business Requirement 3**).

- **User Story** - As a technical user, I can follow instructions in the readme to fork the repository and deploy the project for myself.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


#  Dashboard Design (Streamlit App User Interface) 🎨
The BulldozerPriceGenius dashboard is structured to serve both technical and non-technical users effectively:

**For Non-Technical Users:**

- **Page 1 (Case Study)**: Provide comprehensive overview of BulldozerPriceGenius project and its business context
- **Page 4 (Interactive Prediction)**: Interactive Dashboard for Bulldozer Price Analysis

**For Technical Users:**

- **Page 2 (Hypothesis And Validation)**:  Validate model performance and provide data-driven insights about bulldozer price predictions
- **Page 3 (Project Framework)**: Guide users through the complete data mining process lifecycle for the BulldozerPriceGenius project
- **Page 5 (Documentation**): Provide comprehensive technical documentation for BulldozerPriceGenius project
- **Page 6 (ML Pipeline)**: Detailed explanation of the machine learning pipeline for BulldozerPriceGenius

This structure ensures that users can access information at their preferred technical depth while maintaining the system's overall usability and effectiveness.


## **Page 1: Case Study**
Use Case: Provide comprehensive overview of BulldozerPriceGenius project and its business context

**Key Components:**

- Project Overview
    - Clear value proposition for equipment auction pricing
    - Interactive navigation menu with key sections
- Business Focus
    - AI-powered system for predicting bulldozer auction prices
    - Three core business requirements covering price factors, prediction accuracy, and user accessibility
- Technical Implementation
    - Detailed project terminology and glossary
    - Success metrics including RMSLE and MAE targets
    - Comprehensive dataset overview with training/validation splits

**Action**: Users can quickly understand the project's scope, requirements, and technical framework through an organized, interactive interface

## **Page 2: Hypothesis & Validation**
Use Case: Validate model performance and provide data-driven insights about bulldozer price predictions

**Key Components:**

- Model Validation Results
    - Price accuracy assessment with RMSLE score of 0.27
    - Model prediction vs actual price comparisons
- Feature Analysis
    - Top features influencing prices including year made (19.9%) and product size (15.5%)
    - Comprehensive breakdown of feature importance
- Model Performance Metrics
    - Comparison of different model types
    - Detailed performance metrics including R² values

**Action**: Users can evaluate model reliability, understand key price factors, and verify prediction accuracy through interactive visualizations and detailed performance metrics

## **Page 3: Project Framework**
Use Case: Guide users through the complete data mining process lifecycle for the BulldozerPriceGenius project

**Key Components:**

- Business Understanding
    - Core business requirements and stakeholder impact analysis
    - Detailed breakdown of project objectives with RMSLE target below 1.0
- Data Understanding & Preparation
    - Comprehensive dataset overview with 400,000+ sales records
    - Data cleaning and transformation procedures
    - Feature engineering and quality checks
- Modeling & Evaluation
    - Random Forest model implementation and training
    - Performance metrics with RMSLE score of 0.27
    - Feature importance analysis showing Year Made (19.9%) as top factor
- Deployment
    - Platform implementation on Streamlit Cloud and Heroku
    - Interactive interface for technical and non-technical users

**Action**: Users can navigate through each phase of the data mining process, understand the methodologies used, and access detailed technical documentation with interactive checkboxes for deeper inspection of specific components.

## **Page 4: Interactive Prediction**
Use Case: Interactive Dashboard for Bulldozer Price Analysis

- Data Loading & Memory Optimization
    - Efficient data loading with cached functionality
    - Optimized memory usage through specific data type assignments
- Interactive Filtering Capabilities
    - Price range selection with slider control ($0 - $142,000)
    - State-based filtering with dropdown menu
    - Dynamic data updates based on user selections
- Display Features
    - Clear price range headers showing selected filter values
    - State-specific information when filtered
    - Organized data presentation with SalePrice and state columns prioritized

**Action**: Users can interactively explore bulldozer listings by adjusting price ranges and selecting specific states, with results displayed in an organized table format.

## **Page 5: Documentation**
Use Case: Provide comprehensive technical documentation for BulldozerPriceGenius project

- Technical Documentation Overview
    - Complete API reference for technical users
    - System architecture details
- Key Components
    - Detailed library documentation (pandas, NumPy, matplotlib, scikit-learn)
    - Modular system architecture including data processing, ML core, API layer, and UI components
- System Limitations & Future Development
    - Detailed coverage of technical constraints and performance boundaries
    - Comprehensive development roadmap for future improvements

**Action:** Users can access detailed technical documentation, system architecture details, and understand project limitations and future development plans

## **Page 6: ML Pipeline**
Use Case: Detailed explanation of the machine learning pipeline for BulldozerPriceGenius

- Key Components
    - Problem definition and goals
    - Data collection and preparation steps
    - Exploratory data analysis with visualizations
    - Model training and evaluation process
- Technical Details
    - Overfitting prevention strategies
    - Evaluation metrics and R-squared explanations
    - Model performance metrics and success criteria

**Action**: Users can understand the complete machine learning workflow, from data processing to model deployment, and how the system predicts bulldozer prices


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Tools 🛠️

## Languages

This project requires [`Python 3.12.8`](https://www.python.org/downloads/release/python-3128/) or higher. Python 3.12.8 includes several important features and improvements that are utilized in this project:

- Enhanced error messages and debugging capabilities
- Improved type hinting and annotation features
- Better performance for data processing tasks

To check your Python version, run:

```bash
python --version
```


## Main Data Analysis and Machine Learning Libraries

The project utilizes several key Python libraries for data analysis and machine learning:

-  NumPy (numpy==2.2.2): Foundation for numerical computing in Python
-  Pandas (pandas==2.2.3): Data manipulation and analysis library
-  Matplotlib (matplotlib==3.10.0): Static data visualization library
-  Scikit-learn (scikit-learn==1.6.1): Machine learning algorithms and tools
-  Seaborn (seaborn==0.11.0): Statistical data visualization
-  Streamlit (streamlit==1.10.0): Web app framework for data applications

Example usage:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Reading and processing data
df = pd.read_csv('data.csv')

# Data visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y')
plt.title('Sample Visualization')
```


## Installation of Packages

To install all required packages for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command will automatically install all dependencies listed in the requirements.txt file. Make sure you have Python 3.12.8 installed on your system before running this command.

## Other Technologies
- **Development Tools**
    - **VS Code:** Microsoft's code editor for writing and debugging Python code
    - **Git:** Version control system for tracking code changes and collaboration
    - **GitHub:** Web platform for hosting and managing Git repositories.
    - **Git LFS (Large File Storage):** Extension for Git that manages large files by storing them on a remote server while keeping lightweight references in the repository .
- **Machine Learning Environment**
    - **Google Colab:** Cloud-based notebook with free GPU access for ML development
    - **Jupyter Notebooks:** Interactive computing environment for data analysis
- **Deployment & Documentation**
    - **Heroku:** Cloud platform for deploying web applications and APIs
    - **Streamlit:** Framework for creating data-driven web applications
    - **Notion AI:** AI assistant for documentation improvement
- **Code Quality**
    - **PEP 8 Linter:** Tool ensuring Python code follows style guidelines


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Testing 🧪



## Manual Testing
**User Story Testing**

- The dashboard was tested manually to check if it meets user requirements.
- Since Jupyter notebooks required each function to work in sequence, we skipped manual testing of user stories as it wasn't necessary.

### 1. Case Study
*As a **non-technical user**, I want to access the comprehensive project overview so that I can understand the business context without needing technical expertise.*
| Feature | Action | Expected Result | Actual Result |
|---------|---------|----------------|---------------|
|Case study page|Navigate to the case study page using the left sidebar dropdown menu|Page is displayed, can move between  pages|Functions as expected|
| Case study page | Viewing case study page | Page is displayed, can move between sections on page | Functions as expected |
| Content links | Click to navigate to the section | Displays selected content | Functions as expected |
| Checkbox show glossary | Click the checkbox | When clicked, displays the expected content | Functions as expected |
| External Link to Data Dictionary File | Click the external link | When clicked, opens in a new browser tab | Functions as expected |
| External Link to Blue Book for Bulldozers | Click the external link | When clicked, opens in a new browser tab | Functions as expected |
| External Link to Project README file | Click the external link | When clicked, opens in a new browser tab | Functions as expected |

 ### 2. Hypothesis & Validation
 *As a **technical user** I want to validate the model's performance and accuracy
so that I can verify the model's reliability and understand the key factors driving bulldozer price predictions through detailed metrics and visualizations.*

*ACCEPTANCE CRITERIA:*

- *Must be able to review model validation results showing an RMSLE score of `0.27`
- *Must be able to analyze feature importance, particularly focusing on key factors like year made (`19.9%`) and product size (`15.5%`)*
- *Must be able to compare different model types and examine performance metrics including R² values*
- *Must be able to evaluate model predictions against actual price comparisons*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
|Hypothesis and validation page|Navigate to the hypothesis and validation page using the left sidebar dropdown menu|Page is displayed, can move between  pages|Functions as expected|
| Hypothesis and validation page | Viewing hypothesis and validation page | Page is displayed, can move between sections on page | Functions as expected |
| Content links | Viewing case study page | Displays selected content | Functions as expected |
| Display Image: Actual vs. Predicted Sale Price | No action needed | Display image correctly and can be enlarged | Functions as expected |
| Display Image: Top 20 Feature Importance Values | No action needed | Display image correctly and can be enlarged | Functions as expected |
| Display Image: Validation RMSLE | No action needed | Display image correctly and can be enlarged | Functions as expected |




 ### 3. Project Framework
 *As a **technical user** I want to understand and validate the CRISP-DM workflow implementation so that I can verify the complete data mining lifecycle is properly implemented for the BulldozerPriceGenius project*

*ACCEPTANCE CRITERIA:*

- *Must be able to review core business requirements and project objectives with RMSLE target below `1.0`*
- *Must be able to verify data understanding and preparation steps including:*
    - *Dataset overview with a sample of 500 from 400,000+ records*
    - *Data cleaning procedures*
    - *Feature engineering processes*
- *Must be able to validate modeling and evaluation results:*
    - *Random Forest implementation*
    - *RMSLE score of `0.27`*
    - *Feature importance analysis*
- *Must be able to confirm deployment configuration on Streamlit Cloud and Heroku with appropriate technical and non-technical user interfaces*


| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
|Project framework page|Navigate to the project framework page using the left sidebar dropdown menu|Page is displayed, can move between  pages|Functions as expected|
| Display Image: BPG Project Overview Framework | No action needed | Display image correctly and can be enlarged | Functions as expected |
| Project framework page | Viewing project framework page | Page is displayed, can move between sections on page | Functions as expected |
| Content links | Viewing case study page | Displays selected content | Functions as expected |
| Checkbox show business requirements | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| External Link to Kaggle | Click the external link | Opens in a new browser tab and displays the website | Functions as expected |
| Checkbox DataFrame Inspection: Missing Values | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox DataFrame Inspection: Data Mixed Types | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Main Types of Information | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox DataFrame Inspection: Identify columns with missing data | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Quality Checks: Inspection of Random Sample Rows | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Quality Checks: Total Number of Missing Values | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Feature Importance | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Top 5 Feature Importance Pie Chart | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Prediction vs Reality Analysis | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Interactive Dashboard Image | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Kaggle Dashboard | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |


 ### 4. Interactive Prediction
*As a **non-technical** user I want to explore and filter bulldozer listings interactively
so that I can easily analyze bulldozer prices based on different criteria*

*ACCEPTANCE CRITERIA:*

- *Must be able to adjust price ranges using a slider control between $0 - $142,000*
- *Must be able to select specific states using a dropdown menu*
- *Must be able to see:*
    - *Clear price range headers with selected filter values*
    - *State-specific information when a state is selected*
    - *An organized table showing SalePrice and state information*
- *Must see data updates dynamically based on selected filters*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| Interactive prediction page | Navigate to the Interactive Prediction page using the left sidebar dropdown menu | Page is displayed, can move between pages | Functions as expected |
| Price Range Slider ($) | Adjust the price range slider between $0 and $142,000 | Displays filtered results with clear price range headers showing the selected filter values and a corresponding results table | Functions as expected |
| Select state dropdown input | Select a U.S. state from the dropdown menu, or choose "All States" or "Unspecified" | Display filtered results with state-specific information prominently shown at the top of the results table when a state is selected | Functions as expected |
| Search using all two filters | Adjust the price range slider and select a state from the dropdown menu | Clear headers showing the selected price range filters, state-specific details for the chosen state, and an organized table displaying SalePrice and state information | Functions as expected |

 ### 5. Documentation
 *As a **technical user** I want to thoroughly review the technical documentation so that I can understand the system architecture, implementation details, and future development plans*

*ACCEPTANCE CRITERIA:*

- *Must be able to access and verify complete API reference documentation*
- *Must be able to review system architecture details including:*
    - *Data processing components*
    - *ML core implementation*
    - *API layer structure*
    - *UI components*
- *Must be able to examine detailed library documentation for key technologies (pandas, NumPy, matplotlib, scikit-learn)*
- *Must be able to review:*
    - *Technical constraints and performance boundaries*
    - *Development roadmap for future improvements*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| Documentation page | Navigate to the documentation page | Page is displayed, can move between pages | Functions as expected |
| Documentation page | Viewing documentation page | Page is displayed, can move between sections on page | Functions as expected |
| Content links | Viewing case study page | Displays selected content | Functions as expected |

 ### 6. ML Pipeline
 *As a **technical user** I want to understand and validate the machine learning pipeline implementation so tdhat I can verify the complete workflow from data processing to model deployment is properly implemented*

*ACCEPTANCE CRITERIA:*

- *Must be able to review and validate:*
    - *Problem definition documentation and project goals*
    - *Data collection methodology and preparation procedures*
    - *Exploratory data analysis processes and visualization outputs*
    - *Model training procedures and evaluation methodology*
- *Must be able to verify technical implementation of:*
    - *Overfitting prevention mechanisms*
    - *Evaluation metrics including R-squared calculations*
    - *Model performance metrics against defined success criteria*
- *Must be able to trace the complete workflow from initial data processing through to final model deployment*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| ML Pipeline page | Navigate to the ML Pipeline page | Page is displayed, can move between pages | Functions as expected |
| ML Pipeline page | Viewing ML pipeline page | Page is displayed, can move between sections on page | Functions as expected |
| Content links | Viewing case study page | Displays selected content | Functions as expected |
| Checkbox Inspection: Sale Price Distribution | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |
| Checkbox Inspection: Median Sale Price Monthly | Click the checkbox | Upon clicking, the expected content appears | Functions as expected |


## Validation
We checked the code quality using [CodeInstitute's PEP8 Linter tool](https://pep8ci.herokuapp.com/). This tool looked at all the files in both the app_pages, src folders, and root directory to make sure they follow good coding standards.

- Some long text lines in the dashboard code were flagged as too long by the tool, but we decided this was okay.
- We kept these longer lines because they didn't make the code harder to read or affect how well it works.



## Automated Unit Tests
No automated unit tests have been carried out at this time.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Bug Reports 🐞

I've added links to the bug reports from my GitHub Project in my README.md table below.

## Known bugs ❌

**Known bugs** are issues in the code that still need to be fixed. These include problems that have been identified but require further investigation, resources, or future updates to resolve.

| Bug Description | Bug Report Link | Bug Type |
| --------------- | --------------- | -------- | --- |
|                 |                 |          |     |

## Fixed bugs ✅

**Fixed bugs** are issues that have been successfully resolved. Documenting fixed bugs helps track progress and provides solutions for similar issues that may arise in the future.

| Bug Description | Bug Report Link                                                                                                               | Bug Type                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 🐞 Bug Report:  | Subject: Kaggle Dataset Download 403 Forbidden Error [#12](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2/issues/2) | 🐞Bug: Authentication Error 🔒 |
| 🐞 Bug Report:  | Subject: Bug with GitHub file size limits when pushing large CSV files [#13](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2/issues/1)  | 🐞Bug: File Size Limit Error 💾

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


# Setup & Deployment 🚢

## Git LFS Setup Guide
[**Git LFS (Large File Storage)**](https://git-lfs.com/)  is a Git extension that helps manage large files in your Git repositories. Think of it as a specialized tool that handles files that are too big for regular Git to manage efficiently.

Why do you need it? GitHub has a 100MB file size limit for regular files. Git LFS solves this problem by providing a way to version large files.

Instead of storing these large files directly in your Git repository, Git LFS stores lightweight references and keeps the actual files on a separate server. This makes your repository more manageable and ensures smooth collaboration when working with large files.

> [!NOTE]
> ### Git LFS Storage Management
> During the project development, I encountered storage limitations with Git LFS's 1GB free tier. While there were alternatives available to reduce file sizes, such as removing unnecessary large files or using external storage, time constraints led me to purchase additional data packs. This ensured uninterrupted project progress and maintained the integrity of our version control system.
>
> For those interested in upgrading Git LFS storage, detailed instructions can be found in the [GitHub Documentation](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/upgrading-git-large-file-storage).
>
> Alternative storage management strategies include:
> - Remove unnecessary large files from Git history.
> - Store large files elsewhere (like cloud storage) and add them to `.gitignore`.
> - Clean up old LFS objects you no longer need.

### Prerequisites

- Git Bash
- Git LFS

### Installation

1. Initialize Git LFS in your repository:

```bash
git lfs install
```

1. Configure files to track (examples):

```bash
git lfs track "*.csv"     # Track CSV files
git lfs track "*.xlsx"    # Track Excel files
git lfs track "*.pkl"     # Track Pickle files
```

1. Save the configuration:

```bash
git add .gitattributes
git commit -m "Configure Git LFS"
```

### For Existing Projects

To migrate existing files to LFS:

```bash
git lfs migrate import --include="*.csv,*.xlsx,*.pkl" --everything
git push origin main --force
```

### Important Notes

- All team members must have Git LFS installed
- Files larger than 100MB require Git LFS
- Force push is required after migration

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## **Setting Up Streamlit**

This guide will help you set up Streamlit for your project. We'll walk through the essential steps using virtual environments and pip based on Streamlit [**documentation**](https://docs.streamlit.io/develop/concepts/multipage-apps/overview).

#### **Prerequisites Checklist**

- ✅ Python (version 3.9-3.13)
- ✅ Python environment manager (venv)
- ✅ Package manager (pip)
- ✅ Code editor (VS Code recommended)
- ✅ For Mac users only: Xcode command line tools

### **Quick Setup Guide**

##### **1. Create Virtual Environment**

Navigate to your project folder and run:

```bash
cd myproject
python -m venv .venv

```

#### **2. Activate Environment**

Use the appropriate command for your system:

```bash
# Windows Command Prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

```

#### **3. Install Streamlit**

```bash
pip install streamlit

```

#### **4. Test Installation**

```bash
streamlit hello

```

### **Creating Your First App**

1. Create a file named `app.py`
2. Add this simple code:

```python
import streamlit as st

st.write("Hello world")

```

1. Run your app:

```bash
streamlit run app.py

```

### **Best Practices**

- Always use a virtual environment for each project.
- Keep requirements.txt updated with `pip freeze > requirements.txt`.
- Use `deactivate` when finished working.
- Add `.venv` to your `.gitignore` file.

### **Troubleshooting Tips**

- If standard commands fail, try using `python -m streamlit run app.py`.
- Check that your virtual environment is activated (look for (.venv) in terminal).
- Ensure you're using a supported Python version.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Forking and Cloning
### **What is Forking and Cloning?**

Forking creates your own copy of [**BulldozerPriceGenius**]( https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2.git) on GitHub, while cloning downloads that copy to your local computer.

### **How to Fork a Project**

1. Go to the GitHub project page you want to copy
2. Look for the "Fork" button in the top-right corner
3. Click it! GitHub will create your copy of the project
4. Wait a few seconds while GitHub does its magic

### **How to Clone Your Fork**

1. On your forked project page, find the green "Code" button
2. Click it and copy the HTTPS link (it should end with .git)
3. Open Git Bash on your computer (or Terminal if you're using Mac)
4. Type: `git clone` followed by the link you copied
5. Press Enter and watch the files download to your computer!

### **Important Tips**

- Make sure you're logged into GitHub before forking
- Choose a good spot on your computer to clone the project

### **Common Problems and Solutions**

- **Problem:** "Permission denied" messageSolution: Make sure you're logged into GitHub
- **Problem:** Can't find the fork buttonSolution: Scroll to the top of the page - it's always in the top-right
- **Problem:** Clone isn't workingSolution: Double-check that you copied the full link correctly

Remember: After cloning, you'll have your very own copy of the project to work on!

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Credits ⭐

## Content
- [**Dataset Source**](https://www.kaggle.com/c/bluebook-for-bulldozers/overview) : The dataset used in this project is sourced from the  [*Kaggle Bluebook for Bulldozers Competition*](https://www.kaggle.com/c/bluebook-for-bulldozers/overview). The competition was sponsored by Fast Iron, a leading construction technology solutions provider


## Tutorials
- [**Blog**](https://www.mrdbourke.com/a-6-step-field-guide-for-building-machine-learning-projects/): The project structure inspired by *Daniel Bourke's A 6-step field guide for building machine learning projects*.
- [**Code Institute's Data Analytics Course**](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/): Provides tutorial lessons for basic project setup.

- [**RMSLE metric**](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle): Explanation based on Carlo Lepelaars' Kaggle kernel on "Understanding Root Mean Squared Logarithmic Error (RMSLE)".
- [**YouTube**](https://www.youtube.com/watch?v=4Ln6iRh_LTo): [*How to Setup Git LFS for New and Existing Projects (Works With Unity)*](https://www.youtube.com/watch?v=4Ln6iRh_LTo): This project uses Git LFS (Large File Storage) for handling large files. The Git LFS setup and implementation was guided by Max O'Didily's comprehensive tutorial. For detailed setup instructions and best practices, please refer to the Git LFS documentation and resources in the video.
<br>**Requirements**
  - Git Bash
  - Git LFS<a href="7"/><a href="8"/>
<br>

- [**Random Forest Regressor**](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html): The implementation of the Random Forest model was based on the documentation from Scikit-learn's Random Forest Regressor
- [**Model Driven Data Exploration (EDA)**](https://www.ibm.com/think/topics/exploratory-data-analysis): The methodology for exploratory data analysis was inspired by IBM's article on Model Driven Data Exploration
- [**Recursive Feature Elimination (RFE)**](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html): The implementation of RFE was based on the documentation from Scikit-learn's feature selection module.
- [**The Principal Component Analysis (PCA)**](https://www.kaggle.com/code/ryanholbrook/principal-component-analysis) implementation and methodology was adapted from Ryan Holbrook's Kaggle tutorial on dimensionality reduction techniques.
- [**Correlation Analysis**](https://www.geeksforgeeks.org/what-is-correlation-analysis/): The correlation analysis section was adapted from GeeksforGeeks article on correlation analysis.
- [**Feature Selection**](https://www.kaggle.com/code/prashant111/comprehensive-guide-on-feature-selection): The comprehensive guide on feature selection by Prashant Banerjee.
- [**Hyperparameter Tuning**](https://www.kaggle.com/code/shreayan98c/hyperparameter-tuning-tutorial): The hyperparameter tuning tutorial by Shreayan Chaudhary.
- [**Feature Engineering**](https://www.kaggle.com/learn/feature-engineering):   The feature engineering tutorial is adapted from a Kaggle tutorial that provides comprehensive guidance on creating and selecting meaningful features for machine learning models.
- [**Linear Regression**](https://www.kaggle.com/code/sudhirnl7/linear-regression-tutorial): The linear regression tutorial by Sudhir Kumar.
- [**Decision Trees**](https://www.kaggle.com/code/satishgunjal/tutorial-decision-tree): The decision trees tutorial by Satish Gunjal.
- [**Git LFS Storage**](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/upgrading-git-large-file-storage): The implementation and management of Git Large File Storage was guided by [GitHub's comprehensive documentation](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/upgrading-git-large-file-storage).
- [**Feature Importance Analysis**](https://www.kaggle.com/code/raskoshik/feature-importance-how-not-fool-yourself): The methodology for analyzing feature importance was informed by this [comprehensive Kaggle guide](https://www.kaggle.com/code/raskoshik/feature-importance-how-not-fool-yourself).
- **[Streamlit](https://docs.streamlit.io/)**: The Streamlit [documentation](https://docs.streamlit.io/) served as the foundation for building our interactive web application interface.
- [**Streamlit Installation and Setup**](https://docs.streamlit.io/get-started/installation/command-line): The Streamlit installation and setup instructions were adapted from the official [Streamlit documentation and command-line guide](https://docs.streamlit.io/get-started/installation/command-line), which provides comprehensive guidance for getting started with Streamlit applications.
- [**Streamlit (Create an App)**](https://docs.streamlit.io/get-started/tutorials/create-an-app) : The structure of this project's Streamlit application draws from the official [**"Create an App" tutorial**](https://docs.streamlit.io/get-started/tutorials/create-an-app)— a detailed guide for developing multi-page data applications.
- [**Mean Absolute Error (MAE)**](https://www.kaggle.com/discussions/general/413103): The implementation of the Mean Absolute Error metric was based on the documentation from Scikit-learn's metrics module and Kaggle discussions about error metrics in regression problems.
- [**R² Score (Coefficient of Determination)**](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html): The implementation of the R² Score metric was based on the documentation from Scikit-learn's metrics module for evaluating regression model performance.
  


## Media

- [**Bulldozer image**](http://Freepik.com): Sourced from Freepik.com with a free licence. 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Acknowledgements 📢

- Thanks to my mentor Mo Shami, for his support and guidance on the execution of the project.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

