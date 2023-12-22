import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

stats = pd.read_csv('mvp_votes/csv/players_mvps_stats.csv')
del stats['Unnamed: 0']
null= pd.isnull(stats).sum()
# print(null)

# Ci sono alcuni valori nulli nel %. Nessun tentativo?
three_point_perc_check = stats[pd.isnull(stats['3P%'])][['Player', '3PA']] # Tutte le righe in stat dove 3P% è nullo. Null value = Nessun tentativo
stats= stats.fillna(0)

# Utilizzeremo tutte le colonne numeriche per fare le nostre previsioni.
predictors = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year', 
       'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
# Vogliamo prevedere MVP Share, per questo abbiamo rimosso tutte le variabili che sono direttamente correlate con Share


training = stats[stats['Year'] < 2021] # Tutti i dati degli mvp/giocatori prima del 2021
test = stats[stats['Year'] == 2021] # Test year 2021

reg = Ridge(alpha=.1) 
reg.fit(training[predictors], training['Share']) # Adattiamo il modello prima a tutte le colonne di predittori presenti nel ds di addestramento
predictions = reg.predict(test[predictors]) # Prendiamo tutte le colonne del ds di addestramento e facciamo previsioni basate su di esse
predictions = pd.DataFrame(predictions, columns=['predictions'], index=test.index)

# Possiamo confrontare i valori reali con le nostre previsioni.
combination = pd.concat([test[['Player', 'Share']], predictions], axis=1) # We're combining the test Player and Shares columns and the predictions. On axis=1 it means we will combine the columns
print(combination)
print(combination.sort_values('Share', ascending=False).head(10)) # Ordianimao mettendo per primo chi ha vinto l'mvp
# Jokic ha vinto l'mvp ma non ha i predictors più alti di Antetokounmpo. 
# Come valutare se questo algoritmo ha fatto un buon lavoro? Dobbiamo introdurre una metrica di errore

# Proviamo una metrica di errore predefinita da sklearn
mse = mean_squared_error(combination['Share'], combination['predictions'])  # Prende i valori effettivi e i valori previsti e produce una metrica dell'errore basata su di essi
print(mse) # 0.002668239849159427 è la differenza media tra le previsioni e i valori reali. Ma non è molto significativo per noi, perché molti valori reali sono pari a 0.
print(combination['Share'].value_counts()) # 525 = 0
# Inoltre ci interessano solo i top player. Abbiamo bisogno di una nuova metrica di errore che tenga conto del ranking del giocatore

# Dobbiamo assegnare un rank ai giocatori
combination = combination.sort_values('Share', ascending=False)
combination['Rk'] = list(range(1, combination.shape[0] +1))  # Abbiamo una classifica in ordine di voto degli mvp

# Dobbiamo determinare i ranking delle nostre previsioni
combination = combination.sort_values('predictions', ascending=False)
combination['Predicted_Rk'] = list(range(1, combination.shape[0] +1))
print(combination.head(10)) # Possiamo vedere la differenza tra Rk e Predicted_rk. Ci sono alcuni valori anomali

# Nuova metrica di errore: quante delle prime cinque persone nella corsa agli mvp abbiamo collocato correttamente nella top 5?
# average_precision is the one we will use. Not so used because it deal swith rank, but it's our specific case!

print(combination.sort_values('Share', ascending=False).head(10))

# Abbiamo il giocatore che dovrebbe essere nella top 5 nella top 5?
# Se sì, otteniamo un punteggio perfetto, altrimenti penalizzazione in base a quanto lontano è stato pronosticato quel giocatore.

def find_ap(combination):
    actual = combination.sort_values('Share', ascending=False).head(5)
    predicted = combination.sort_values('predictions', ascending=False)
    ps = []
    found = 0
    seen = 1
    for index, row in predicted.iterrows():
       if row['Player'] in actual['Player'].values:
            found +=1
            ps.append(found/seen)
       seen +=1
    return (ps)

