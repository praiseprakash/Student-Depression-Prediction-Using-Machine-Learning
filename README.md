# Student Depression Prediction Using Machine Learning

## Overview

Student mental health has become a significant concern due to increasing academic pressure, financial stress, workload, family expectations, and lifestyle challenges. Depression among students can negatively impact academic performance, social interactions, and overall well-being.

This project aims to develop a Machine Learning-based Student Depression Prediction System that can identify students who may be at risk of depression based on various academic, lifestyle, and mental health-related factors.

The system analyzes student information and predicts whether a student is likely to experience depression. The final model is deployed using Streamlit with MySQL integration for real-time prediction and data storage.

---

## Problem Statement

Early identification of depression among students is important for providing timely support and intervention. Traditional assessment methods can be time-consuming and may not always detect early warning signs.

The objective of this project is to build an intelligent prediction system that can analyze student-related factors and predict depression risk using Machine Learning techniques.

---

## Dataset Information

The dataset contains student-related information including:

* Gender
* Age
* Academic Pressure
* Study Satisfaction
* Sleep Duration
* Dietary Habits
* Degree
* Work/Study Hours
* Financial Stress
* Suicidal Thoughts
* Family History of Mental Illness
* Depression (Target Variable)

### Target Variable

* 0 = No Depression
* 1 = Depression

---

## Project Workflow

### 1. Data Collection

The student depression dataset was collected and loaded into a Pandas DataFrame for analysis.

### 2. Data Cleaning

Data cleaning was performed to improve data quality.

Activities performed:

* Removed duplicate records
* Handled missing values
* Removed irrelevant categories such as "Others" in Sleep Duration
* Verified data consistency

### 3. Exploratory Data Analysis (EDA)

EDA was performed to understand data distribution and identify relationships between features and depression.

Visualizations used:

* Histograms
* Box Plots
* Count Plots
* Correlation Heatmap

Key observations:

* Higher academic pressure is associated with higher depression risk.
* Financial stress shows a strong relationship with depression.
* Students with lower study satisfaction tend to have higher depression rates.
* Poor sleep duration is associated with increased depression risk.
* Suicidal thoughts show a strong correlation with depression.

---

## Feature Selection

Manual feature selection was performed using:

* Domain Knowledge
* Exploratory Data Analysis
* Correlation Analysis

Selected Features:

* Gender
* Age
* Academic Pressure
* Study Satisfaction
* Sleep Duration
* Dietary Habits
* Degree
* Work/Study Hours
* Financial Stress
* Suicidal Thoughts
* Family History of Mental Illness

---

## Data Preprocessing

### Label Encoding

Degree values were converted into numerical format using LabelEncoder.

### Ordinal Encoding

OrdinalEncoder was used for:

* Sleep Duration
* Dietary Habits

These features have a natural order and were encoded accordingly.

### Feature Scaling

StandardScaler was applied to numerical features:

* Age
* Academic Pressure
* Study Satisfaction
* Work/Study Hours
* Financial Stress

This ensures all features are on a similar scale.

### Pipeline and ColumnTransformer

Pipeline was used to automate preprocessing steps.

ColumnTransformer was used to apply different preprocessing techniques to different feature groups.

---

## Train-Test Split

The dataset was divided into:

* Training Data: 80%
* Testing Data: 20%

This allows the model to learn patterns from training data while evaluating performance on unseen data.

---

## Machine Learning Models Evaluated

The following algorithms were tested:

### Logistic Regression

Parameters:

* C = 0.1
* max_iter = 1000

### Random Forest

Parameters:

* n_estimators = 300
* max_depth = 15
* random_state = 42

### Support Vector Machine (SVM)

Parameters:

* C = 10
* kernel = RBF
* gamma = scale

---

## Model Selection

Model performance was compared using classification metrics.

Final Model Selected:

### Logistic Regression

Reasons:

* Suitable for binary classification problems
* Works well on structured/tabular data
* Provides probability predictions
* Fast and efficient
* Achieved the highest accuracy

### Final Accuracy

**85%**

---

## Deployment

The trained model was deployed using Streamlit.

Features available:

* User-friendly web interface
* Real-time depression prediction
* Risk percentage calculation
* Interactive dashboard
* Prediction history storage

---

## MySQL Integration

MySQL was used to store:

* Student details
* Prediction results
* Historical prediction records

This allows tracking and analysis of prediction history.

---

## Dashboard Features

The Streamlit dashboard includes:

* Total Predictions
* Prediction Distribution
* Gender Distribution
* Financial Stress Distribution
* Prediction History Table

Interactive visualizations were created using Plotly.

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Plotly
* Streamlit
* Pickle

### Database

* MySQL

### Machine Learning

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)

---

## Future Scope

* Improve prediction accuracy using larger datasets.
* Apply advanced machine learning and deep learning models.
* Add personalized mental health recommendations.
* Deploy the system on cloud platforms.
* Integrate real-time monitoring and reporting features.

---

## Conclusion

This project demonstrates how Machine Learning can be used to predict depression risk among students using academic, lifestyle, and mental health-related factors. Logistic Regression achieved an accuracy of approximately 85% and was successfully deployed using Streamlit with MySQL integration. The system can serve as an early screening tool to support student mental health awareness and intervention.
