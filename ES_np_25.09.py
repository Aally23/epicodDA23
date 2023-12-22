# import numpy as np
# lista = [1, 2, 3, 4]
# array = np.array(lista)
# print(type(array))

# array = np.arange(0, 11, 2)
# print(array)

# array = np.zeros(5)
# print(array)

# array = np.linspace(0, 11, 10)
# print(array)


# array_1 = np.random.randint(0, 100, 10)
# print(array_1)

# array_2 = np.random.randint(0, 2, (3, 4))
# print(array_2)

# array_3 = np.arange(0, 100).reshape(10, 10)
# print(array_3)


# diz = {'a': 1, 'b': 2, 'c': 3}
# print('il valore di a è:', diz['a'])

# print('a' in diz)

# print(diz.items())
# print(diz.get('a'))

# magazzino = {
#     't-shirts': 10,
#     'cappotti': 8,
#     'sciarpe': 7
#     }

# print(magazzino['sciarpe'])
# print(magazzino.get('calze', 0))
# print(magazzino)

# magazzino.update({'t-shirts': 8, 'cappotti': 3})
# print(magazzino)

# print(magazzino.keys())
# print(magazzino.values())
# print(magazzino.items())


magazzino_2 = {
    't-shirts': [10, 7],
    'cappotti': 8,
    'sciarpe': 7
    }

print(magazzino_2)
print(magazzino_2.items())
print(magazzino_2.values())

for articolo, quantita in magazzino_2.items():
    print(f"Ci sono {quantita} pezzi di {articolo}")