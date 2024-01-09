import requests as rq
import pandas as pd
from bs4 import BeautifulSoup

# I record delle squadre sono molto importanti per prevedere che vincerà il titolo di MVP


# Download pagine html contenti i dati per tutti gli anni
team_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'
years= range(1993,2024)
for year in years:
    url = team_stats_url.format(year)
    data = rq.get(url)
    with open('mvp_votes/team_records/{}team_records.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(data.text) 


# Provo ad estrarre dati per il primo anno (Eastern Conference)
year= 1993
with open('mvp_votes/team_records/{}team_records.html'.format(year), encoding='utf-8') as f:
    page = f.read()
soup = BeautifulSoup(page, 'html.parser')
for element in soup.find_all('tr', class_='thead'):
    element.decompose()
teams_record_table_East_1993 = soup.find(id="divs_standings_E")

teams_record_Eastern_Conference_1993 = pd.read_html(str(teams_record_table_East_1993))[0]

# Itero per tutti gli anni 
dfs = []
years= range(1993,2024)
for year in years:
    with open('mvp_votes/team_records/{}team_records.html'.format(year), encoding= 'utf-8') as f:
        page = f.read()

# Tabella Eastern Conference
    soup = BeautifulSoup(page, 'html.parser')
    for element in soup.find_all('tr', class_='thead'):
        element.decompose()
    teams_record = soup.find(id="divs_standings_E")
    teams_record_table_E = pd.read_html(str(teams_record))[0]
    teams_record_table_E['Year'] = year
    teams_record_table_E['Team'] = teams_record_table_E['Eastern Conference']
    del teams_record_table_E['Eastern Conference']
    dfs.append(teams_record_table_E)

# Tabella Western Conference
    soup = BeautifulSoup(page, 'html.parser')
    for element in soup.find_all('tr', class_='thead'):
        element.decompose()
    teams_record = soup.find(id="divs_standings_W")
    teams_record_table_W = pd.read_html(str(teams_record))[0]
    teams_record_table_W['Year'] = year
    teams_record_table_W['Team'] = teams_record_table_W['Western Conference']
    del teams_record_table_W['Western Conference']
    dfs.append(teams_record_table_W)

# Creo un unico Dataset
teams_record_table_def = pd.concat(dfs)

# Scrivo i risultati su un csv
teams_record_table_def.to_csv('mvp_votes/csv/team_records.csv')
