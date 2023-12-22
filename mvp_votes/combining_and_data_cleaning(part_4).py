# Team losing record --> unlikely to win mvp

# Cleaning mvps data
import pandas as pd
mvps = pd.read_csv('mvp_votes/csv/mvps.csv')
# print(mvps)

# Get rid of some extra columns --> TRB, AST, STL, BLK, FG%, FT%, are also in the player stats file
mvps = mvps[['Player','Year','Pts Won', 'Pts Max', 'Share']] # Use the double square brackets to create a list of column names. This will select the specified columns from the DataFrame
# print(mvps)

# Cleaning players data
players = pd.read_csv('mvp_votes/csv/player_stats.csv')
# print(players)
# print(players.columns)
del players['Rk']
del players['Unnamed: 0']

# Players data has some names with * and there are several rows fo the same players in the same year, each one has to have only one row
# get rid of the extraneous rows

players['Player'] = players['Player'].str.replace('*', '', regex=False)


# players.groupby(['Player', 'Year']) # We now have group.by, we can get a single group by using get_group
# print(players.groupby(['Player', 'Year']).get_group(('LeBron James', 2005)))

# We have to make sure each group only have one row. Let's create a function
""" 
def single_player(df):
    if df.shape[0]==1:
        return df
    else:
        row = df[df['Tm'] == 'TOT'] # TOT is not  valid team so we cannot combine data --> we have to replace it with the last team he played for. It's in chronological order
        row['Tm'] = df.iloc[-1:]['Tm']
        return row 
 """
""" 
def single_player_2(df):
    if df.shape[0] == 1:
        return df
    else:
        last_team = df.iloc[-1]['Tm']
        df.loc[df['Tm'] == 'TOT', 'Tm'] = last_team
        return df


players.groupby(['Player', 'Year']).apply(single_player_2)

print(players.head(20))
 """


""" def single_player_2(df):
    if df.shape[0] == 1:
        return df
    else:
        # Find the row with 'Tm' == 'TOT'
        tot_row = df[df['Tm'] == 'TOT']
        
        if not tot_row.empty:
            # Replace 'TOT' with the last team the player played for
            last_team = df.iloc[-1]['Tm']
            df.loc[df['Tm'] == 'TOT', 'Tm'] = last_team
            df = tot_row
        return df
 """    

def single_player_2(df):
    if df.shape[0] == 1:
        return df
    else:
        # Find the row with 'Tm' == 'TOT'
        tot_row_index = df[df['Tm'] == 'TOT'].index
        
        if not tot_row_index.empty:
            # Replace 'TOT' with the last team the player played for
            last_team = df.iloc[-1]['Tm']
            df.loc[tot_row_index, 'Tm'] = last_team
            df = df.loc[tot_row_index]
        return df
    
# Apply the single_player_2 function to each group defined by 'Player' and 'Year'
cleaned_players = players.groupby(['Player', 'Year']).apply(single_player_2).reset_index(drop=True)

# Now 'cleaned_players' contains the DataFrame with the adjustments made by the single_player_2 function
# print(cleaned_players.head(20))

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