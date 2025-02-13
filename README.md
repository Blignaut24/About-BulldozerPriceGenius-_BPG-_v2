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
- [Dataset Content](#dataset-content)
- [Project Terms \& Jargon](#project-terms--jargon)
  - [Prediction-Related Terms](#prediction-related-terms)
  - [Data Organization](#data-organization)
  - [Technical Tools](#technical-tools)
  - [File Types](#file-types)
- [Business Requirements](#business-requirements)
- [ML Business Case (10 Key Components)](#ml-business-case-10-key-components)
- [Project Hypothesis and Validation](#project-hypothesis-and-validation)
    - [Hypothesis](#hypothesis)
  - [Validation Approach](#validation-approach)
    - [Data Splitting Strategy](#data-splitting-strategy)
    - [Performance Measurement](#performance-measurement)
    - [Model Evaluation Process](#model-evaluation-process)
- [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
    - [Price Prediction](#price-prediction)
    - [Market Trends](#market-trends)
    - [Smart Pricing](#smart-pricing)
  - [How Our Tools Help Us](#how-our-tools-help-us)
- [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
- [Bug Reports 🐞](#bug-reports-)
  - [Known bugs ❌](#known-bugs-)
  - [Fixed bugs ✅](#fixed-bugs-)
- [Deployment](#deployment)
  - [Git LFS Setup Guide](#git-lfs-setup-guide)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [For Existing Projects](#for-existing-projects)
    - [Important Notes](#important-notes)
  - [Heroku](#heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Tools](#tools)
- [Credits](#credits)
  - [Content](#content)
  - [Tutorials](#tutorials)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)

# Introduction

# Dataset Content

- The project leverages an extensive dataset of historical bulldozer sales information, carefully sourced from [Kaggle's prestigious Bluebook for Bulldozers competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview).
- This comprehensive dataset encompasses a wide range of crucial attributes, including detailed model specifications, precise size measurements, accurate sale dates, specific location data, and numerous other relevant parameters.
- For an exhaustive understanding of the data structure, please consult the comprehensive [data dictionary](https://www.kaggle.com/c/bluebook-for-bulldozers/data?select=Data+Dictionary.xlsx) available on the Kaggle competition page.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Project Terms & Jargon

Here are the main terms you'll encounter in this project:

## Prediction-Related Terms

- **Regression**: Making predictions about numbers (like guessing house prices)
- **Time Series**: Using past information to predict future events (like weather forecasting)
- **RMSLE**: A way to measure how accurate our predictions are

## Data Organization

- **Data Dictionary**: A guide that explains what each piece of information means
- **Target Variable**: What we're trying to predict (in this case, bulldozer prices)
- **Independent Variables**: The information we use to make predictions (like age or model of bulldozer)
- **Feature Engineering**: Creating new useful information from existing data

## Technical Tools

- **Datetime**: A way to work with dates and times in Python
- **EDA**: Looking at data to understand patterns (like making charts and graphs)
- **Random Forest**: A powerful prediction tool that combines multiple simpler predictions
- **NaN**: Stands for "Not a Number" - used when data is missing

## File Types

- **CSV**: A simple file type that stores data in a table format
- **Parquet**: A more advanced file type that saves space and works quickly
- **Feather**: Another fast file type for storing data

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Business Requirements

- The system needs to make accurate price predictions for bulldozers at auctions, no matter what the market looks like.
- As more data comes in, the system should handle it smoothly and be ready to grow bigger in the future.
- The system should be easy to use for everyone, whether they're tech-savvy or not.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# ML Business Case (10 Key Components)

1. **Business Problem:** The current bulldozer auction market suffers from a significant lack of reliable pricing guidance mechanisms, resulting in substantial financial risks for both buyers and sellers.
2. **Proposed Solution:** BPG implements sophisticated AI algorithms to generate accurate price predictions, enabling more informed and confident decision-making processes.
3. **Data Sources:** Comprehensive historical sales data obtained from the highly regarded Kaggle's Bluebook for Bulldozers competition.
4. **ML Model:** Advanced Random Forest Regression model specifically optimized for robust and reliable predictions.
5. **Evaluation Metric:** Utilizes Root Mean Squared Log Error (RMSLE) for precise measurement of prediction accuracy.
6. **Success Metrics:** Demonstrable reduction in auction risks, enhanced bidding strategy effectiveness, and maximized financial returns.
7. **Deployment:** Implemented on Heroku's scalable platform to ensure optimal accessibility and performance.
8. **Stakeholders:** Encompasses construction companies, equipment dealers, auctioneers, and data scientists.
9. **Risks:** Careful consideration of data quality assurance, model interpretability challenges, and market fluctuation impacts.
10. **Cost-Benefit Analysis:** Substantial reduction in financial risks combined with increased profit potential provides clear justification for investment.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Project Hypothesis and Validation

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

# The rationale to map the business requirements to the Data Visualizations and ML tasks


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


# Dashboard Design (Streamlit App User Interface)
Dashboard Component Examples:

**Basic Things to Enter:**
- What year the sale happened (pick from a list)
- Which month it was (pick from a list) 
- Which state it's in (pick from a list)
- The machine's ID number (type it in)
- The model's ID number (type it in)

**More Detailed Things:**
- How many hours the machine has been used (type in a number)
- How much it's been used (pick Low, Medium or High)
- What kind of machine it is (pick from a list)
- Where we got the data from (pick from a list)
- Who's selling it (type in a number)
- When it was made (pick from a list)

**Extra Things You Can Choose:**
- Pick dates for when it was sold
- What type of machine it is
- What kind of wheels it has (2-wheel, 4-wheel, etc.)
- What kind of cab it has (closed or open)

**How We'll Build It:**
We'll use simple buttons, drop-down lists, and places to type in numbers. Everything will be neat and easy to find on the screen.

Remember: We want to make it super easy for people to use!

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


# Deployment

## Git LFS Setup Guide
[**Git LFS (Large File Storage)**](https://git-lfs.com/)  is a Git extension that helps manage large files in your Git repositories. Think of it as a specialized tool that handles files that are too big for regular Git to manage efficiently.

Why do you need it? GitHub has a 100MB file size limit for regular files. Git LFS solves this problem by providing a way to version large files.

Instead of storing these large files directly in your Git repository, Git LFS stores lightweight references and keeps the actual files on a separate server. This makes your repository more manageable and ensures smooth collaboration when working with large files.

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
git lfs track "*.csv"    # Track CSV files
git lfs track "*.xlsx"   # Track Excel files 
```

1. Save the configuration:

```bash
git add .gitattributes
git commit -m "Configure Git LFS"
```

### For Existing Projects

To migrate existing files to LFS:

```bash
git lfs migrate import --include="*.*csv*,*.xlsx" --everything
git push origin main --force
```

### Important Notes

- All team members must have Git LFS installed
- Files larger than 100MB require Git LFS
- Force push is required after migration

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


# Main Data Analysis and Machine Learning Libraries

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


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Tools

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Credits

## Content
- **Dataset Source** : The dataset used in this project is sourced from the  [Kaggle Bluebook for Bulldozers Competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview). The competition was sponsored by Fast Iron, a leading construction technology solutions provider


## Tutorials
- **Blog**: The project structure inspired by Daniel Bourke's [A 6-step field guide for building machine learning projects](https://www.mrdbourke.com/a-6-step-field-guide-for-building-machine-learning-projects/)
- [**Code Institute's Data Analytics Course**](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/): Provides tutorial lessons for basic project setup - [**Link**](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/)

- [**RMSLE metric**](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle): Explanation based on Carlo Lepelaars' Kaggle kernel on "Understanding Root Mean Squared Logarithmic Error (RMSLE)". - [**Link**](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle)
- **YouTube** [*How to Setup Git LFS for New and Existing Projects (Works With Unity)*](https://www.youtube.com/watch?v=4Ln6iRh_LTo): This project uses Git LFS (Large File Storage) for handling large files. The Git LFS setup and implementation was guided by Max O'Didily's comprehensive tutorial. For detailed setup instructions and best practices, please refer to the Git LFS documentation and resources - [**Link**](https://www.youtube.com/watch?v=4Ln6iRh_LTo)
<br>**Requirements**
  - Git Bash
  - Git LFS<a href="7"/><a href="8"/>
<br>
- [**Random Forest**](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) : A method that combines many simple prediction models to make better, more accurate predictions -[**Link**](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
  


## Media

- **Bulldozer image**: Sourced from [Freepik.com](http://Freepik.com) with a free licence.  [Link](http://Freepik.com)

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

# Acknowledgements 

- Thank the people who provided support through this project.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

