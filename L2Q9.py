frase = input('Digite uma frase:')
l_frase = list(frase)
while True:
    if ' ' in l_frase:
        l_frase.remove(' ')
    else:
        break
# pegando somente as letras individualmente
s_frase = set(frase)
print('Quantidade de vezes que cada letra aparece')
for letra in s_frase:
    print(f'letra {letra} - {frase.count(letra)} x')