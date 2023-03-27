frase = input('Digite uma frase:')

vogais = ['a','e','i','o','u','A','E','I','O','U']

quantidade_vogais = 0
for v in vogais:
    quantidade_vogais += frase.count(v)

print(f'Quatidade de vogais = {quantidade_vogais}')