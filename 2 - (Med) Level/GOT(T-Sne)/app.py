import streamlit as st
import pickle
import requests
import numpy as np

api_data = requests.get("").json()

import os

file_path = os.path.join(os.path.dirname(__file__), 'data.pkl')
df = pickle.load(open(file_path, 'rb'))
df = df.head(25)

df['character'] = df['character'].str.replace('Jaime','Jamie')
df['character'] = df['character'].str.replace('Lord Varys','Varys')
df['character'] = df['character'].str.replace('Bronn','Lord Bronn')
df['character'] = df['character'].str.replace('Sandor Clegane','The Hound')
df['character'] = df['character'].str.replace('Robb Stark','Rob Stark')

def fetch_image(name,api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']



st.title("Game Of Thrones Personality Matcher")

characters = df['character'].values

selected_character = st.selectbox("Select a character",characters)

# fetch closest match
character_id = np.where(df['character'].values == selected_character)[0][0]
x = df[['x','y']].values

distances = []
for i in range(len(x)):
    distances.append(np.linalg.norm(x[character_id] - x[i]))

recommended_id = sorted(list(enumerate(distances)),key=lambda x:x[1])[1][0]
recommended_character = df['character'].values[recommended_id]

image_url = fetch_image(selected_character,api_data)
recommended_character_image_url = fetch_image(recommended_character,api_data)
col1, col2 = st.columns(2)

with col1:
    st.header(selected_character)
    if image_url:
        st.image(image_url)
    else:
        st.write("Image not available")
with col2:
    st.header(recommended_character)
    if recommended_character_image_url:
        st.image(recommended_character_image_url)
    else:
        st.write("Image not available")