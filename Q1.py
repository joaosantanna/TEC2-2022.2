print('Responda sim ou nao para as seguintes perguntas:')
r1 = input('Telefonou para a vítima? :')
r2 = input('Esteve no local do crime? :')
r3 = input('Mora perto da vítima? :')
r4 = input('Devia para a vítima? :')
r5 = input('Já trabalhou com a vítima? :')
respostas = [r1, r2, r3, r4, r5]

sim = respostas.count('sim')
if sim == 2:
    print('Pessoa Suspeita')
elif sim == 3 or sim == 4:
    print('Pessoa deve ser cumplice')
elif sim == 5:
    print('Provavel assassino')
else:
    print('Inocente')