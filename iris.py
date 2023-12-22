# import pandas as pd
# file = pd.read_csv('iris.csv')
# # dim = file.shape
# # print(dim)
# # print(dim[0])
# # print(dim[1])

# # print(file.head())
# # print(file.tail())

# righe = file.index
# colonne = file.columns
# valori = file.values

# # print(righe)
# # print(colonne)
# # print(valori)
# # print(len(valori))

# # riepilogo= file.describe()
# # riepilogo.to_csv('iris_descrizione.csv')

# colonne = file.columns
# print(colonne)

# loc = file.loc[49, 'variety']
# print(loc)



import pandas as pd
file = pd.read_csv("C:/Users/aless/Downloads/Mappa-degli-autovelox-in-italia.csv", sep=';')
dimensione = file.shape
print(dimensione)

colonna = file.columns
print(colonna)


filtro = file.Comune == 'COLLEGNO'

# print(filtro)

selezione = file.loc[filtro, ['Provincia', 'Regione', 'Anno inserimento']]
print(selezione)
