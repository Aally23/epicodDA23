import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mvp_votes/csv/players_mvps_stats.csv')

# print(df.columns)

# Who scored the most points in the alla dataset?
# highest_scoring = df[df['G'] > 70].sort_values('PTS', ascending=False)
# highest_scoring_10 = highest_scoring.head(10)
# print(highest_scoring)

# highest_scoring_10.plot.bar(x='Player', y='PTS')
# plt.show()

# Who scored the most for each year?
""" highest_scoring_per_year = df.sort_values(by='PTS', ascending=False).groupby('Year').first()
highest_scoring_per_year_reset = highest_scoring_per_year.reset_index()

# Ora puoi usare 'Year' come colonna regolare
highest_scoring_per_year_reset.plot(kind='bar', x='Year', y='PTS')

plt.show() """

highest_per_year = df.groupby('Year').apply(lambda x: x.sort_values('PTS', ascending=False).head(1))

# print(highest_per_year)

def highest_pts(df):
    return df.sort_values('PTS', ascending=False).head(1)

highest_per_year_2 = df.groupby('Year').apply(highest_pts)
# print(highest_per_year_2)

# print(df.corr()['Share'].sort_values(ascending=False)) # Finding correlation with shares

df.corr()['Share'].plot(kind='bar') # Correlation
# plt.show()