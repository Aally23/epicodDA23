import pandas as pd
file = pd.read_csv('owid-covid-data.csv', sep=',')

# Verifica dimensioni del file
dimensione = file.shape  
print('La dimensione del file é:\n',  dimensione)

# Verifica diciture presenti nell'intestazione
colonne = file.columns
print('Le intestazioni del file sono:\n', colonne)

# Verifica dei continenti
unique_countries = file['continent'].unique()
print('I continenti presenti nel file sono:\n', unique_countries)

# Ricerca dei casi totali avvenuti nel signolo continente
file_filtrato = file[file['continent'] != 'nan'] # Filtro nel DF solo i dati pr cui è presente un valore diverso da nan nella colonna 'continent' 
casi_per_continente = file_filtrato.groupby('continent')['total_cases'].sum().reset_index() # Sommo i valori della colonna 'total_cases' raggruppandoli per 'continent' e trasformo la serie in un DF
casi_ordinati = casi_per_continente.sort_values('total_cases', ascending=False) # Ordino i dati in ordine decrescente
print(' I casi totali per singolo continente possono essere riassunti nella seguente tabella:\n',  casi_ordinati)

# Funzione per confronto n° casi totali nel mondo
def confronta_continenti_casi_tot(file, continente_1, continente_2):
    casi_totali_nel_mondo = file['total_cases'].sum()

    file_continente_1 = file[file['continent'] == continente_1]
    file_continente_2 = file[file['continent'] == continente_2]

    min_1 = file_continente_1['total_cases'].min()
    max_1 = file_continente_1['total_cases'].max()
    media_1 = file_continente_1['total_cases'].mean()
    perc_1 = (file_continente_1['total_cases'].sum() / casi_totali_nel_mondo) * 100

    min_2 = file_continente_2['total_cases'].min()
    max_2 = file_continente_2['total_cases'].max()
    media_2 = file_continente_2['total_cases'].mean()
    perc_2 = (file_continente_2['total_cases'].sum() / casi_totali_nel_mondo) * 100

    risultati = {
        continente_1: {
            'min_casi': min_1,
            'max_casi': max_1,
            'media_casi': media_1,
            '%_su_tot': perc_1
    },
        continente_2: {
            'min_casi': min_2,
            'max_casi': max_2,
            'media_casi': media_2,
            '%_su_tot': perc_2
    }
}

    return risultati


risultato = confronta_continenti_casi_tot(file, 'North America', 'South America')
df = pd.DataFrame(risultato)
print('Di seguito una tabella che ci dà qualche informazione  sui casi per singolo continente:\n', df)

# Funzione per confronto n° vaccinazioni totali nel mondo
def confronto_continenti_vaccinazioni(file, continente_1, continente_2):
    continente_1_data = file[file['continent'] == continente_1]
    continente_2_data = file[file['continent'] == continente_2]
    vaccinazioni_totali_mondo = file['total_vaccinations'].sum()

    min_c1 = continente_1_data['total_vaccinations'].min()
    max_c1 = continente_1_data['total_vaccinations'].max()
    media_c1 = continente_1_data['total_vaccinations'].mean()
    perc_su_tot_mondo_c1 = (continente_1_data['total_vaccinations'].sum() / vaccinazioni_totali_mondo) * 100

    min_c2 = continente_2_data['total_vaccinations'].min()
    max_c2 = continente_2_data['total_vaccinations'].max()
    media_c2 = continente_2_data['total_vaccinations'].mean()
    perc_su_tot_mondo_c2 = (continente_2_data['total_vaccinations'].sum() / vaccinazioni_totali_mondo) * 100

    risultati = {
        continente_1: {
            'min_vacc': min_c1,
            'max_vacc': max_c1,
            'media_vacc': media_c1,
            'percentuale_su_vacc_totali': perc_su_tot_mondo_c1
    },
        continente_2: {
            'min_vacc': min_c2,
            'max_vacc': max_c2,
            'media_vacc': media_c2,
            'percentuale_su_vacc_totali': perc_su_tot_mondo_c2
        }
}

    return risultati

confronto_continenti_vacc = confronto_continenti_vaccinazioni(file, 'Asia', 'Europe')
df = pd.DataFrame(confronto_continenti_vacc)
print('Di seguito una tabella che ci dà qualche informazione sulle vaccinazioni per singolo continente:\n', df)

# Per rispondere all'ultimo quesito ridefinisco le funzioni per confrontare in un singolo df i dati relativi ai 3 continenti:
def confronta_continenti_casi_tot_bis(file, *continenti):
    casi_totali_mondo = file['total_cases'].sum()
    risultati = {}
    
    for continente in continenti:
        
        continente_data = file[file['continent'] == continente]
        min_continente = continente_data['total_cases'].min()
        max_continente = continente_data['total_cases'].max()
        media_continente = continente_data['total_cases'].mean()
        perc_continente = (continente_data['total_cases'].sum() / casi_totali_mondo) * 100
        
        risultati[continente] =  {
            'min_casi': min_continente,
            'max_casi': max_continente,
            'media_casi': media_continente, 
            'perc_casi_su_totale': perc_continente
        }
        
    return risultati

ris = confronta_continenti_casi_tot_bis(file,'South America', 'Europe', 'Oceania')
df = pd.DataFrame(ris)
print('Di seguito una tabella che ci dà qualche informazione sui casi confrontando South America, Europe e Oceania:\n', df)



def confronto_continenti_vaccinazioni_bis(file, *continenti):
    vacc_totali_mondo = file['total_vaccinations'].sum()
    risultati = {}
    
    for continente in continenti:
        
        continente_data = file[file['continent'] == continente]
        min_continente = continente_data['total_vaccinations'].min()
        max_continente = continente_data['total_vaccinations'].max()
        media_continente = continente_data['total_vaccinations'].mean()
        perc_continente = (continente_data['total_vaccinations'].sum() / vacc_totali_mondo) * 100
        
        risultati[continente] =  {
            'min_vacc': min_continente,
            'max_vacc': max_continente,
            'media_vacc': media_continente, 
            'perc_vacc_su_totale': perc_continente
        }
        
    return risultati

ris = confronto_continenti_vaccinazioni_bis(file,'South America', 'Europe', 'Oceania')
df = pd.DataFrame(ris)
print('Di seguito una tabella che ci dà qualche informazione sulle vaccinazioni confrontando South America, Europe e Oceania:\n', df)

# Sarebbe stato possibile operare in modo diverso? Senza "generare" una nuova funzione?

"""
Le statistiche relative a casi e vaccinazioni evidenziano notevoli differenze tra i 3 continenti:

- Per quanto riguarda i casi, l'Europa ha il massimo numero di casi, seguita da Sud America e Oceania; 
  Allo stesso tempo Europa ha una percentuale significativamente più alta rispetto agli altri due continenti rispetto al totale mondiale, mentre Sud America e Oceania hanno percentuali inferiori.

- Per quanto riguarda le vaccinazioni, Sud America mostra il massimo numero di vaccinazioni, seguito da Europa e Oceania (Sarebbe utile confrontare le popolazioni dei vari continenti); 
  In termini di percentuale sul totale mondiale però l'Europa ha la percentuale più alta, mentre Sud America ha una percentuale significativamente inferiore e Oceania la più bassa.

Questi dati indicano profonde differenze nella gestione della pandemia e nell'andamento dei casi e delle vaccinazioni tra questi tre continenti 

"""
