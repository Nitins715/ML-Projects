# Laptop Price Predictor

A Streamlit-based web application that predicts the price of a laptop based on its configuration.

## Overview
This project uses a machine learning pipeline to estimate laptop prices. Users can input various specifications such as Brand, Type, RAM, Weight, Screen Size, Resolution, CPU, GPU, and Storage type to get a predicted price.

## Features
- **Interactive UI**: Built with Streamlit for a smooth user experience.
- **Comprehensive Inputs**: Supports detailed hardware configurations.
- **ML Pipeline**: Uses a pre-trained regression pipeline for inference.

## Technologies Used
- **Python**
- **Streamlit** (Web Interface)
- **Scikit-Learn** (ML Pipeline)
- **Pandas/NumPy** (Data Handling)
- **Pickle** (Model Deployment)

## Installation & Usage
1. Install dependencies:
   ```bash
   pip install streamlit scikit-learn pandas numpy
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Use the sidebar and input fields to configure your laptop and click "Predict Price".

## Files
- `app.py`: Streamlit application file.
- `Predictor.ipynb`: Data analysis and model training notebook.
- `laptop_data.csv`: Dataset used for training..