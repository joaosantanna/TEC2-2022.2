from random import randint

numeros = list()

for i in range(100):
    numeros.append(randint(1,20))

print('Frequencia dos numeros')
for i in range(1,20):
    print(f'numero {i} = {numeros.count(i)}')

