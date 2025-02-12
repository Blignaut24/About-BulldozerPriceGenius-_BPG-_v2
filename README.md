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

## Table of Content

- [BulldozerPriceGenuis (BPG)](#bulldozerpricegenuis-bpg) - ["**BulldozerPriceGenuis (BPG)**: _Know Your Equipment's Worth, Make Smarter Auction Decisions_ |](#bulldozerpricegenuis-bpg-know-your-equipments-worth-make-smarter-auction-decisions-) - [_"Stop leaving money on the table. Let BulldozerPriceGenius transform your uncertain pricing decisions into data-driven success stories."_](#stop-leaving-money-on-the-table-let-bulldozerpricegenius-transform-your-uncertain-pricing-decisions-into-data-driven-success-stories)
  - [Table of Content](#table-of-content)
  - [Dataset Content](#dataset-content)
  - [Project Terms \& Jargon](#project-terms--jargon)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
      - [Bulldozer image](#bulldozer-image)
  - [Acknowledgements (optional)](#acknowledgements-optional)
  - [Cloud IDE Reminders](#cloud-ide-reminders)

## Dataset Content

- Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Project Terms & Jargon

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Business Requirements

- Describe your business requirements

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them)

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualizations and ML tasks

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## ML Business Case

- In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Dashboard Design (Streamlit App User Interface)

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Bug Reports 🐞

I've added links to the bug reports from my GitHub Project in my README.md table below.

### Known bugs ❌

**Known bugs** are issues in the code that still need to be fixed. These include problems that have been identified but require further investigation, resources, or future updates to resolve.

| Bug Description | Bug Report Link | Bug Type |
| --------------- | --------------- | -------- | --- |
|                 |                 |          |     |

### Fixed bugs ✅

**Fixed bugs** are issues that have been successfully resolved. Documenting fixed bugs helps track progress and provides solutions for similar issues that may arise in the future.

| Bug Description | Bug Report Link                                                                                                               | Bug Type                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 🐞 Bug Report:  | Subject: Kaggle Dataset Download 403 Forbidden Error [#12](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2/issues/2) | 🐞Bug: Authentication Error 🔒 |
| 🐞 Bug Report:  | Subject: Bug with GitHub file size limits when pushing large CSV files [#13](https://github.com/Blignaut24/About-BulldozerPriceGenius-_BPG-_v2/issues/1)  | 🐞Bug: File Size Limit Error 💾

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Deployment

### Heroku

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

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Tools

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Credits

### Content
- **Dataset Source** :The dataset used in this project is sourced from the [Kaggle Bluebook for Bulldozers Competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview)

### Tutorials
- **Blog**: The project structureinspired by Daniel Bourke's [A 6-step field guide for building machine learning projects](https://www.mrdbourke.com/a-6-step-field-guide-for-building-machine-learning-projects/)
- **Code Institute's Data Analytics Course**: provides tutorial lessons for basic project setup - [Course Link](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/)
- **YouTube** [*How to Setup Git LFS for New and Existing Projects (Works With Unity)*](https://www.youtube.com/watch?v=4Ln6iRh_LTo): This project uses Git LFS (Large File Storage) for handling large files. The Git LFS setup and implementation was guided by Max O'Didily's comprehensive tutorial. For detailed setup instructions and best practices, please refer to the Git LFS documentation and resources [**Link**](https://www.youtube.com/watch?v=4Ln6iRh_LTo)
<br>**Requirements**
  - Git Bash
  - Git LFS<a href="7"/><a href="8"/>
<br>


### Media

- **Bulldozer image**: Sourced from [Freepik.com](http://Freepik.com) with free license

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

## Acknowledgements (optional)

- Thank the people who provided support through this project.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

#FIXME: Delete later

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
