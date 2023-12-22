import pandas as pd
file = pd.read_csv('owid-covid-data.csv', sep=',')
# a = file[file['continent'].isna()]
# print(a)



# def confronta_continenti(file, continente_1, continente_2, continente_3, continente_4, continente_5, continente_6, continente_7):
#     casi_totali_nel_mondo = file['total_cases'].sum()

#     file_continente_1 = file[file['continent'] == continente_1]
#     file_continente_2 = file[file['continent'] == continente_2]
#     file_continente_3 = file[file['continent'] == continente_3]
#     file_continente_4 = file[file['continent'] == continente_4]
#     file_continente_5 = file[file['continent'] == continente_5]
#     file_continente_6 = file[file['continent'] == continente_6]
#     file_continente_7 = file[file['continent'] == continente_7]

#     perc_1 = (file_continente_1['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_2 = (file_continente_2['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_3 = (file_continente_3['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_4 = (file_continente_4['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_5 = (file_continente_5['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_6 = (file_continente_6['total_cases'].sum() / casi_totali_nel_mondo) * 100
#     perc_7 = (file_continente_7['total_cases'].sum() / casi_totali_nel_mondo) * 100

    
#     risultati = {
#         continente_1: {
#             '%_su_tot': perc_1
#     },
#         continente_2: {
#             '%_su_tot': perc_2
#     },
#     continente_3: {
#             '%_su_tot': perc_3
#     },
#     continente_4: {
#             '%_su_tot': perc_4
#     },
#     continente_5: {
#             '%_su_tot': perc_5
#     },
#     continente_6: {
#             '%_su_tot': perc_6
#     },
#     continente_7: {
#             '%_su_tot': perc_7
# }
#     }
#     return risultati


# risultato = confronta_continenti(file, 'North America', 'South America', 'Europe','Asia','Africa','Oceania', 'NaN')
# df = pd.DataFrame(risultato)
# # df = df.reset_index()
# # df = df.rename(columns={'index': 'Descrittore'})
# print(df)

# df.to_csv('confronto_continenti.csv')




# def confronto_continenti_vaccinazioni(file, *continenti):
#     vacc_totali_mondo = file['total_vaccinations'].sum()
#     risultati = {}
#     totale_altro = 0
#     for continente in continenti:
#         if continente == 'nan':
#             continente_data = file[file['continent'].isna()]
#         else:
#             continente_data = file[file['continente'] == continente]
#         perc = (continente_data['total_vaccinations'].sum() / vacc_totali_mondo) * 100
    
#         if continente == 'nan':
#             totale_altro += perc
#         else:
#             risultati[continente] =  {
#            'perc_vacc_su_totale': perc
#         }
    
#     risultati['Altro'] = {
#         'perc_vacc_su_totale': totale_altro
#     }
    
#     return risultati

# ris = confronto_continenti_vaccinazioni(file, 'North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania', 'nan')
# df = pd.DataFrame(ris)
# print(df)    
    
    
    
import pandas as pd

def confronto_continenti_vaccinazioni(file, *continenti):
    vacc_totali_mondo = file['total_vaccinations'].sum()
    risultati = {}
    totale_altro = 0
    for continente in continenti:
        if continente == 'nan':
            continente_data = file[file['continent'].isna()]
        else:
            continente_data = file[file['continent'] == continente]
        perc = (continente_data['total_vaccinations'].sum() / vacc_totali_mondo) * 100
    
        if continente == 'nan':
            totale_altro += perc
        else:
            risultati[continente] =  {
               'perc_vacc_su_totale': perc
            }
    
    risultati['Altro'] = {
        'perc_vacc_su_totale': totale_altro
    }
    
    return risultati

# Esempio di utilizzo
file = pd.read_csv('owid-covid-data.csv', sep=',')
ris = confronto_continenti_vaccinazioni(file, 'North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania', 'nan')
df = pd.DataFrame(ris)
print(df)

    
    
    
#     continente_1_data = file[file['continent'] == continente_1]
#     continente_2_data = file[file['continent'] == continente_2]
#     vaccinazioni_totali_mondo = file['total_vaccinations'].sum()

#     min_c1 = continente_1_data['total_vaccinations'].min()
#     max_c1 = continente_1_data['total_vaccinations'].max()
#     media_c1 = continente_1_data['total_vaccinations'].mean()
#     perc_su_tot_mondo_c1 = (continente_1_data['total_vaccinations'].sum() / vaccinazioni_totali_mondo) * 100

#     min_c2 = continente_2_data['total_vaccinations'].min()
#     max_c2 = continente_2_data['total_vaccinations'].max()
#     media_c2 = continente_2_data['total_vaccinations'].mean()
#     perc_su_tot_mondo_c2 = (continente_2_data['total_vaccinations'].sum() / vaccinazioni_totali_mondo) * 100

#     risultati = {
#         continente_1: {
#             'min_vacc': min_c1,
#             'max_vacc': max_c1,
#             'media_vacc': media_c1,
#             'percentuale_su_vacc_totali': perc_su_tot_mondo_c1
#     },
#         continente_2: {
#             'min_vacc': min_c2,
#             'max_vacc': max_c2,
#             'media_vacc': media_c2,
#             'percentuale_su_vacc_totali': perc_su_tot_mondo_c2
#         }
# }

#     return risultati


