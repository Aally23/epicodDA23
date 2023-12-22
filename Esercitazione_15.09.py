""" nome_scuola = 'Epicode'
for i in nome_scuola:
    print(i)
 """
""" 
elementi = 'NPKOHC'
for i in elementi:
    print('elemento-', i)

 """
""" 
elementi = 'NPKOHC'
x = 0
for i in elementi:
    print('elemento - numero', x, ":", i)
    x += 1
 """
""" 
parola = 'mermelade'
nuova_parola = ''
for x in parola:
    if x == 'a':
        nuova_parola += 'e'
    elif x == 'e':
        nuova_parola += 'a'
    else:
        nuova_parola += x

print(nuova_parola)
 """
""" 
old_string = "Marmalade"
new_string = 'Mermeleda'
stringa_risultante = old_string.replace(old_string,new_string)
print(stringa_risultante) """


""" 
pot_due = []
for i in range(1,11):
    pot_due.append(2**i) 
print(pot_due)
 """

# in B ci sia 5 e a ci sia 7 serve terza variabile c
""" 
a = 5
b = 7
c = 0

c = a
a = b
b = c
print(a, b)

 """
""" 
N = int(input('Scrivi nun numero: '))
i = 0
pot_due = []
while i < (N + 1):
    pot_due.append(2**i)
    i += 1
print(pot_due)

 """


N = int(input('Scrivi nun numero: '))
pot_due = []

for i in range(1, N + 1):
    pot_due.append(2**i)
print(pot_due)





