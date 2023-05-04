from random import randint
import numpy as np
a = [0,3,1,2]
b=[-5,0,6,4]
c=[0.5, 1, 3, -2]
a = np.array(a)
a.shape = (2,2)
b = np.array(b)
b.shape = (2,2)
c = np.array(c)
c.shape = (2,2)


print(f'a = \n {a}')
print(f'b = \n {b}')
print(f'c = \n {c}')

print(f'a) A+B-C \n {a+b-c}')
print(f'b) -1/3.C \n {(1/3)*c}')
print(f'c) A.B \n {np.dot(a,b)}')
print(f'd) B.C \n {np.dot(b,c)}')
print(f'e) A-B + C \n {a-b+c}')

# letra a no codigo sem numpy
resultado=[]
for li in range(2):
    for col in range(2):
        resultado.append(a[li,col] + b[li,col] - c[li,col])

resultado = np.array(resultado)
resultado.shape = (2,2)
print(f'a) resultado \n {resultado}')

# letra b no codigo sem numpy
resultado=[]
for li in range(2):
    for col in range(2):
        resultado.append(1/3*c[li,col])

resultado = np.array(resultado)
resultado.shape = (2,2)
print(f'b) resultado \n {resultado}')

# letra c no codigo sem numpy
resultado=[]

resultado.append(a[0,0]*b[0,0]+a[0,1]*b[1,0])
resultado.append(a[0,0]*b[0,1]+a[0,1]*b[1,1])
resultado.append(a[1,0]*b[0,0]+a[1,1]*b[1,0])
resultado.append(a[1,0]*b[0,1]+a[1,1]*b[1,1])

resultado = np.array(resultado)
resultado.shape = (2,2)
print(f'c) resultado \n {resultado}')


