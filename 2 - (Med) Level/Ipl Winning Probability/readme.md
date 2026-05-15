# IPL Win Predictor

This project is a Machine Learning based web application built with **Streamlit** that predicts the winning probability of an ongoing Indian Premier League (IPL) cricket match.

## Project Overview

In a limited-overs cricket match, the situation changes dynamically after every ball. This application uses a pre-trained Machine Learning pipeline (`pipe.pkl`), which was trained on historical IPL data (`matches.csv` and `deliveries.csv`), to calculate the real-time winning probability of both the batting and bowling teams based on the match's current state.

### Features
The app takes the following inputs from the user during the second innings of an IPL match:
- **Batting Team:** The team currently chasing the target.
- **Bowling Team:** The team currently defending the target.
- **Host City:** The city where the match is being played.
- **Target:** The total runs scored by the team batting first + 1.
- **Current Score:** The runs scored so far by the batting team.
- **Overs Completed:** The number of overs bowled so far.
- **Wickets Out:** The number of wickets lost by the batting team.

Based on these inputs, it calculates the required run rate (RRR) and current run rate (CRR) and provides the win probability for both teams in percentages.

## Technologies Used
- **Python:** Programming Language
- **Streamlit:** For building the interactive web application interface
- **Pandas:** For data manipulation and creating dataframes for inference
- **Scikit-Learn:** For loading and utilizing the pre-trained pipeline model
- **Jupyter Notebook:** For initial data exploration, preprocessing, and model training (`win prediction.ipynb`)

## Setup and Installation

Follow these steps to run the application on your local machine:

1. **Navigate to the project directory:**
   ```bash
   cd Ipl-Winning-Probability
   ```

2. **Install the required dependencies:**
   Ensure you have Python installed. You can install the required libraries using pip:
   ```bash
   pip install streamlit pandas scikit-learn
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Web App:**
   Once the command runs successfully, it will open the application in your default web browser (typically at http://localhost:8501).

## Files Description
- `app.py`: The main Streamlit web application script.
- `win prediction.ipynb`: The Jupyter Notebook containing the data preprocessing, exploratory data analysis (EDA), and machine learning model training code.
- `matches.csv` & `deliveries.csv`: Historical IPL dataset used for training the model.
