from random import randint
import numpy as np
a = []

for i in range(10000):
    a.append(randint(25,45))
a = np.array(a)
a.shape = (100,100)
print(a)

r= np.mean(a,axis=1)
for i in r:
    print(i)