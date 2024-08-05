import streamlit as st

import numpy as np
import pandas as pd

from model_aug3 import process_new_anime

# st.write('Welcome to my app')

st.markdown("""# Japanese Tourism through Anime
### Travels to Japan Influenced by the Popularity of Anime Series""")

# with st.sidebar:
    # genre_entry = st.sidebar.text
genres = st.multiselect(
    'What are the genres of the anime you would like to create?',
    ['Action', 'Adventure', 'Comedy', 'Coming-of-age',
       'Dark fantasy', 'Drama', 'Fantasy', 'Harem', 'Historical', 'Horror',
       'Martial arts', 'Mecha', 'Mystery', 'Post-apocalyptic', 'Psychological',
       'Romance', 'Science Fiction', 'Slice of life', 'Space opera', 'Sports',
       'Supernatural', 'Suspense', 'Thriller'])
# st.write('You selected:', genres)

years = st.slider('For how many years are you planning your anime to run?', 1, 20)

# result = st.markdown("There's a ***(from saved model) certainty that your
# anime would contribute {result from passing the entry through the model} percent
# to the visits to japan.")

submitted = st.button("Submit", key="submit_button")
if submitted:
    if genres != []:
        st.write("Result:")
        with st.spinner('Calculating...'):
            prediction_result = process_new_anime(genres, years)

        genres = ','.join(genres)
        st.write(f"If a new anime is introduced in the genre of **{genres}**,")
        st.write(f"and stays on the air for **{years}** year(s),")
        st.write(f"there is an approximate %{np.round(prediction_result*100)[0]} chance of encouraging foreigners to visit Japan!")
    else:
        st.write("Please select a genre.")
    # st.write(f"{genres}")
