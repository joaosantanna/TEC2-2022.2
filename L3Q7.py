from random import randint
import numpy as np

a = []
b = []

for i in range(4):
    a.append(randint(1,100))
    b.append(randint(1,100))

a = np.array(a)
b = np.array(b)
a.shape = (2,2)
b.shape = (2,2)

print(f'a = \n {a}')
print(f'b = \n {b}')

c = a + b
print(f'c = \n {c}')
