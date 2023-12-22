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


risultato = confronta_continenti(file, 'North America', 'South America')
df = pd.DataFrame(risultato)
# df = df.reset_index()
# df = df.rename(columns={'index': 'Descrittore'})
print(df)

# df.to_csv('confronto_continenti.csv')




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
# print(df)


# ordi =file.sort_values('date', ascending=False)
# print(ordi)

a = file.sort_values(by='date', ascending=False)
print(a.date)


# col = file.continent.unique()
# print(col)
