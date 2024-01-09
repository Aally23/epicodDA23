import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from bs4 import BeautifulSoup


service = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=service) as driver:
    player_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    years = range(1993,2024)


# Download pagine html contenti i dati per tutti gli anni con ChromeDriverManager

for year in years:
    url = player_stats_url.format(year)
    driver.get(url)
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)
    html = driver.page_source
    with open('mvp_votes/players/{}stats.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(html)


# Provo ad estrarre dati per il primo anno
year = 1993
with open('mvp_votes/players/{}stats.html'.format(year), encoding='utf-8') as f:
    page = f.read()
soup = BeautifulSoup(page, 'html.parser')
soup.find('tr', class_='thead').decompose()
player_table = soup.find(id='div_per_game_stats')
player = pd.read_html(str(player_table))[0]
player['Year'] = year
print(player.tail())

# Itero per tutti gli anni 
dfs = []
years = range(1993,2024)
for year in years:
    with open('mvp_votes/players/{}stats.html'.format(year), encoding='utf-8') as f:
        page = f.read()
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find(id='div_per_game_stats')
    player = pd.read_html(str(player_table))[0]
    player['Year'] = year
    dfs.append(player)

# Creo un unico Dataset
player_stats = pd.concat(dfs)

# Scrivo i risultati su un csv
player_stats.to_csv('mvp_votes/players/player_stats.csv')

