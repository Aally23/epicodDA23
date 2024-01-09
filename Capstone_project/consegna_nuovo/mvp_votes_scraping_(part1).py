import requests
import pandas as pd
from bs4 import BeautifulSoup

# https://www.basketball-reference.com/ - Sorgente dati
# Web scraping from https://www.basketball-reference.com/awards/awards_{}.html

# Definisco gli anni
years = range(1993,2024)

# Download pagine html contenti i dati per tutti gli anni
url_start ='https://www.basketball-reference.com/awards/awards_{}.html'
for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open('mvp_votes/{}.html'.format(year), 'w', encoding='utf-8') as f:
        f.write(data.text)

# PARSING dei dati

with open('mvp_votes/1993.html', encoding='utf-8') as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')
soup.find('tr', class_='over_header').decompose()

# Seleziono la tabella che mi interessa tramite ispeziona pagina web
mvp_table = soup.find(id='mvp')

# Provo ad estrarre dati per il primo anno
mvp_1993 = pd.read_html(str(mvp_table))
mvp_1993 = pd.read_html(str(mvp_table))[0] 

# Itero per tutti gli anni 
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


# Creo un unico Dataset
mvps = pd.concat(dfs)

# Scrivo i risultati su un csv
mvps.to_csv('mvp_votes/mvps.csv')

# Ora abbiamo tutti i dati dei giocatori che hanno vinto l'MVP, ma non è sufficiente! Abbiamo bisogno delle statistiche di tutti i giocatori se vogliamo prevedere la stagione...
