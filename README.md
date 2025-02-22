# BulldozerPriceGenuis (BPG)

#### "**BulldozerPriceGenuis (BPG)**: _Know Your Equipment's Worth, Make Smarter Auction Decisions_

<img src="static/images/bulldozer_ai-min.webp" width="40%" style="display: block; margin: 0 auto;">

In the complex world of heavy equipment auctions, construction companies and dealers face a persistent challenge: accurately determining the value of their bulldozers. The uncertainty can lead to missed opportunities and financial losses.

Enter BulldozerPriceGenius (BPG), your trusted partner in bulldozer valuation. We've developed an advanced AI-powered system that leverages data analysis to predict auction prices with precision. By analyzing comprehensive datasets from real auctions and considering crucial factors like equipment usage, features, and market conditions, we eliminate the guesswork from pricing.

In collaboration with Fast Iron, we're revolutionizing the industry by creating the equivalent of a Kelly Blue Book for bulldozers. This means you can now:

- Make confident pricing decisions backed by data
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

- **Regression**: Making predictions about numbers (like guessing house prices)
- **Time Series**: Using past information to predict future events (like weather forecasting)
- [**RMSLE**](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle): A way to measure how accurate our predictions are

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
• [**Business Requirement 1**](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2/issues/10) - The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.

• [**Business Requirement 2**](https://github.com/users/Blignaut24/projects/23/views/2?pane=issue&itemId=97854211&issue=Blignaut24%7CAbout-BulldozerPriceGenius-_BPG-_v2%7C11) - The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.

• [**Business Requirement 3**](https://github.com/users/Blignaut24/projects/23/views/2?pane=issue&itemId=97854762&issue=Blignaut24%7CAbout-BulldozerPriceGenius-_BPG-_v2%7C13) - The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.

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
    
  - **Interactive Visualization:** A user-friendly interface displaying real-time price predictions, market analytics, and trend analysis
  - **Data-Driven Insights:** Clear presentation of key pricing factors and market indicators to support strategic decision-making
  - **Seamless Integration:** Real-time updates of predictions and market data, ensuring users always have access to current information
  - **Cross-Team Accessibility:** An intuitive interface suitable for both technical and business users, supporting collaborative decision-making
  - **Automated Reporting:** Streamlined generation and distribution of insights, reducing manual effort and improving operational efficiency

## 4. What does success look like?
Project success will be evaluated through three critical metrics:
    
  ### 1. Model Accuracy
  - Root Mean Squared Log Error (RMSLE)
  - Quantifies prediction accuracy against actual sale prices
  - Success target: RMSLE below 0.25
    
  ### 2. Market Performance  
  - Kaggle Competition Ranking
  - Top 10% placement on leaderboard
  - Consistent performance across different market conditions
    
  ### 3. Business Impact  
  - Measurable Value Creation
  - At least 15% improvement in price prediction accuracy
  - Demonstrated ROI through reduced pricing discrepancies
  - Increased user confidence in pricing decisions
    
    Success is achieved when our model delivers consistently accurate predictions (verified by RMSLE), maintains competitive performance, and provides clear, actionable insights that enhance business outcomes.
    
## 5. Can you break down the project into Epics and User Stories?
  
  Yes, the project can be broken down into [Epics and User Stories](https://github.com/users/Blignaut24/projects/23/views/2).
    
## 6. Ethical or Privacy concerns?
    
  No, there are no ethical or privacy concerns about this data as it is fictitious data from a [Kaggle competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview). 
    
## 7. What level of prediction performance is needed?
    
  For this project, we use Root Mean Squared Log Error (RMSLE) as our key performance metric. Our target is to achieve an RMSLE below 0.25, which would indicate highly accurate price predictions.
    
  **Why RMSLE?**
    
  We chose RMSLE because it works well with our wide range of bulldozer prices and puts more emphasis on avoiding price underestimation, which is crucial for our business case.
    
  **Performance Benchmarks:**
    
  - Top 10% of Kaggle competition scores
  - Consistent accuracy across different price ranges
  - Minimum 15% improvement over current pricing methods
    
  These targets will ensure our model delivers reliable and competitive results while meeting business requirements.
    
## 8. What are the project inputs and intended outputs?
  - **Input Features:**
    - Equipment specifications (year, model, series)
    - Sale conditions and location
    - Technical specifications (engine, hours, condition)
  - **Model Output:**
      - Predicted auction price in USD
      - Confidence intervals for predictions
    - **Workflow:**
      - System processes equipment details
      - Advanced ML algorithm generates price estimate
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

## Hypothesis
I hypothesize that machine learning models can accurately predict bulldozer auction prices using historical sales data. The prediction model will analyze key features including:
- Model specifications
- Manufacturing year
- Usage metrics
- Sale location and timing

## Validation Approach

### Data Splitting Strategy
- `Training set`: Model learning
- `Validation set`: Parameter tuning and performance assessment
- `Test set`: Final evaluation of real-world prediction capability

### Performance Measurement: How We Measure Success?
- We use a measurement called **RMSLE** to check how accurate our predictions are
- A lower **RMSLE** number means our predictions are better
- We'll test our system on different types of bulldozers to make sure it works well in all cases

### Model Evaluation Process
1. Train multiple ML models
2. Compare RMSLE scores
3. Select best performing model based on validation results
4. Analyze feature importance for key price drivers
5. Conduct error analysis to identify improvement areas

Success will be determined by achieving consistent price predictions within acceptable error margins across diverse bulldozer types and market conditions.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# The rationale to map the business requirements to the Data Visualizations and ML tasks 🗺️


### Price Prediction

- **What We Need**: To accurately tell how much a bulldozer will sell for
- **How We Do It**: Using a computer program called Random Forest that learns from past sales
- **Why It Works**: The program looks at lots of old sales data to understand what makes prices go up or down

### Market Trends

- **What We Need**: To understand how bulldozer prices change over time
- **How We Do It**:
    - Making charts that show prices over time
    - Looking at monthly price changes
    - Using special tools to spot patterns
- **Why It Works**: This helps us see when prices typically rise and fall during the year

### Smart Pricing

- **What We Need**: To set the best possible prices
- **How We Do It**:
    - Making maps to show prices in different areas
    - Finding out what features affect price the most
    - Creating charts to show price ranges
- **Why It Works**: This helps us understand what makes prices different in various places

## How Our Tools Help Us

We use computer programs and charts together to help us understand bulldozer prices better. Here's what they do:

- They predict prices: Our computer program looks at things like a bulldozer's age, size, and condition to guess how much it might sell for. This helps people make better choices when buying or selling.
- They show us patterns: Our charts help us see when bulldozer prices go up and down. For instance, we've found that prices are usually higher in January and February.
- They help with pricing: By knowing what makes bulldozer prices go up or down, we can figure out fair prices. This helps everyone get good deals when buying or selling.
- They explain the market: We can see which states sell the most bulldozers and what matters most when setting prices. This information helps anyone who works with bulldozers.

When we use all these tools together, we can make smarter decisions about buying and selling bulldozers.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

#  Epics and User Stories 📜
The project was divided into 5 Epics covering Data Analysis and Machine Learning tasks. User stories were created within each Epic to implement an agile methodology in the [Git project](https://github.com/users/Blignaut24/projects/23/views/1).

## **Epic 1 - Data Ingestion and Preprocessing**

• **User Story** - As a data scientist, I can ingest the bulldozer sales data from a CSV file so that it's available for analysis and modeling. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can create new features from the 'saledate' column to enhance model training capabilities. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can handle missing values in the dataset to ensure data quality for modeling. (**Business Requirement 2**)

• **User Story** - As a data scientist, I can convert categorical string columns to numerical representations for machine learning compatibility. (**Business Requirement 2**)

## **Epic 2 - Exploratory Data Analysis (EDA)**

• **User Story** - As a data scientist, I can visualize the distribution of the SalePrice column to understand the target variable characteristics (**Business Requirement 1**).

• **User Story** - As a data scientist, I can explore sales trends over time to identify patterns and seasonality in the data (**Business Requirement 1**).

## **Epic 3 - Machine Learning Modeling**

• **User Story** - As a data scientist, I can train a Random Forest Regression model to predict bulldozer sale prices (**Business Requirement 2**).

• **User Story** - As a data scientist, I can evaluate model performance to ensure accurate price predictions (**Business Requirement 2**).

• **User Story** - As a data scientist, I can save the trained model for future use and deployment. (**Business Requirement 2**)

## **Epic 4 - Dashboard Planning, Designing, and Development**
• **User Story** - As a data analyst, I can access an interactive prediction page to make real-time price predictions for bulldozers (**Business Requirement 3**).

• **User Story** - As a data analyst, I can input bulldozer specifications through a user-friendly interface to get accurate price estimates (**Business Requirement 3**).

• **User Story** - As a data analyst, I can view confidence metrics for predictions to assess the reliability of the results (**Business Requirement 3**).

## **Epic 5 - Dashboard Deployment and Release**

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


#  Dashboard Design (Streamlit App User Interface) 🎨
The BulldozerPriceGenius dashboard is structured to serve both technical and non-technical users effectively:

**For Non-Technical Users:**

- Page 1 (Project Overview): Provides a clear, high-level understanding of the project's purpose and benefits
- Page 2 (Data Analysis): Offers intuitive visualizations and insights about price influencing factors
- Page 4 (Interactive Prediction): Features a user-friendly interface for obtaining bulldozer price estimates

**For Technical Users:**

- Page 3 (Model Performance): Details model accuracy metrics, validation results, and performance analysis
- Page 5 (Documentation): Contains comprehensive technical documentation, including API details, system limitations, and development roadmap

This structure ensures that users can access information at their preferred technical depth while maintaining the system's overall usability and effectiveness.


## **Page 1: Project Overview**
Use Case: Provide quick orientation and project context
- Project summary and objectives
- Key business requirements
- Dataset overview
- Technical prerequisites
  
Action: Help users easily see what the project does and what it needs

## **Page 2: Data Analysis**
Use Case: Enable data-driven insights
- Interactive data exploration tools
- Feature importance visualization
- Price trend analysis
- Geographic insights

Action: Users can find out what makes bulldozer prices go up or down

## **Page 3: Model Performance**
Use Case: Validate model reliability
- Performance metrics dashboard
- Accuracy visualization
- Error distribution analysis
- Model comparison interface

Action: Users can easily check how well the system is working and how accurate its predictions are

## **Page 4: Interactive Prediction**
Use Case: Generate real-time predictions
- User-friendly input form
- Real-time price predictions
- Confidence metrics display
- Results interpretation guide
  
Action: Users can quickly find out what their bulldozer is worth

## **Page 5:Documentation**
Use Case: Provide technical reference
- API documentation
- User guide
- Known limitations
- Future roadmap
  
Action: Users can easily check a bulldozer's price


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



## Validation



## Automated Unit Tests

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
  


## Media

- [**Bulldozer image**](http://Freepik.com): Sourced from Freepik.com with a free licence. 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Acknowledgements 📢

- Thanks to my mentor Mo Shami, for his support and guidance on the execution of the project.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

