# T20 Cricket Score Predictor

A machine learning based web application that predicts the final score of a T20 cricket match in the first innings, based on the current match situation.

## 🚀 Features
- **Team Selection:** Predicts scores for major international T20 teams (Australia, India, England, Pakistan, etc.).
- **Venue Aware:** Considers the impact of different cities/venues on the score.
- **Dynamic Inputs:** Real-time prediction based on:
    - Batting & Bowling teams
    - Match City/Venue
    - Current Score
    - Overs completed (Effective after 5 overs)
    - Wickets fallen
    - Runs scored in the last 5 overs

## 🛠️ Technologies Used
- **Python**: Core programming language.
- **XGBoost**: For high-performance regression modeling.
- **Streamlit**: For creating the interactive web interface.
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Pickle**: For model serialization.

## 📁 Project Structure
- `app.py`: The main Streamlit application script.
- `data_extraction.ipynb`: Notebook containing data cleaning and initial processing steps.
- `feature_extraction.ipynb`: Notebook for feature engineering, model training, and exporting the pipeline.
- `dataset_level2.pkl`: Pre-processed dataset used for model development.
- `pipe.pkl`: The trained XGBoost regression pipeline (used by the app).

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "T20 score predictor"
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install streamlit pandas numpy xgboost scikit-learn
   ```

3. **Generate the Model:**
   If `pipe.pkl` is not present, run all cells in `feature_extraction.ipynb` to train the model and save the pipeline.

4. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## 📊 Methodology
The predictor uses historical T20 data to learn patterns between match situations and final scores. Key calculated features include:
- **CRR (Current Run Rate):** Current Score / Overs.
- **Balls Left:** Total balls (120) - balls delivered.
- **Wickets Left:** Total wickets (10) - wickets lost.
- **Last 5 Overs Momentum:** Captures the recent scoring trend.

---
Created by [Nitin](https://github.com/Nitin)
