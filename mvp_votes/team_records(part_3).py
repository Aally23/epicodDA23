# team records are very important for the machine learning model to predict nba mvp
import requests as rq
""" 
team_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'
year = 1993
url = team_stats_url.format(year)
data = rq.get(url)
with open('mvp_votes/team_records/{}team_records.html'.format(year), 'w', encoding='utf-8') as f:
    f.write(data.text)
 """

# Create a loop
""" team_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'
years= range(1993,2024)
for year in years:
    url = team_stats_url.format(year)
    data = rq.get(url)
    with open('mvp_votes/team_records/{}team_records.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(data.text) """

import pandas as pd
from bs4 import BeautifulSoup

""" year= 1993
with open('mvp_votes/team_records/{}team_records.html'.format(year), encoding='utf-8') as f:
    page = f.read()
soup = BeautifulSoup(page, 'html.parser')
for element in soup.find_all('tr', class_='thead'):
    element.decompose()
teams_record_table_East_1993 = soup.find(id="divs_standings_E")

teams_record_Eastern_Conference_1993 = pd.read_html(str(teams_record_table_East_1993))[0]
print(teams_record_Eastern_Conference_1993)
 """
dfs = []
years= range(1993,2024)
for year in years:
    with open('mvp_votes/team_records/{}team_records.html'.format(year), encoding= 'utf-8') as f:
        page = f.read()
    soup = BeautifulSoup(page, 'html.parser')
    for element in soup.find_all('tr', class_='thead'):
        element.decompose()
    teams_record = soup.find(id="divs_standings_E")
    teams_record_table_E = pd.read_html(str(teams_record))[0]
    teams_record_table_E['Year'] = year
    teams_record_table_E['Team'] = teams_record_table_E['Eastern Conference']
    del teams_record_table_E['Eastern Conference']
    dfs.append(teams_record_table_E)

# Let's parse the second division table as well
    soup = BeautifulSoup(page, 'html.parser')
    for element in soup.find_all('tr', class_='thead'):
        element.decompose()
    teams_record = soup.find(id="divs_standings_W")
    teams_record_table_W = pd.read_html(str(teams_record))[0]
    teams_record_table_W['Year'] = year
    teams_record_table_W['Team'] = teams_record_table_W['Western Conference']
    del teams_record_table_W['Western Conference']
    dfs.append(teams_record_table_W)

# print(dfs)
teams_record_table_def = pd.concat(dfs)
# print(teams_record_table_def)

teams_record_table_def.to_csv('mvp_votes/csv/team_records.csv')
