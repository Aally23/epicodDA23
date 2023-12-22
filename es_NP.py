""" nome_scuola = 'Epicode'
for lettera in nome_scuola:
    print(lettera)

    
lista = []
x = 0
while x < 21:
    lista.append(x)
    x += 1
print(lista)
 """


""" lista = []
pot_due = 0
while pot_due < 11:
    lista.append(2**pot_due)
    pot_due += 1
print(lista)
 """


""" lista = []
domanda = input('Inserici un numero: ')
pot_due = 0
N = int(domanda)
while pot_due < N:
    lista.append(2**pot_due)
    pot_due += 1
print(lista)
print(len(lista))
 """


""" 
studenti = ['ALex', 'Bob', 'Cindy', 'Dan', 'Emma']
corsi = ['Cybersecurity', 'Data Analyst', 'Backend', 'Frontend', 'Boh', 'Gino']
if len(studenti) == len(corsi):
    print('Le due liste hanno la stessa lunghezza')
else:
    print("C'è un errore")
 """
""" 
domanda = input('Scrivi una parola a caso: ')
if len(domanda) >= 6:
    print(domanda[0:3] + '...' + domanda[-3:])
elif len(domanda) >= 4:
    print(domanda[0:2] + '...' + domanda[-2:])
else:
    print("Errore fatale!!!")
 """
""" 
numero = int(input('Inserisci un numro intero: '))
fattori = []
for i in range(1, numero + 1):
    if numero % i == 0:
        fattori.append(i)
print(f'I fattori di {numero} sono: ')
for fattore in fattori:
    print(fattore)
 """
""" 
N = 5
p, n, z = 0, 0, 0
d1 = int(input('Inserisci un numero: '))
d2 = int(input('Inserisci un numero: '))
for i in range(N):
    if d1 > 0 and d2 > 0 or d1 < 0 and d2 < 0:
        p += 1
    elif d1 == 0 or d2 == 0:
        z += 1
    else:
        n += 1
print('Coppie positive:', p, 'Coppie negative:', n, 'Coppie nulle:', z)
 """
""" 
N = 5
p, n, z = 0, 0, 0

for i in range(N):
    d1 = int(input('Inserisci un numero: '))
    d2 = int(input('Inserisci un altro numero: '))

    if (d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0):
        p += 1
    elif d1 == 0 or d2 == 0:
        z += 1
    else:
        n += 1

print('Coppie positive:', p, 'Coppie negative:', n, 'Coppie nulle:', z)
 """

nome_scuola = 'Epicode'
esempio = ""
for parola in nome_scuola:
    esempio = (esempio + parola + '-')
print(esempio)
    
    



