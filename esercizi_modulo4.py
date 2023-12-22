""" #Es 1
nome_scuola = 'Epicode'
for i in nome_scuola:
    print(i)
 """
"""  
#Es 2
elementi = 'NPKOHC'
for i in elementi:
    print(i) """
""" 
#ES 3
elementi = 'NPKOHC'
for i in elementi:
    print("elemento-" + i)
 """
""" 
#ES 4
elementi = 'NPKOHC'
n = 1
for i in elementi:
    print ('elemento-numero ' + str(n))
    n += 1
 """
""" 
#ES 5 
#CICLO FOR
parola = 'marmalade'
nuova_parola = ''
for i in parola:
    if i == 'a':
        nuova_parola += 'e'
    elif i == 'e':
        nuova_parola += 'a'
    else:
        nuova_parola += i
print(nuova_parola)
 """

""" #CICLO WHILE
parola = 'marmalade'
nuova_parola = ''
indice = 0
while indice < len(parola):
    if parola[indice] == 'a':
        nuova_parola += 'e'
    elif parola[indice] == 'e':
        nuova_parola += 'a'
    else:
        nuova_parola += parola[indice]        
    indice += 1
print(nuova_parola)
 """

""" #CON .replace
parola = "marmalade"
parola_modificata = parola.replace('a', 'X').replace('e', 'a').replace('X', 'e')
print(parola_modificata)
 """
""" 
pot_2 = ''
for i in range(1, 11):
    pot_2 = (2**i)
    print(pot_2)
 """
""" 
#ES 6
N = int(input('Inserisci un numero: '))
pot_due = []
for i in range(1, N + 1):
    pot_due.append(2**i)
print(pot_due)

N = int(input('Inserisci un numero: '))
pot_due = []
contatore = 1
while contatore < N +1 :
    pot_due.append(2**contatore)
    contatore += 1
print(pot_due)
 """
""" 
n = 2500
pot_due = []
contatore = 1
while contatore < n +1:
    pot_due.append(2**contatore)
    contatore += 1
print(pot_due) """

""" pot_due = []
n = 100
for i in range(100):
    if i % 3 == 0:
        pot_due.append(2**i)
    else:
        pass
print(pot_due)         
 """

""" 
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
massimo = numeri[0]
for numero in numeri:
    if numero > massimo:
        massimo = numero
print(massimo)

numeri = [4, 9, 5, 1, 7, 10, 2, 3]
somma = 0
for numero in numeri:
    somma += numero
lung = len(numeri)
media = somma / lung
print(media)

 """

# eta_studenti = [20, 30, 40, 50, 60]
# somma = 0
# for eta in eta_studenti:
#     somma += eta
# media = somma/len(eta_studenti)
# print(media)

# studenti = ['Alex', 'Bob', 'Cindy', 'Dan','Emma']
# for studente in studenti:
#     print('-', studente)

# parole = ['Albergo', 'Sedia', 'Borgo', 'Petalo', 'Belvedere', 'Semestre', 'Sosta', 'Orpello', 'Abete']
# for parola in parole:
#     conteggio_e = parola.count('e')
#     print(f'Nella parola {parola} la lettera e è presente {conteggio_e} volte')

# parole = ['Elbergo', 'Sedia', 'Borgo', 'Petalo', 'Belvedere', 'Semestre', 'Sosta', 'Orpello', 'Abete']
# for parola in parole:
#     conteggio_e = parola.lower().count('e')
#     print(f'Nella parola {parola} la lettera e è presente {conteggio_e} volte')

# cf = ['LLZKKS82E25B036D', 'CXVPYF73S54G663G', 'DHVMVR62A22Z347L', 'TKLSLR98S58D615I']
# contatore = 0
# verifica = cf[contatore]
# carattere = '66'
# for i in cf:
#     if carattere in i:
#         print (i)
#     contatore += 1


# cf = ['LLZKKS82E25B036D', 'CXVPYF73S54G663G', 'DHVMVR62A22Z347L', 'TKLSLR98S58D615I']
# anno = '66'
# for i in cf:
#     if anno in i:
#         print(i)


# cf = ['LLZKKS82E25B036D', 'CXVPYF73S54G663G', 'DHVMVR62A22Z347L', 'TKLSLR98S58D615I']
# for i in cf:
#     print(i[0:3], i[3:6])

# cf = ['LLZKKS82E25B036D', 'CXVPYF73S54G663G', 'DHVMVR62A22Z347L', 'TKLSLR98S58D615I']
# for contatore, i in enumerate(cf):
#     print(contatore, i)


# studenti = ['Alex', 'Bob', 'Cindy', 'Dan']
# corsi = ['Cybersecurity', 'Data Analyst', 'Backend', 'Frontend']
# edizioni = [1, 2, 3, 1] 

# for i in range(len(studenti)):
#     if edizioni[i] == 1:
#         print (f'Lo studente {studenti[i]} frequenta la prima edizione del corso {corsi[i]}')

# diz_auto ={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107'}
# print(diz_auto)
# print(diz_auto['Debbie'])

# diz_auto['Emily'] = 'A1'
# diz_auto['Fred'] = 'Octavia'
# print(diz_auto)     

# del diz_auto['Ben']
# print(diz_auto)


diz_auto = {
    'Ada': 'Punto', 
    'Ben': 'Multipla', 
    'Charlie': 'Golf', 
    'Debbie': '107', 
    'Emily': 'A1'
    }
nuovi_proproetari = {
    'Ben': 'Polo', 
    'Fred': 'Octavia', 
    'Grace': 'Yaris', 
    'Hugh': 'Clio'
    }

diz_auto.update(nuovi_proproetari)
print(diz_auto)

print(diz_auto.get('Ada'))
print(diz_auto.get('Pippo', 'Non esiste nessuna corrispondenza'))

print(diz_auto.get('Ada'))
print(diz_auto.setdefault('Pippo', 'Non esiste nessuna corrispondenza'))
del diz_auto['Pippo']
for chiave, valore in diz_auto.items():
    print(f'Chiave:{chiave} Valore:{valore}')
    print ()

for valore in diz_auto.values():
    if valore != 'Multipla':
        print(valore)
