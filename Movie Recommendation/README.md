# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on a user's selection.

## Project Overview
This project uses a dataset of movies to calculate similarity scores between them. It provides a web-based interface built with Streamlit where users can select a movie and get 5 recommended movies along with their posters.

## Features
- Search from thousands of movies.
- Fetches real-time posters using The Movie Database (TMDB) API.
- Intuitive and responsive UI built with Streamlit.

## Implementation
- **Data**: Processed using Pandas in `recommendation.ipynb`.
- **Similarity**: Calculated using Vectorization and Cosine Similarity.
- **Frontend**: Streamlit (`app.py`).

## How to Run
1. Install requirements:
   ```bash
   pip install streamlit requests pandas scikit-learn
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
