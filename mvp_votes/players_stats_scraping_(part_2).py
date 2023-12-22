import requests as rq
"""
player_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

url = player_stats_url.format(1993)
data = rq.get(url)
with open('mvp_votes/players/1993.html', 'w', encoding='utf-8') as f:
    f.write(data.text) """

# pip install selenium

# pip3 install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
# Install Webdriver
service = Service(ChromeDriverManager().install())



""" 
year = 1993
    url = player_stats_url.format(year)
    driver.get(url)
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)

    html = driver.page_source
    with open('mvp_votes/players/{}bis.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(html)
"""
import time
with webdriver.Chrome(service=service) as driver:
    player_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    years = range(1993,2024)

"""
for year in years:
    url = player_stats_url.format(year)
    driver.get(url)
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)
    html = driver.page_source
    with open('mvp_votes/players/{}stats.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(html)
 """

# Save the file immediately after a web scraping
from bs4 import BeautifulSoup
import pandas as pd

""" year = 1993 """

# 'page' is the html page we've seen before but as a string
""" with open('mvp_votes/players/{}stats.html'.format(year), encoding='utf-8') as f:
    page = f.read()

# Copy the previous scraping code
soup = BeautifulSoup(page, 'html.parser')
soup.find('tr', class_='thead').decompose()
player_table = soup.find(id='div_per_game_stats')
player = pd.read_html(str(player_table))[0]
player['Year'] = year
print(player.tail()) """

# Turn this into a loop
dfs = []
years = range(1993,2024)
for year in years:
    with open('mvp_votes/players/{}stats.html'.format(year), encoding='utf-8') as f:
        page = f.read()
# Copy the previous scraping code
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find(id='div_per_game_stats')
    player = pd.read_html(str(player_table))[0]
    player['Year'] = year
    dfs.append(player)
# print(dfs)

player_stats = pd.concat(dfs)
# print (player_stats)
player_stats.to_csv('mvp_votes/players/player_stats.csv')

