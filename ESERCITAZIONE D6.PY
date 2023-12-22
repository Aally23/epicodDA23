# mat = [[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9],
#         [10, 11, 12, 13, 14]]

# # print(mat[1][2])

# import numpy as np
# mat = np.array(mat)
# # print(mat)

# print(mat[0][2])

# linear_data = np.array([x for x in range(27)])
# reshaped_data = linear_data.reshape(3, 3, 3)

# print(linear_data)
# print(reshaped_data)
# print(reshaped_data[0][1][2]) # Matrice/Riga/Colonna

# territorio_cittadino = np.array()

import numpy as np
import random
conteggi_store = np.zeros((2, 2), int)
print(conteggi_store)

numero_iterazioni = 100
for i in range(numero_iterazioni):
    quadrante_scelto = random.randint(0,2)
    clienti_serviti = random.randint(1, 100)
    conteggi_store[quadrante_scelto] += clienti_serviti
print(conteggi_store)