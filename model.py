import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from sklearn import model_selection, datasets
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle

def process_new_anime(user_genres:list, user_years:int):
    # pass
    # Define the data as a dict, then insert all the columns (Years_on_air and all the genres) with values 0.
    # d = {'Years_on_air': [user_years], 'col2': [3, 4]}
    d = {'Years_on_air': [user_years]}
    # Create a dataframe for the new entry.
    user_df = pd.DataFrame(data=d)
    # Update columns with the values given by the user.
    # Pass it through the saved model.

# anime_df_test["Aired_start"] = 0
# anime_df_test["Aired_end"] = 0
# for years in L:
#     year_range = anime_df_test["Aired"][years].split("-")
#     start_year = int(year_range[0])
#     end_year = int(year_range[1])
#     anime_df_test["Aired_start"][years] = start_year
#     anime_df_test["Aired_end"][years] = end_year

# anime_df_test['affect_on_jpvisits'] = 0
# for row in L:
#     if anime_df_test['Aired_start'][row] <= 1995:
#         anime_df_test['affect_on_jpvisits'][row] = 0
#     elif anime_df_test['Aired_start'][row] == anime_df_test['Aired_end'][row]:
#         visits = jpvisitssimp_df['average_visits'][jpvisitssimp_df['year'] == anime_df_test['Aired_start'][row]].tolist()[0]
#         votes_to_visits_ratio = anime_df_test['Votes'][row] / visits
#         anime_df_test['affect_on_jpvisits'][row] = votes_to_visits_ratio
#     else:
#         for year in range(anime_df_test['Aired_start'][row], anime_df_test['Aired_end'][row]):
#             visits_list = []
#             visits = jpvisitssimp_df['average_visits'][jpvisitssimp_df['year'] == year].tolist()[0]
#             visits_list.append(visits)
#             visits_sum = sum(visits_list)
#             votes_to_visits_ratio = anime_df_test['Votes'][row] / visits_sum
#             anime_df_test['affect_on_jpvisits'][row] = votes_to_visits_ratio

# rb_scaler = RobustScaler()
# rb_scaler.fit(anime_df_test[['Votes']])
# anime_df_test['Votes'] = rb_scaler.transform(anime_df_test[['Votes']])

# anime_df_test['Years_on_air'] = 0
# for row in L:
#     if anime_df_test['Aired_end'][row] - anime_df_test['Aired_start'][row] == 0:
#         anime_df_test['Years_on_air'][row] = 1
#     else:
#         new_col = anime_df_test['Aired_end'][row] - anime_df_test['Aired_start'][row]
#         anime_df_test['Years_on_air'][row] = new_col

# genres = anime_df_test['Genre'].str.get_dummies(sep=', ')
# animeencoded_df_test = pd.concat([anime_df_test, genres], axis=1)
# # animeencoded_df.drop('Genre', axis=1, inplace=True)
# animeencoded_df_test




# genres = anime_df['Genre'].str.get_dummies(sep=', ')
    genre_columns = ['Action', 'Adventure', 'Alternate history', 'Bangsian fantasy',
        'Body horror', 'Comedy', 'Comedy drama', 'Coming-of-age', 'Crime',
        'Crime Girls with guns', 'Cyberpunk', 'Dark comedy', 'Dark fantasy',
        'Demographic', 'Drama', 'Fantasy', 'Harem', 'Historical',
        'Historical Fiction', 'Horror', 'Magical girl', 'Martial arts', 'Mecha',
        'Murder mystery', 'Musical', 'Mystery', 'Neo-noir', 'Post-apocalyptic',
        'Pseudo-historical', 'Psychological horror', 'Psychological thriller',
        'Reverse harem', 'Romance', 'Romantic comedy', 'Romantic drama',
        'Samurai', 'Science Fiction', 'Science fantasy', 'Slice of life',
        'Space', 'Sports', 'Spy', 'Steampunk', 'Supernatural',
        'Supernatural horror', 'Supernatural thriller', 'Surrealism',
        'Thriller', 'Tragedy', 'Vampire', 'Western']
    new = pd.DataFrame()
    for col in genre_columns:
        # new[[f'{col}']] = pd.DataFrame([[0]], index=anime_df_test.index)
        new[[f'{col}']] = pd.DataFrame([[0]], index=user_df.index)

    user_df = pd.concat([user_df, new], axis=1)

    # genres_test = anime_df_test['Genre'].str.get_dummies(sep=', ')
    # animeencoded_df_test = pd.concat([anime_df_test, genres], axis=1)

    # for g in user_genres:
    #     user_df[g] = user_df[g].map({g: 1})
    for g in user_genres:
        g_column = user_df[g]
        new_g_column = 1
        user_df[g] = new_g_column

    # animeencoded_df_test.update(genres_test)



# x_new = animeencoded_df_test.drop(['Name', 'Type', 'Aired', 'Rating', 'Votes', 'Discription', 'Studio',
#        'Genre', 'Aired_start', 'Aired_end', 'affect_on_jpvisits'], axis=1)


    loaded_model = joblib.load("Completed_model.joblib")
    # result = loaded_model.score(X_test, y_test)
    # print(result)

    # result = loaded_model.score(X_test, y_test)
    new_predictions = loaded_model.predict(user_df)
    # print(f"\n**** What all this means is that:\nIf a new anime is introduced\nin the genre of {animeencoded_df_test['Genre'][L[0]]} and\nstays on the air for {animeencoded_df_test['Years_on_air'][L[0]]} year(s),\nwe can say, with an estimation of {round(score*100, 2)} accuracy, that\nit has {round(new_predictions[0]*100, 2)} percent chance of encouraging foreigners to visit Japan! ****")


    return new_predictions
