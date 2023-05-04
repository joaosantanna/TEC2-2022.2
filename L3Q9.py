from random import randint
import numpy as np
a = []

for i in range(9):
    a.append(randint(1,100))

a = np.array(a)
a.shape = (3,3)


print(f'a = \n {a}')
determinante = np.linalg.det(a)
print(f'Determinante da matriz a = {determinante:.2f}')

