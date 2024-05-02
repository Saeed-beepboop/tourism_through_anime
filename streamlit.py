import streamlit as st

import numpy as np
import pandas as pd

from model import process_new_anime

# st.write('Welcome to my app')

st.markdown("""# Japanese Tourism Advertising
## via the Popularity of Anime Series
### Live Demo""")

# with st.sidebar:
    # genre_entry = st.sidebar.text
genres = st.multiselect(
    'What are the genres of the anime you would like to create?',
    ['Action', 'Adventure', 'Alternate history',
       'Bangsian fantasy', 'Body horror', 'Comedy', 'Comedy drama',
       'Coming-of-age', 'Crime', 'Crime Girls with guns', 'Cyberpunk',
       'Dark comedy', 'Dark fantasy', 'Demographic', 'Drama', 'Fantasy',
       'Harem', 'Historical', 'Historical Fiction', 'Horror', 'Magical girl',
       'Martial arts', 'Mecha', 'Murder mystery', 'Musical', 'Mystery',
       'Neo-noir', 'Post-apocalyptic', 'Pseudo-historical',
       'Psychological horror', 'Psychological thriller', 'Reverse harem',
       'Romance', 'Romantic comedy', 'Romantic drama', 'Samurai',
       'Science Fiction', 'Science fantasy', 'Slice of life', 'Space',
       'Sports', 'Spy', 'Steampunk', 'Supernatural', 'Supernatural horror',
       'Supernatural thriller', 'Surrealism', 'Thriller', 'Tragedy', 'Vampire',
       'Western'])
# st.write('You selected:', genres)

years = st.slider('For how many years are you planning your anime to run?', 1, 20)

# result = st.markdown("There's a ***(from saved model) certainty that your
# anime would contribute {result from passing the entry through the model} percent
# to the visits to japan.")

submitted = st.button("Submit", key="submit_button")
if submitted:
    with st.spinner('Calculating...'):
        prediction_result = process_new_anime(genres, years)

    st.write(f"If a new anime is introduced in the genre of {genres} and stays on the air for {years} year(s), we can say, with an estimation of 94.27 accuracy, that it has an approximate {np.round(prediction_result*100)[0]} percent chance of encouraging foreigners to visit Japan! ****")
