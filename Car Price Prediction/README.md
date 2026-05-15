# Car Price Prediction

A machine learning application to predict the selling price of used cars based on historical data from Quikr.

## Overview
This project uses a Linear Regression model to estimate car prices. It processes raw data from the Quikr platform, cleans it, and trains a predictive model that takes into account the car's company, name, year of purchase, fuel type, and kilometers driven.

## Features
- **Data Cleaning Pipeline**: Handles inconsistent data formats in the Quikr dataset.
- **Predictive Modeling**: Uses Linear Regression with high accuracy.
- **Web App**: A Flask-based interface where users can select car details and get an instant price prediction.

## Technologies Used
- **Python**
- **Flask** (Backend)
- **Scikit-Learn** (Machine Learning)
- **Pandas/NumPy** (Data Processing)

## Installation & Usage
1. Install the required libraries:
   ```bash
   pip install flask pandas scikit-learn numpy
   ```
2. Run the Flask application:
   ```bash
   python application.py
   ```
3. Access the app in your browser at the local address provided (usually `http://127.0.0.1:5000`).

## Dataset
The project uses the `quikr_car.csv` dataset, which contains information about various used car listings.
