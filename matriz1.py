from random import randint


a = []
b = []
soma = []
for linha in range(3):
    tmp = []
    for coluna in range(3):
        n = randint(1, 10)
        tmp.append(n)
    a.append(tmp)
print('Matriz A')
for linha in range(3):
    for coluna in range(3):
        print(a[linha][coluna], end=' ')
    print()



for linha in range(3):
    tmp = []
    for coluna in range(3):
        n = randint(1, 10)
        tmp.append(n)
    b.append(tmp)
print('Matriz B')
for linha in range(3):
    for coluna in range(3):
        print(b[linha][coluna], end=' ')
    print()

# somando as duas matrizes
for linha in range(3):
    tmp =[]
    for coluna in range(3):
        tmp.append(a[linha][coluna] + b[linha][coluna])
    soma.append(tmp)


# imprimindo o resultado
print('Matriz B')
for linha in range(3):
    for coluna in range(3):
        print(soma[linha][coluna], end=' ')
    print()




