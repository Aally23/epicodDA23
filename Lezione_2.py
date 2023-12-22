""" lista = [10, 14, 23, 53, 34, 75]

# Da 0 fino al 2 escluso 
print(lista[0:2]) 

#  2 e 3 
print(lista[1:3])

# Tutti tranne 0 
print(lista[1:])

# Da 0 fino al 2 escluso
print(lista[:2])

# Ultimi due (-2 sta a indicare il penultimo) Con il - si parte al contrario
print(lista[-2:])

# Tutti tranne primo e ultimo
print(lista[1:-1])

print(lista[2:5])

print(lista[:-3])
 """
""" 
lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista.insert(2, 'nuovo')

# Cosi facendo lo mette nell'ultima riga
lista.insert(20, 'fuori elenco')
print(lista) 

# Per aggiungere un elenco di valori
lista = ['a', 'b', 'c', 'd', 'e', 'f']
aggiungi = ['g', 'h', 'i']
lista.extend(aggiungi)
print(lista)

# Remove indica sempre il valore
lista.remove('b')
print(lista)

# Rimuovi valore in posizione specifica
lista.remove(lista[0])
print(lista)
"""
""" lista_new = ['a', 'a', 'a', 'a', 'b', 'b', 'b']
while 'b' in lista_new:
    lista_new.remove('b')
print(lista_new)

print(lista_new.count('a'))

print(lista_new.index('a'))
 """
""" 
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1
print(lista1)
print(lista2)
lista2.append(100)
print(lista2)
print(lista1)

# Ha messo 100 anche in lista 1
# Non stiamo duplicando i valori ma stiamo dicendo che lista2 punta a quello che è definito in lista1. Si crea un collegamento tra le due liste 

lista1.append(999)
print(lista2)

lista3 = []
lista3.extend(lista2)
print(lista3)
lista2.append(1234)
print(lista3)
print(lista2)

if 3 in lista1:
    print("True")

"""
'''
stringa = 'abcdefghi'

# Punto di partenza: Punto di arrivo: Quanti elementi saltare
print(stringa[0:6:2])
print(stringa[::-1])
print(stringa[7:3:-1])

ita_str = """ Stringa con l'apostrofo e le "virgolette" """
print(ita_str)
print(len(ita_str))

ita_str = """ Stringa con l'apostrofo\n e le "virgolette" """
print(ita_str)
'''

codici = ['abc-12', 'def-34', 'ghi-56', 'lmn-78', 'opq-90']
n_1 = codici[0][-3:]
print(n_1)

# codici[1], codici[2]

#print(n_1[-3:], n_2[-3:], n_3[-3:])

# a,b,c = input("Scrivi tre numeri separati da virgola ").split(",")

