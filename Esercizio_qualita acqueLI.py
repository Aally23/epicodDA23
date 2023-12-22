import json

file = open("Qualita_acque_Livorno.json")
acque = json.load(file)

print(len(acque))

elemento = acque[0]
print(elemento)  # STAMPA UN DIZIONARIO

tutti_i_CAP = [] # TUTTI I CAP
for elemento in acque:
    CAP = elemento['CAP']
    tutti_i_CAP.append(CAP)
print(tutti_i_CAP)

print(set(tutti_i_CAP)) # PER RIMUOVERE I DUPLICATI

province = list() # TUTTE LE PROVINCE
for elemento in acque:
    PR = elemento['SIGLA_PROV']
    province.append(PR)
print(province)

etichette_Pisa = list() # ESTRARRE I LINK DAL CAMPO ETICHETTA PER IL TERRITORIO DI PISA
for elemento in acque:
    if elemento['SIGLA_PROV'] == 'PI':
        etichetta = elemento['ETICHETTA']
        etichette_Pisa.append(etichetta)
print(etichette_Pisa)

numero_analisi_PI = []  # QUANTE SONO LE ANALISI DELLE ACQUE NEL TERRITORIO DI PISA RISPETTO A QUELLE TOTALI?
for elemento in acque:
    if elemento['SIGLA_PROV'] == 'PI':
        numero_analisi_PI.append(elemento)
print(len(numero_analisi_PI))

nr_pi = len(numero_analisi_PI)  # potevo ache usare len(etichette_Pisa)
nr_tot = (len(acque))

print(f'Il numero delle analisi delle acque nel territorio di Pisa è {nr_pi} su {nr_tot}')


file_2 = open('etichette_acque.csv', 'w') # Creiamo file .csv 
file_2.write('COD_ACQ,CAP,ETICHETTA\n') # Scriviamo l'intestazione
for elemento in acque:
    file_2.write(elemento['COD_ACQ'] + ',')
    file_2.write(elemento['CAP'] + ',')
    file_2.write(elemento['ETICHETTA'] + '\n')
file_2.close()

print(file_2)




def massimo(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max

a = int(input('Inserisci un numero:'))
b = int(input('Inserisci un numero:'))
c = int(input('Inserisci un numero:'))

print('Il massimo è: ', massimo(a, b, c))
