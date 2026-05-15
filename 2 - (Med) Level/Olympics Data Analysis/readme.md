# Olympics Data Analysis End-to-End Project

This is an interactive web application built with **Streamlit** that provides a comprehensive and visual analysis of the historical data of the modern Olympic Games (from Athens 1896 up to Rio 2016). It includes detailed statistics about nations, events, sports, and individual athletes based on 120 years of Olympic history.

## 🌟 Features

The application provides analyses divided into four main sections:

### 1. 🥇 Medal Tally
View the all-time historic medal tally, or filter the exact tally of Gold, Silver, and Bronze medals by:
- **Specific Year**
- **Specific Country**

### 2. 📊 Overall Analysis
Provides a top-level, global overview of the entire history of the Olympics:
- High-level statistics (Host Cities, Total Editions, Events, Participating Nations).
- Line charts showing the growth in participating nations, events, and athletes over the years.
- A heatmap visualizing the number of events per sport over time.
- A list of the most successful athletes of all time (globally or across specific sports).

### 3. 🌍 Country-wise Analysis
Deep dive into an individual country's performance:
- A line chart showing the total medals won by the selected country over the years.
- A heatmap highlighting the sports where the selected country excels.
- A leaderboard displaying the top 10 most successful athletes from that country.

### 4. 🏃 Athlete-wise Analysis
Insights based on the athletes' physical attributes and biographies:
- Distribution of age across all participants versus medalists (Gold, Silver, Bronze).
- Age distribution of Gold medalists broken down by famous sports.
- A scatter plot visualizing the Height vs. Weight of athletes separated by sport and gender.
- A multi-line chart depicting Men vs. Women participation over the years.

## 🛠️ Technology Stack
- **Python**: Core programming language.
- **Streamlit**: For the interactive web app framework and UI components.
- **Pandas**: For fast and efficient data manipulation and preprocessing.
- **Plotly Express / Figure Factory**: For building interactive and analytical graphs.
- **Matplotlib & Seaborn**: For specialized static visualizations like heatmaps and scatter plots.

## 🚀 How to Run the App Locally

### Prerequisites
Make sure you have Python installed. It's recommended to work within a virtual environment.

### 1. Clone the repository and install dependencies
```bash
pip install -r requirements.txt
```
*(Make sure `streamlit`, `pandas`, `plotly`, `matplotlib`, and `seaborn` are installed)*

### 2. Prepare the datasets
This project uses the famous **120 years of Olympic history: athletes and results** dataset. You need two CSV files in the project root:
- `athlete_events.csv`
- `noc_regions.csv`

### 3. Run the Streamlit User Interface
```bash
streamlit run app.py
```
This will launch a local server and automatically open the application in your default web browser on `http://localhost:8501`.

## 📁 Repository Structure

- `app.py`: The main running application file that contains all Streamlit front-end logic and routings.
- `helper.py`: Contains modular utility functions for slicing and grouping the Pandas dataframes to keep `app.py` clean.
- `preprocessor.py`: A small data cleaning script that filters the dataset for Summer Olympics and merges the NOC region names.
- `athlete_events.csv` / `noc_regions.csv`: Data files (please download from Kaggle if missing).
