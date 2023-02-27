from random import  randint

def lancar_dados():
    d = randint(2,12)
    return d

def simular():
    #inicio
    # inicializacao do dicionario com os valores sorteados
    resultado ={}
    for i in range(2,13):
        resultado [i] = 0
    #print(resultado)
    for i in range(1000):
        chave = lancar_dados() # chave é o valor sorteado nos dados
        resultado[chave] += 1
    #print(resultado)
    return resultado



if __name__ == '__main__':
    r = simular()
    for c,v in r.items():
        print(f'{c} - {v/10}%')