print(find_ap(combination)) # [1.0, 1.0, 1.0, 0.6666666666666666, 0.15151515151515152]. Punteggio perfetto per i primi tre, ma abbiamo (Curry 4/6), (Paul 5/33).


def find_ap_2(combination):
    actual = combination.sort_values('Share', ascending=False).head(5)
    predicted = combination.sort_values('predictions', ascending=False)
    ps = []
    found = 0
    seen = 1
    for index, row in predicted.iterrows():
       if row['Player'] in actual['Player'].values:
            found +=1
            ps.append(found/seen)
       seen +=1
    return sum(ps) / len(ps)

print(find_ap_2(combination)) # Questa è la nostra metrica di errore 0,7636363636363636. Più si abbassa, più tempo ci vuole per trovare l'mvp. Questo numero deve essere il più alto possibile


# BACKTESTING 
# Se guardiamo agli errori di un singolo anno, quel campione potrebbe non essere significativo e anche se l'algoritmo sembra buono non significa che lo sia. Più anni riusciamo a testare l'algoritmo, più fiducia possiamo avere che non vada in overfit e che funzioni correttamente.

years = list(range(1993, 2024))

def add_ranks(combination):
       combination = combination.sort_values('Share', ascending=False)
       combination['Rk'] = list(range(1, combination.shape[0] +1)) 
       combination = combination.sort_values('predictions', ascending=False)
       combination['Predicted_Rk'] = list(range(1, combination.shape[0] +1))
       combination['Diff'] = combination['Rk'] - combination['Predicted_Rk'] # Ci fa vedere la maggiore differenza tra il rango effettivo e quello previsto
       return combination


def backtest(stats, model, year, predictors):
       aps = []
       all_predictions = []
       for year in years[5:]: # Partiamo dal quinto anno perché abbiamo bisogno di alcuni dati storici per fare delle previsioni (assumiamo almeno 5 anni)
              training = stats[stats['Year'] < year]
              test = stats[stats['Year'] == year] # Partiamo dal 1998 e diciamo che tutti i dati dal 1993 al 1998 inclusi sono il nostro dataset di "allenamento". Il 1998 è l'anno su cui stiamo facendo previsioni
              model.fit(training[predictors], training['Share'])
              predictions = reg.predict(test[predictors])
              predictions = pd.DataFrame(predictions, columns=['predictions'], index=test.index)
              combination = pd.concat([test[['Player', 'Share']], predictions], axis=1)
              combination = add_ranks(combination)
              all_predictions.append(combination) # Lista che contiene previsioni per ogni singolo anno
              aps.append(find_ap_2(combination)) # Lista che contiene i punteggi medi di precisione
       return sum(aps)/len(aps), aps, pd.concat(all_predictions)

mean_ap, aps, all_predictions = backtest(stats, reg, years[5:], predictors)
print(mean_ap) # 0.7356320654877144. L'algoritmo sembra un po' meno preciso quando si analizzano tutti i dati, ma è comunque sufficientemente preciso


ranking = add_ranks(all_predictions[1:2]) # Predictions from 1999 season 
# print(ranking[ranking['Rk'] < 6 ].sort_values('Diff', ascending=False)) # It gives me the top 5 MVP vote getters along with their predicted rank and difference. This is helpfull for diagnostic, we will use it later

# DIAGNOSTIC

ten_biggest = all_predictions[all_predictions['Rk'] < 6 ].sort_values('Diff').head(10) # Guardiamo tutte le previsioni per a chiunque si sia classificato nei primi 5 posti e guardiamo le dieci differenze più grandi
print(ten_biggest)

print(reg.coef_) # Ci dice quali sono le variabili più importanti per l'algoritmo. Il coefficiente più alto indica le variabili più significative per la regressione 

# Non è molto utile poiché non abbiamo i nomi delle variabili
conc= pd.concat([pd.Series(reg.coef_), pd.Series(predictors)], axis=1)
print(conc.sort_values(0, ascending=False))
