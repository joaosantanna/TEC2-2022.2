from random import  randint

numeros = list()

for i in range(100):
    numeros.append(randint(1,20))

print(numeros)

resultado = dict()
# iniciar dicionario usando count
for num in range(1,21):
    resultado[num] = numeros.count(num)

print('Resultado')
for c , v in resultado.items():
    print(f'{c} - {v}')






