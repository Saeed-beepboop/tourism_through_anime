anime_df['affect_on_jpvisits'] = 0
for row in range(0, 483):
    if anime_df['Aired_start'][row] == anime_df['Aired_end'][row]:
        visits = jpvisitssimp_df['average_visits'][jpvisitssimp_df['year'] == year].tolist()[0]
        votes_to_visits_ratio = anime_df['Votes'][row] / visits
        anime_df['affect_on_jpvisits'][row] = votes_to_visits_ratio
    else:         
        for year in range(anime_df['Aired_start'][row], anime_df['Aired_end'][row]):
            visits_list = []
            visits = jpvisitssimp_df['average_visits'][jpvisitssimp_df['year'] == year].tolist()[0]
            visits_list.append(visits)
            visits_sum = sum(visits_list)
            votes_to_visits_ratio = anime_df['Votes'][row] / visits_sum
            anime_df['affect_on_jpvisits'][row] = votes_to_visits_ratio