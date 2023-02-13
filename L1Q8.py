
print('Digite varios numeros , espaco em branco para sair')
numeros = list()
while True:
    n = input('>')
    if n == ' ':
        break
    else:
        numeros.append(int(n) )

media = sum(numeros)/len(numeros)
print(f'Media = {media}')
print('Numeros acima da media')
for i in numeros:
    if i > media:
        print(i)

if media in numeros:
    print('Numeros na media')
    for i in numeros:
        if i == media:
            print(i)
print('Numeros abaixo da media')
for i in numeros:
    if i < media:
        print(i)

print(f'{numeros} ')



