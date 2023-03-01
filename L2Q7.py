from random import  randint
from prettytable import PrettyTable

x = PrettyTable()

numeros = list()

for i in range(100):
    numeros.append(randint(1,20))

print(numeros)

resultado = dict()
# iniciar dicionario usando count
for num in range(1,21):
    resultado[num] = numeros.count(num)

for busca in range(1,21):
    tmp = []
    for posicao, num in enumerate(numeros):
        if num == busca:
            tmp.append(posicao)
    tmp2 =[resultado[busca], tmp]
    resultado[busca] = tmp2


print(resultado)


x.field_names = ["Numero", "Frequencia", "Posições"]
for c , v in resultado.items():
    x.add_row([c, v[0], v[1]])

print(x)


