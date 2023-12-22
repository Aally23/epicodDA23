# https://www.basketball-reference.com/ source of datas
# Web scraping from NBA Awards Voting pages
# pip install requests

# Define the years we want to scrape data for
years = range(1993,2024)

import requests
"""
url_start ='https://www.basketball-reference.com/awards/awards_{}.html'
for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open('mvp_votes/{}.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(data.text) """

# # - PARSING -
# Install pip beautifulsoup4

# Import parser class from beautifulsoup
from bs4 import BeautifulSoup

# 'page' is the html page  we've seen before but as a string
with open('mvp_votes/1993.html', encoding='utf-8') as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')

# get ride of some stuff with inspector --> we don't need overheader (voting/ per game/ shooting /advanced)
# Inspector --> we've found the specific class of the header: it's a 'tr' ( a table row) with the class 'over_header'. Let's remove it with decompose command
soup.find('tr', class_='over_header').decompose()

# Let's remove all the other stuff by only finding the specific table that we want. The table has an  id="mvp" --> global unique property
mvp_table = soup.find(id='mvp')

import pandas as pd
mvp_1993 = pd.read_html(str(mvp_table))

# This is not a DF but a list of DF. Transform it into  a single DF 
mvp_1993 = pd.read_html(str(mvp_table))[0] 
# print(mvp_1993)
# We have parsed the 1993 mmvp page for mvps and loaded it into Pandas!!!

# Let's do it for the other seasons
dfs = []
for year in years:
    with open('mvp_votes/{}.html'.format(year), encoding='utf-8') as f:
        page = f.read()
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='over_header').decompose()
    mvp_table = soup.find(id='mvp')
    mvp = pd.read_html(str(mvp_table))[0]
    mvp['Year'] = year

    dfs.append(mvp)
# print(dfs) # dfs is now a list of DataFrames, one for each year

# We want to work with just one single DataFrame
mvps = pd.concat(dfs)
# print(mvps)

# There's no way to tell which year datas came from. We need a column called 'Year'. mvp['Year'] = year - line 53 - 

# Store the Df into a csv format
mvps.to_csv('mvp_votes/mvps.csv')

# We now have all the data for players who won MVP, it's not enough! We need statistics of all the players. If we want to predict within the season... 

# - DOWNLOADING PLAYER STATS - 
# URL https://www.basketball-reference.com/leagues/NBA_2023_per_game.html

player_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

url = player_stats_url.format(1993)
data = requests.get(url)
with open('players/1993.html', 'w') as f:
    f.write(data.text)

