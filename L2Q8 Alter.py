from random import randint, seed
seed(18)
a = set()
b = set()
c = set()
d = set()
e = set()

while True:
    a.add(randint(1,40))
    if len(a) == 20:
        break
while True:
    b.add(randint(1,40))
    if len(b) == 20:
        break
while True:
    c.add(randint(1,40))
    if len(c) == 20:
        break
while True:
    d.add(randint(1,40))
    if len(d) == 20:
        break
while True:
    e.add(randint(1,40))
    if len(e) == 20:
        break



intersecao = a.intersection(b.intersection(c.intersection(d.intersection(e))))
print('a) numeros presentes em todos os conjuntos')
print(intersecao)

# primeiro vou unir todas os conjuntos
uniao = a.union(b.union(c.union(d.union(e))))
nao_presentes = set()
for i in range(1,41): # todos os numeros que podiam ser sorteados
   if i not in uniao:
       nao_presentes.add(i)
print('b) numeros entre 1 e 40 nao presentes em nenhum conjunto')
print(nao_presentes)

# vou varrer todos os numeros do conjunto uniao
# contando quantas vezes cada um deles aparece nos conjuntos
# vou guardar o resulado em um dicionario onde a chave sao os numeros
# do conjunto e o valor é a quantidade de vezes que ele aparece
resultado = dict()
frequencia = 0
for n in uniao:
    if n in a:
        frequencia += 1
    if n in b:
        frequencia += 1
    if n in c:
        frequencia += 1
    if n in d:
        frequencia += 1
    if n in e:
        frequencia += 1
    resultado[n] = frequencia
    frequencia = 0

maior_frequencia = max(resultado.values())
menor_frequencia = min(resultado.values())
#print(f'{maior_frequencia =} ')
#print(f'{menor_frequencia =} ')
print('c)Numeros que aparecem com mais frequencia nos conjuntos')
for v, f in resultado.items():
    if f == maior_frequencia:
        print(v, end = ' ')
print(f'\n{maior_frequencia} x cada um')

print('d)Numeros que aparece com menor frequencia nos conjuntos')
for v, f in resultado.items():
    if f == menor_frequencia:
        print(v, end = ' ')
print(f'\n{menor_frequencia} x cada um')