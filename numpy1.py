import numpy as np
from random import randint

a = []
b = []
soma = []

for i in range(9):
    n1 = randint(1,10)
    a.append(n1)
    n2 = randint(1,10)
    b.append(n2)

a = np.array(a)
b = np.array(b)

a.shape = (3,3)
b.shape = (3,3)

print(f'matriz a \n {a}')
print(f'matriz b \n {b}')

soma = a + b
print(f'Soma de a + b = \n {soma}')