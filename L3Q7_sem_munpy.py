from random import  randint

a = []
b = []

for l in range(5):
    tmp = []
    for c in range(5):
        tmp.append(randint(1,100))
    a.append(tmp)

for l in range(5):
    tmp = []
    for c in range(5):
        tmp.append(randint(1,100))
    b.append(tmp)

print('Matriz a')
for l in a:
    print(l)

print('Matriz b')
for l in b:
    print(l)

r = []
for l in range(5):
    tmp = []
    for c in range(5):
        tmp.append(0)
    r.append(tmp)


for l in range(5):
    for c in range(5):
        r[l][c] = a[l][c] + b[l][c]

print('Matriz r')
for l in r:
    print(l)


