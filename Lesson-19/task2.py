import pandas as pd


file_path = 'Lesson-19/Euro_2012_stats_TEAM.csv'

df = pd.read_csv(file_path)
# print(df)

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

num_teams = df['Team'].nunique()
print("\nTeams participated in the Euro2012:", num_teams)

high_scoring_teams = df[df['Goals'] > 6]
print("\n", high_scoring_teams)