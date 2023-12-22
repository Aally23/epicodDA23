import pandas as pd
file = pd.read_csv('owid-covid-data.csv', sep=',')
def confronta_continenti(file, continente_1, continente_2):
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
        continente_1: min_1,
        continente_2: {
            'min_casi': min_2,
            'max_casi': max_2,
            'media_casi': media_2,
            '%_su_tot': perc_2
    }
    }

    return risultati


risultato = confronta_continenti(file, 'North America', 'South America')
risultato = pd.DataFrame(risultato)
print(risultato)