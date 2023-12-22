import pandas as pd

mvps = pd.read_csv('mvp_votes/csv/mvps.csv')

# Elimino alcune colonne aggiuntive che si trovano anche nel file delle statistiche dei giocatori
mvps = mvps[['Player','Year','Pts Won', 'Pts Max', 'Share']]


players = pd.read_csv('mvp_votes/csv/player_stats.csv')
del players['Rk']
del players['Unnamed: 0']
players['Player'] = players['Player'].str.replace('*', '', regex=False)
players.groupby(['Player', 'Year']) 

# Dobbiamo assicurarci che ogni gruppo abbia una sola riga
def single_player_(df):
    if df.shape[0] == 1:
        return df
    else:
        tot_row_index = df[df['Tm'] == 'TOT'].index
        
        if not tot_row_index.empty:
            last_team = df.iloc[-1]['Tm']
            df.loc[tot_row_index, 'Tm'] = last_team
            df = df.loc[tot_row_index]
        return df

cleaned_players = players.groupby(['Player', 'Year']).apply(single_player_).reset_index(drop=True)

# Now 'cleaned_players' contains the DataFrame with the adjustments made by the single_player_2 function
print(cleaned_players.head(20))

# We don'tn need a multilevel index so we can drop it

# print(cleaned_players.head(20))

# Prova
""" if (cleaned_players['Tm'] == 'LAL').any():
    print(cleaned_players[cleaned_players['Tm'] == 'LAL'][['Player', 'Tm']])
else:
    print('Non ci sono colonne con TOT')
 """

""" lb = (cleaned_players[cleaned_players['Player'] == 'LeBron James']).groupby('Tm')
print(lb.get_group('LAL')) """


# Merge out two DF

combined = cleaned_players.merge(mvps, how='outer', on=['Player', 'Year']) # Not all of the columns. Inner mode get ride of anyone who didn't win mvp

# print(combined[combined['Player'] == 'Michael Jordan']) Prova!!!

# There are columns empty --> We want to replace that with 0s
combined[['Pts Won', 'Pts Max', 'Share']] = combined[['Pts Won', 'Pts Max', 'Share']].fillna(0)
# print(combined[combined['Share'] > 0.50])

# CLEANING TEAM DATA

team_rec = pd.read_csv('mvp_votes/csv/team_records.csv')
# print(team_rec)

team_rec['Team'] = team_rec['Team'].str.replace('*', '', regex=False)
# print(team_rec['Team'])
del team_rec['Unnamed: 0']
# print(team_rec)

""" if (team_rec['W'] == 50).any():
    print(team_rec.loc[team_rec['W'] == 50, ['W', 'Team', 'Year']])
else:
    print('NOOO') """

# print(team_rec['Team'].unique())

# We have the full name of the team but in the combined we have the short name of the teams
# We need to find the way to either add the nickname into the team column or add the full team name into the combined DF
# We will use the file nicknames.csv that matches the short and the full name of the teams

nicknames = {}

with open('mvp_votes/csv/nicknames.csv') as f:
    lines = f.readlines() # This is a list called lines that has all the data from our file
    for line in lines[1:]: # Spread up the lines
        abbrev, name = line.replace('\n', '').split(',') # Each item in this list is the abbreviation then comma then full name. We assign them to two variables
        nicknames[abbrev] = name # We put them into the dictionary. Keay are the abbreviation and the values are the full names
# print(nicknames)
combined['Team'] = combined['Tm'].map(nicknames) # We create in the combined dataframe a full team name column

""" combined.to_csv('mvp_votes/csv/check_combined.csv')
team_rec.to_csv('mvp_votes/csv/check_team_stats.csv') """

""" print(combined.shape)
print(team_rec.shape) """
# Now we have everything we need to merge combined DF and team name DF 
stats = combined.merge(team_rec, how='outer', on=['Team', 'Year'])
stats = stats[stats['Player'] != 'Player']
# print(stats)
# print(stats.dtypes) # We have to convert them to numerical type
# stats = stats.apply(pd.to_numeric, errors='ignore')
# print (stats.dtypes)

# print(stats['GB'].unique())  # There's dash == 0 GB, a team is in the lead
stats['GB'] = stats['GB'].str.replace('—', '0')
# print(stats['GB'].unique())

stats = stats.apply(pd.to_numeric, errors='ignore')
# print(stats.dtypes)

# Let's write it to csv to use it in machine learning later
stats.to_csv('mvp_votes/csv/players_mvps_stats.csv')

# Let's explore this file

# Who scored the most points in the alla dataset?
highest_scoring = stats[stats['G'] > 70].sort_values('PTS', ascending=False)
# print(highest_scoring)