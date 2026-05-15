# SMS Spam Classifier

A machine learning application that classifies SMS messages into "Spam" or "Ham" (not spam).

## Project Overview
This project uses Natural Language Processing (NLP) techniques to process text data and train a classification model. It includes a user-friendly Streamlit web application for real-time message testing.

## Workflow
1. **Preprocessing**: Lowercasing, tokenization, removing special characters, removing stop words/punctuation, and stemming.
2. **Vectorization**: Converting text data into numerical format using TF-IDF Vectorizer.
3. **Model**: Trained on the SMS Spam Collection dataset.
4. **Deployment**: Built using Streamlit.

## How to Run
1. Install dependencies:
   ```bash
   pip install streamlit nltk pandas scikit-learn
   ```
2. Download NLTK data (if not already present):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
