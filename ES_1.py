# Abbiamo 25 studenti; memorizzare dato in una variabile #


""" 
studenti = 25
print("studenti la prima volta", studenti)
print("studenti la prima volta vale " + str(studenti) + " poi lo modifico")

studenti = 10
print("studenti la seconda volta", studenti)
print("studenti la seconda volta vale " + str(studenti) + " fine")
"""


# Abbiamo 25 studenti; memorizzare dato in una variabile + stampa a video #

""" 
studenti = 25
print(studenti)
"""

# Abbiamo 25 studenti; memorizzare dato in una variabile, arrivano altri 3 studenti, memorizzare + terza variabile somma delle altre due #
""" 
studenti = 25
altri_studenti = 3

studenti_new = (studenti + altri_studenti)
print(studenti_new) 
"""

# Creare a mano una lista che contenga i numeri da 0 a 5
# memorizzarla in una variabile a video
""" 
lista_numeri = [0, 1, 2, 3, 4, 5]
print("La lista è questa: ", lista_numeri)

lista_numeri = range(0,5)
print("La lista è questa: ", list(lista_numeri))

lista_numeri = range(0,6)
print("La lista è questa: ", list(lista_numeri))


lista_film = ["Il signore degli anelli", "Kill Bill", "The nightmare before Christmas"]
print(lista_film) """
""" 
numero_1 = input("Inserisci un numero: ")
numero_2 = input("Inserisci un numero: ")
numero_3 = input("Inserisci un numero: ")

if numero_1 > numero_2 and numero_1 > numero_3:
    print(numero_1)

elif numero_2 > numero_1 and numero_2 > numero_3:
    print(numero_3)

elif numero_3 > numero_1 and numero_3 > numero_2: 
    print(numero_3)
else:
    print("Non c'è un numero maggiore degli altri")
 """
# Scrivi un programma che chieda all'utente una lista di numeri e fornisca in output il maggiore tra tutti.
""" 
lista_numeri = [50, 56, 75, 86, 12, 34]
numero_maggiore = lista_numeri[0]
for numero in lista_numeri:
    if numero > numero_maggiore:
        numero_maggiore = numero
print("é il num maggiore")
 """
1
input_numeri = input("Inserisci una lista di numeri separati da virgole: ")
lista_numeri = [int(numero) for numero in (input_numeri.split(','))]1,23,45,67

print("Lista di numeri inseriti:", lista_numeri)
