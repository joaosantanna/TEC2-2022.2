from random import randint
import numpy as np

m =[]
for i in range(9):
    m.append(randint(1,100))

m = np.array(m)
m.shape = (3,3)
print(m)

maior = np.max(m)

for l in range(3):
    for c in range(3):
        if m[l][c] == maior:
            print(f'Maior numero{maior} esta na posicao {l}-{c}')
