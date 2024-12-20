# Customer Churn Prediction - MLOps End-to-End Project

## Overview

This project demonstrates the implementation of an **End-to-End MLOps pipeline** for predicting customer churn using IBM's Customer Churn dataset. It combines various stages of the machine learning lifecycle, including **data preprocessing**, **model training**, **deployment**, and **monitoring** in a seamless and automated pipeline. The goal of this project is to predict which customers are likely to churn (i.e., leave the service), enabling businesses to take proactive measures to retain them.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Steps](#steps)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Description

Customer churn is a critical problem for businesses, especially in subscription-based industries. Predicting which customers are at risk of leaving can help companies take preventive actions, such as offering personalized promotions or improving customer service. This project uses machine learning to analyze customer data and predict churn based on historical patterns.

The project follows the MLOps methodology to automate the machine learning pipeline, making it easier to deploy, monitor, and maintain the model. It includes:

1. **Data Preprocessing**: Cleaning and preparing the dataset for modeling.
2. **Model Training**: Using classification algorithms to train the churn prediction model.
3. **Model Evaluation**: Evaluating the model using metrics like accuracy, precision, recall, and F1-score.
4. **Deployment**: Deploying the trained model using tools like Docker and Kubernetes for scaling.
5. **Monitoring**: Setting up monitoring to track the model's performance in production.

## Technologies Used

- **Python**: Programming language used for data analysis and modeling.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Scikit-learn**: For building machine learning models and evaluation.
- **Matplotlib / Seaborn**: For data visualization.
- **Flask**: For creating a simple web API to serve the model.
- **Docker**: For containerizing the application and model.
- **Kubernetes**: For orchestrating containers and managing the deployment.
- **MLflow**: For tracking experiments and model versioning.
- **TensorFlow** (optional): For more advanced machine learning models (e.g., neural networks).
- **Jupyter Notebook**: For interactive development and analysis.

## Dataset

The **IBM Customer Churn dataset** contains customer information such as demographics, account information, and services used. The dataset also includes a column that indicates whether the customer has churned (left the service) or not.

- **Source**: [Kaggle - IBM Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Features**:
  - Customer ID
  - Gender
  - SeniorCitizen
  - Partner
  - Dependents
  - Tenure
  - PhoneService
  - MultipleLines
  - InternetService
  - OnlineSecurity
  - OnlineBackup
  - DeviceProtection
  - TechSupport
  - StreamingTV
  - StreamingMovies
  - Contract
  - PaperlessBilling
  - PaymentMethod
  - MonthlyCharges
  - TotalCharges
  - Churn (Target variable)

## Steps

### 1. **Data Preprocessing**:
   - Loading and cleaning the dataset.
   - Handling missing values.
   - Encoding categorical variables.
   - Feature scaling and normalization.

### 2. **Exploratory Data Analysis (EDA)**:
   - Visualizing relationships between features.
   - Identifying important features affecting customer churn.
   - Using correlation matrices and pairplots.

### 3. **Model Training and Evaluation**:
   - Splitting the dataset into training and testing sets.
   - Training machine learning models (e.g., Logistic Regression, Random Forest, XGBoost).
   - Hyperparameter tuning using GridSearchCV.
   - Evaluating models with classification metrics (accuracy, precision, recall, F1-score).

### 4. **Deployment**:
   - Building a REST API using Flask to serve the trained model.
   - Dockerizing the application for easy deployment.
   - Deploying the application using Kubernetes.

### 5. **Monitoring**:
   - Setting up monitoring tools to track model performance and data drift.
   - Collecting and analyzing real-time metrics.

## Model

In this project, several machine learning models are trained and compared for predicting customer churn, including:

- **Logistic Regression**
- **Random Forest**
- **Gradient Boosting (XGBoost)**

The best-performing model is chosen based on evaluation metrics like accuracy, recall, and F1-score. The final model is deployed for inference.

## Installation

### Prerequisites
To run this project, you need to have Python 3.x installed. Additionally, you need to install the required libraries. You can do this by creating a virtual environment and installing the dependencies via `pip`.


