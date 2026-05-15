# WhatsApp Chat Analyzer

A Python-based Streamlit web application that analyzes exported WhatsApp chat text files and provides comprehensive statistical insights, visualizations, and activity mappings.

## Features

- **Top Statistics**: Displays total messages, total words, media shared, and links shared.
- **Monthly & Daily Timelines**: Visualizes message frequency over time to show trends and usage patterns.
- **Activity Maps**: Identifies the most active days of the week and months of the year.
- **Weekly Activity Heatmap**: Shows the busiest times of day over the entire week.
- **Most Busy Users**: Find out who texts the most in a group chat.
- **Word Cloud & Common Words**: Generates a word cloud and a bar chart of the most frequently used words (ignoring common stop words/Hinglish stop words).
- **Emoji Analysis**: Analyzes and visualizes the most frequently used emojis.

## Tech Stack

- **Python**: Core logic and scripting.
- **Streamlit**: Web interface and interactive UI.
- **Matplotlib & Seaborn**: Data visualization and plotting.
- **Pandas**: Data manipulation and analysis.

## Project Structure

- `app.py`: The main Streamlit application script containing the UI and layout.
- `helper.py`: Contains helper functions to extract specific statistics and generate dataframes for visualization.
- `preprocessor.py`: Handles the parsing and preprocessing of the raw WhatsApp chat text file into a structured Pandas DataFrame.
- `stop_hinglish.txt`: A custom list of Hinglish stop words used to filter out common conversational filler words during word frequency analysis.

## How to Run locally

1. **Clone the repository** (or download the source code).
2. **Install the required dependencies**:
   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

3. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

4. **Upload your chat**: 
   - Export a chat from WhatsApp (without media) to get a `.txt` file.
   - Upload this text file using the sidebar in the application.
   - Select a specific user or "Overall" to view the statistics and click **"Show Analysis"**.

## Usage Note
Please ensure your WhatsApp chat is exported in the 24-hour time format standard for the preprocessor to correctly parse the dates and times. If your export is different, you might need to adjust the regex pattern in `preprocessor.py`.
