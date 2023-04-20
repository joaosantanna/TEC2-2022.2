from random import randint

import numpy as np

a = []
b = []

for i in range(9):
    a.append(randint(1,100))
    b.append(randint(1,100))

a = np.array(a)
b = np.array(b)
a.shape = (3,3)
b.shape = (3,3)

print(f'a: \n {a}')
print(f'b: \n {b}')
C = []
for l in range(3):
    for c in range(3):
        if a[l][c] > b [l,c]:
            C.append(a[l,c])
        else:
            C.append(b[l,c])
C = np.array(C)
C.shape = (3,3)

print(f'c: \n {C}')


