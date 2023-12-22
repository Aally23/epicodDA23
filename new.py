import pandas as pd
file = pd.read_csv('owid-covid-data.csv', sep=',')



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
print(df)