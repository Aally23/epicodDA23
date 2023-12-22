# prezzi = ['100 £', '200 £']
# prezzi_con_dollari = [prezzo.replace('£', '$') for prezzo in prezzi]
# print(prezzi_con_dollari)

# studenti = ['Alex', 'Gino', 'Pippo', 'Giovanni', 'Alice', 'Marta', 'Anna', 'Alex', 'Federica', 'Gigi']
# lunghezza = len(studenti)
# print(lunghezza/2)
# prima_squadra = studenti[0:int(lunghezza/2)]
# seconda_squadra = studenti[int(lunghezza/2):lunghezza]

# print(prima_squadra)
# print(seconda_squadra)


# guadagni= [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

# for i in range(len(guadagni)):
#     guadagno_mese_corrente = guadagni[i]
#     media_guadagni_precedenti = round(sum(guadagni[:i]) / max(i, 1), 2)  
#     if i == 0:
#         guadagno_mese_corrente = guadagni[i]
#         print(f"Mese {i + 1}: Guadagno = {guadagno_mese_corrente}")
#     else:
#             if guadagno_mese_corrente > media_guadagni_precedenti:
#                 print(f"Mese {i + 1}: Guadagno = {guadagno_mese_corrente} è maggiore della Media Guadagni Precedenti = {media_guadagni_precedenti}")
#             elif guadagno_mese_corrente < media_guadagni_precedenti:
#                 print(f"Mese {i + 1}: Guadagno = {guadagno_mese_corrente} è minore della Media Guadagni Precedenti = {media_guadagni_precedenti}")
#             else:
#                  print(f"Mese {i + 1}: Guadagno = {guadagno_mese_corrente} è uguale alla Media Guadagni Precedenti = {media_guadagni_precedenti}")



# def Trova_max(lista_num):
#     massimo = lista_num[0]
#     for numero in lista_num:
#           if numero > massimo:
#                massimo = numero
#     return massimo  

# lista_num = [10, 20, 30, 40, 50, 45, 34, 23, 12, 19]
# massimo = Trova_max(lista_num)
# print(massimo)


# # lista_num = lista_num = [10, 20, 30, 40, 50, 45, 34, 23, 12, 19]
# # massimo = lista_num[0]
# # for num in lista_num:
# #     if num > massimo:
# #          massimo = num
# # print(massimo)

# def Trova_minimo(lista_num):
#     minimo = lista_num[0]
#     for num in lista_num:
#          if num < minimo:
#               minimo = num
#     return minimo

# num_minimo = Trova_minimo(lista_num)
# print(num_minimo)

# min_max = (f'Il massimo è {massimo} e il minimo è {num_minimo}')
# print(min_max)

# def Due_maggiori(lista_num):
#      massimo_1 = lista_num[0]
#      massimo_2 = lista_num [1]
#      if massimo_2 > massimo_1:
#         massimo_1, massimo_2 = massimo_2, massimo_1
#      for numero in lista_num[2:]:
#             if numero > massimo_1:
#                 massimo_1 = numero
#                 massimo_2 = massimo_1
#             elif numero > massimo_2:
#                  massimo_2 = numero
#      return massimo_1, massimo_2

# due_massimi = Due_maggiori(lista_num)
# print(due_massimi)


# def Due_maggiori(lista_num):
#     massimo_1 = lista_num[0]
#     massimo_2 = lista_num[1]
#     if massimo_2 > massimo_1:
#         massimo_1, massimo_2 = massimo_2, massimo_1
#     for numero in lista_num[2:]:
#         if numero > massimo_1:
#             massimo_2 = massimo_1
#             massimo_1 = numero
#         elif numero > massimo_2:
#             massimo_2 = numero
#     return massimo_1, massimo_2

# lista_num = [10, 20, 30, 40, 50, 45, 34, 23, 12, 19]
# due_massimi = Due_maggiori(lista_num)
# print(due_massimi)






# def conta_caratteri(testo):
#     Inizializziamo un dizionario vuoto per contenere i conteggi dei caratteri
#     conteggi = {}

#     Scorrere il testo carattere per carattere
#     for carattere in testo:
#         Verificare se il carattere è già nel dizionario dei conteggi
#         if carattere in conteggi:
#             Se è presente, incrementare il conteggio
#             conteggi[carattere] += 1
#         else:
#             Se non è presente, aggiungere il carattere al dizionario con un conteggio di 1
#             conteggi[carattere] = 1

#     return conteggi

# Test della funzione con il testo fornito
# testo = "La mia anima è pervasa da una mirabile serenità, simile a queste belle mattinate di maggio che io godo con tutto il cuore. Sono solo e mi rallegro di vivere in questo luogo che sembra esser creato per anime simili alla mia."
# risultato = conta_caratteri(testo)

# Stampare il risultato
# print(risultato)



studenti = ['Alex', 'Gino', 'Pippo', 'Giovanni', 'Alice', 'Marta', 'Anna', 'Alex', 'Federica', 'Gigi']
lunghezza = len(studenti)

prima_squadra = list()
seconda_squadra = list()
i = 0
for studenti[i] in studenti:
    if i % 2 == 0:
        prima_squadra.append(studenti[i])
    else: seconda_squadra.append(studenti[i])
    i += 1
print(prima_squadra)
print(seconda_squadra)




def Aster(numeri):
    for numero in numeri:
        print('*'*numero)


numeri = [5, 2, 3, 4]
print(Aster(numeri))