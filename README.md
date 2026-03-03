# AutoSales Intelligence Engine

A production-ready Machine Learning powered Automobile Sales Forecasting System designed to predict monthly vehicle sales using historical transactional data.

This project demonstrates a complete end-to-end ML lifecycle including data preprocessing, exploratory analysis, model development, API creation, and cloud deployment.


## Project Overview

The AutoSales Intelligence Engine helps automobile businesses forecast sales demand using historical sales patterns and business factors.

### Business Problem

Traditional manual forecasting methods often result in:
- Overstocking
- Understocking
- Revenue leakage
- Poor inventory turnover

This solution enables:
- Optimized inventory planning
- Reduced holding costs
- Improved demand forecasting
- Data-driven regional sales strategies

## Project Objectives

- Build a regression model to predict monthly automobile sales
- Identify key drivers influencing demand
- Deploy the trained model as a REST API
- Host the application on a cloud platform
- Maintain modular and scalable architecture

## Dataset Information

- Total Records: 100
- Total Features: 14
- Structured tabular dataset
- Contains categorical and numerical variables

### Key Columns:
- Region
- Product Category
- Date
- Quantity Sold (Target Variable)

## Exploratory Data Analysis (EDA)

Performed:
- Missing value detection
- Distribution analysis
- Monthly trend visualization
- Regional sales comparison

### Key Insights:
- Seasonal demand patterns observed
- Certain regions consistently outperform others
- Product category significantly impacts sales volume

## Data Preprocessing

Steps:
- Handling missing values
- Dropping irrelevant columns
- Date feature extraction (Month)
- One-hot encoding for categorical variables

## Feature Engineering

Engineered Features:
- Extracted Month from Date
- Encoded Region & Product Category

Purpose:
- Capture seasonality
- Improve model learning
- Represent categorical features numerically

## Model Development

**Algorithm Used:** Random Forest Regressor

### Why Random Forest?
- Handles non-linear relationships
- Reduces overfitting
- Works well with mixed data types
- Minimal scaling required

### Train-Test Split
- 80% Training
- 20% Testing

## Model Performance

- R² Score: 0.79
- Mean Absolute Error (MAE): 0.85

The model explains approximately 79% of variance in sales and maintains acceptable prediction error for business use.


##  Model Serialization

- Serialized using Pickle
- Stored as: `deployment/model.pkl`
- Enables production deployment without retraining

## API Development

Framework: Flask

### Endpoints

**GET /**
- Health check endpoint

**POST /predict**
- Accepts JSON input
- Returns predicted sales volume

### API Workflow
1. Receive JSON input
2. Convert to numpy array
3. Pass to trained model
4. Return prediction as JSON response

## Deployment

- Platform: Render
- Server: Gunicorn WSGI
- Deployment Type: Web Service

### Live API URL

https://autosales-intelligence-engine.onrender.com

## System Architecture

User → Flask API → ML Model → Prediction Response

Components:
- Client
- Flask Application
- Serialized ML Model
- Cloud Hosting (Render)

## Business Impact

- Improved forecasting accuracy
- Reduced stock-out incidents
- Better demand planning
- Increased operational efficiency

## Future Enhancements

- Implement XGBoost / LSTM models
- Add interactive dashboard
- Automate model retraining pipeline
- CI/CD integration
- Real-time forecasting

## Project Structure
├── data/
├── src/
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── predict.py
│ └── model_evaluation.py
├── deployment/
│ ├── app.py
│ ├── model.pkl
│ └── requirements.txt
├── notebooks/
└── README.md

## Author

Supraja Srinivasula  
Machine Learning & Data Science Enthusiast

## Conclusion

This project demonstrates strong capabilities in:
- End-to-end ML implementation
- Production-grade structuring
- REST API development
- Cloud deployment
- Business understanding

The system can be scaled into a full enterprise-level forecasting platform.
