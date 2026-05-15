# Book Recommendation System

A content-based and popularity-based book recommendation system built using Python and Flask.

## Overview
This project provides book recommendations to users based on two main approaches:
1. **Popularity-Based**: Recommends the top 50 books with the highest average ratings (minimum 250 ratings).
2. **Collaborative Filtering / Content-Based**: Recommends similar books based on user input using a similarity matrix.

## Features
- **Top 50 Books**: Browse the most popular books on the home page.
- **Search Recommendation**: Enter a book title to get a list of 4 similar book recommendations.
- **Web Interface**: Easy-to-use UI built with Flask and HTML templates.

## Technologies Used
- **Python**
- **Flask** (Web Framework)
- **Pandas/NumPy** (Data Manipulation)
- **Scikit-Learn** (Cosine Similarity)
- **Pickle** (Model Serialization)

## Project Structure
- `app.py`: The Flask application backend.
- `bookrecommendation.ipynb`: Jupyter notebook containing data analysis and model building.
- `data/`: Directory for datasets.
- `templates/`: HTML templates for the web interface.

## Installation & Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5001`.
