import pandas as pd

mvps = pd.read_csv('mvp_votes/csv/mvps.csv')

# Elimino alcune colonne aggiuntive che si trovano anche nel file delle statistiche dei giocatori
mvps = mvps[['Player','Year','Pts Won', 'Pts Max', 'Share']]


players = pd.read_csv('mvp_votes/csv/player_stats.csv')
del players['Rk']
del players['Unnamed: 0']
players['Player'] = players['Player'].str.replace('*', '', regex=False)
players.groupby(['Player', 'Year'])
print(players)
# Dobbiamo assicurarci che ogni gruppo abbia una sola riga
def single_player_2(df):
    if df.shape[0] == 1:
        return df
    else:
        tot_row_index = df[df['Tm'] == 'TOT'].index
        
        if not tot_row_index.empty:
            last_team = df.iloc[-1]['Tm']
            df.loc[tot_row_index, 'Tm'] = last_team
            df = df.loc[tot_row_index]
        return df

cleaned_players = players.groupby(['Player', 'Year']).apply(single_player_2).reset_index(drop=True)

print(cleaned_players.head(20))

# Merge dei due DF

combined = cleaned_players.merge(mvps, how='outer', on=['Player', 'Year']) # Non tutte le colonne, rimuovo tutti coloro che non hanno vinto l'mvp

# Ci sono colonne vuote, le sostituiamo con degli 0
combined[['Pts Won', 'Pts Max', 'Share']] = combined[['Pts Won', 'Pts Max', 'Share']].fillna(0)


# CLEANING TEAM DATA

team_rec = pd.read_csv('mvp_votes/csv/team_records.csv')
team_rec['Team'] = team_rec['Team'].str.replace('*', '', regex=False)
del team_rec['Unnamed: 0']

# Abbiamo il nome completo della squadra, ma nella combinazione abbiamo il nome abbreviato delle squadre.
# Dobbiamo trovare il modo di aggiungere il nickname nella colonna della squadra o di aggiungere il nome completo della squadra nel DF combinato.
# Utilizzeremo il file nicknames.csv che corrisponde al nome breve e al nome completo delle squadre

nicknames = {}

with open('mvp_votes/csv/nicknames.csv') as f:
    lines = f.readlines() #  Questo è un elenco chiamato lines che contiene tutti i dati del nostro file
    for line in lines[1:]:
        abbrev, name = line.replace('\n', '').split(',') # Ogni elemento di questa lista è costituito dall'abbreviazione, poi dalla virgola e dal nome completo. Li assegniamo a due variabili
        nicknames[abbrev] = name  # Le inseriamo nel dizionario.

combined['Team'] = combined['Tm'].map(nicknames) # Creiamo nel dataframe combinato una colonna con il nome completo della squadra.

# Ora abbiamo tutto ciò che ci serve per unire il DF combinato e il DF dei nomi delle squadre.

stats = combined.merge(team_rec, how='outer', on=['Team', 'Year'])
stats = stats[stats['Player'] != 'Player']


# print(stats['GB'].unique())  # C'è un "—" che è uguale a dire che ci sono 0 GB ossia che una squadra è in testa
stats['GB'] = stats['GB'].str.replace('—', '0')

stats = stats.apply(pd.to_numeric, errors='ignore') 

# Scrivo i risultati su un csv
stats.to_csv('mvp_votes/csv/players_mvps_stats.csv')
