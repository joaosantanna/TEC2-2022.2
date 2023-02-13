from random import randint

numeros = []
for i in range(10):
    numeros.append(randint(1,20))

print(numeros)

x = int(input('Informe o numero que vc procura:'))

if x not in numeros:
    print(f'o numero {x} não está presente no vetor')

else:
    for p,v in enumerate(numeros):
        if v == x:
            print(f'numero {x} está na posição {p}')
print(numeros)





