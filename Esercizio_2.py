""" var_1 = 'Epicode'
print(var_1)

nome_scuola = 'Epicode'
print(nome_scuola[0])

nome_scuola = 'Epicode'
print(nome_scuola[2])

nome_scuola = 'Epicode'
print(nome_scuola.upper())

x = 10
print((x + 2)*3)
x_2 = x + 2
print(3*x_2)

Q_1 = input('Quanti litri di benzina ci sono nel serbatoio?')
Q_2 = input('''Qual è l'efficienza espressa in km/l?''')
Q_3 = input('Qual è il prezzo della benzina per litro?')
print(Q_1,Q_2,Q_3)
costo_per_100km = float(Q_3)*100
print(costo_per_100km)

domanda = input('Come ti chiami?')
y = (domanda[:3] +'...'+ domanda[-3:])
print(y) 


lista = ['Epicode', 'Windows', 'Excel', 'Powerpoint', 'Word']
for parola in lista:
    if 5 <= len(parola) <= 8:
        print (f"{parola} ha lunghezza tra 5 e 8 caratteri")
    else:
        print(f"{parola} NON ha lunghezza tra 5 e 8 caratteri")
 """

""" codici = ['knt-s1', 'cba-G9', 'qtr-z8']
for codice in codici:
    last_3 = codice[-3:]
    print (last_3)
 """
 
""" codici = ['knt-s1', 'cba-G9', 'qtr-z8']
l3_1 = codici[0]
l3_2 = codici[1]
l3_3 = codici[2]
print(l3_1[-3:], l3_2[-3:], l3_3[-3:]) """
""" 
codici = ['knt-s1', 'cba-G9', 'qtr-z8']
last_tre = []
for codice in codici:
    last_3 = codice[-3:]
    last_tre.append(last_3)
    print(last_tre)
 """

codici = ['knt-s1', 'cba-G9', 'qtr-z8']
ultimi_3_caratteri_lista = []

for codice in codici:
    ultimi_3 = codice[-3:]
    print(type(ultimi_3))
    ultimi_3_caratteri_lista.append(ultimi_3)

print(ultimi_3_caratteri_lista)
