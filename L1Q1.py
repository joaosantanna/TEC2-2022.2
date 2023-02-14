from random import randint

numeros = []
for i in range(10):
    numeros.append(randint(1,20))

print(numeros)

x = int(input('Informe o numero que vc procura:'))

if x not in numeros:
    print(f'o numero {x} não está presente no vetor')

if x not in numeros:
    print(f'o numero {x} não está presente no vetor')

else:
    for p,v in enumerate(numeros):
        if v == x:
            print(f'numero {x} está na posição {p}')
print(numeros)



'''
#solucao alternativa usando o metodo index
# tudo isso necessario pq um numero pode aparecer mais
# de uma vez no vetor
else:
    pi = 0 # posicao inicial de busca , inicia em zero
    freq = numeros.count(x) # quantas vezes o numero aparece no vetor?
    while freq > 0 : # enquanto ainda tiver numero repetido
        p = numeros.index(x,pi) # busca x iniciando na posicao pi
        print(f'numero {x} está na posição {p}')
        pi = p + 1 # proximo valor de pi = p + 1
        # por exemplo se a primeria ocorrencia do numero
        # aconteceu na posicao 2 vc inicia a proxima busca na 3
        # por isso é P + 1
        freq -= 1 # decrementa a frequencia ate chegar em zero

'''






