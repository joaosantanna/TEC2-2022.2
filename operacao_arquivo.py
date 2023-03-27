import pickle

info = []
print('primeira tentativa')
for dado in info:
    print(dado)

with open('dados.bin', 'rb') as arq:
    info = pickle.load(arq)
print('dados carregados com sucesso')

print('segunda tentativa')
for dado in info:
    print(dado)