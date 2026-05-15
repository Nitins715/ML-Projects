# Game Of Thrones Personality Matcher 🐺⚔️

A Streamlit-based Web Application that helps you discover similar characters from the Game of Thrones universe! It uses machine learning to plot characters in a 2D space (using dimensionality reduction methods like t-SNE) and calculates the closest "personality match" based on their traits or dialogues. 

## 🚀 Features

- **Character Selection**: Choose from 25 of the most iconic Game of Thrones characters.
- **Personality Matching**: Under the hood, this app computes the Euclidean distance between characters based on predefined traits (reduced to `x` and `y` coordinates) to recommend the most identical personality.
- **Dynamic Image Fetching**: Actively pulls character photographs in real-time from [ThronesAPI](https://thronesapi.com/) so you get visual references for both the character you selected and your recommended match!
- **Fallback Support**: Includes error handling just in case the API doesn't have an exact image for the targeted character.

## 📁 Project Structure

- `app.py`: The main Streamlit web application. Contains the UI and logical flow for finding and displaying character matches.
- `got.ipynb`: The Jupyter Notebook potentially used for data generation, exploration, and dimensionality reduction mapping (e.g. producing the embeddings).
- `script-bag-of-words.json`: The raw or processed data containing script info or Bag of Words representations.

## 🛠️ Prerequisites

Be sure you have Python installed as well as the following libraries:

```bash
pip install streamlit pandas numpy requests
```

## 💻 How to Run

1. Clone or download this repository.
2. Navigate to the project directory in your terminal:
   ```bash
   cd "ML-Projects/GOT(T-Sne)"
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Open the localhost URL (usually `http://localhost:8501`) inside your browser.

## ⚠️ Notes
- Ensure you have an active internet connection when launching the application, as it attempts to hit the `thronesapi.com` API right at the startup! 
- Some characters might lack an image mapping from the API. The app will smoothly display an "Image not available" fallback.