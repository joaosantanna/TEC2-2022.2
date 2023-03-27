from random import choice, randint,seed

seed(12)

atletas = ['João do pulo', 'Rodigo Grillo', 'Maurin Maggie', 'Ana Bunny', 'Maria Rossi']

resultados = dict()
for i in range(len(atletas)):
    atleta = choice(atletas)
    atletas.remove(atleta)
    saltos = dict()
    for n in range(1,6):
        salto = randint(30,70)/10
        saltos[n] = salto
    resultados[atleta] = saltos

for c, v in resultados.items():
    print(f'{c} - {v}')

# achando o melhor salto de cada um
melhor = dict()
for atleta, saltos_do_atleta in resultados.items():
    maior = 0
    for salto in saltos_do_atleta.values():
        maior = max(maior, salto)
    melhor[atleta] = maior

# melhor é um dicionario que contem
# o nome do atleta e seu melhor salto
m = list(melhor.values())
rank1 = max(m)
m.remove(rank1)
rank2 = max(m)
m.remove(rank2)
rank3 = max(m)
m.remove(rank3)

print('Ranque dos melhores saltos')

for c, v in melhor.items():
    if v == rank1:
        ranque1 =(c, v)
    if v == rank2:
        ranque2 = (c, v)
    if v == rank3:
        ranque3 = (c, v)

print(f'1 lugar {ranque1[0]} - {ranque1[1]} m')
print(f'2 lugar {ranque2[0]} - {ranque2[1]} m')
print(f'3 lugar {ranque3[0]} - {ranque3[1]} m')