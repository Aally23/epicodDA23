file = open('Mappa-dei-pub-circoli-locali-in-Italia.csv', 'r', encoding = 'latin1')
# content = file.readlines()
# print(len(content))

# attributi = file.readlines()
# print(attributi)

# contenuto = file.read().splitlines()
# seconda_riga = contenuto[1]
# ultima_riga = contenuto[-1]
# print(seconda_riga)
# print(ultima_riga)

# import numpy as np
# content = file.readlines()[1:]


# num_casuale = np.random.randint(0, (len(content) -1))
# riga_a_caso = content[num_casuale]
# print(riga_a_caso)



# attributi = file.readline()
# print(attributi)
anni_presenti = set()
righe = file.readlines()[1:]
for riga in righe:
    colonne = riga.strip().split(';')
    anno = colonne[4]
    anni_presenti.add(anno)
print(anni_presenti)
