estados ={
    'Acre':'Rio Branco',
    'Amapá':'Macapá',
    'Amazonas' : 'Manaus',
    'Pará' : 'Belém',
    'Rôndonia':'Porto Velho',
    'Roraima' : 'Boa vista',
    'Tocantins':'Palmas'
}

print('Escolha um estado para saber sua capital')
for k in estados.keys():
    print(f'{k}')
nome = input('Digite o nome do estado:')
print(f'{nome} capital {estados[nome]}')