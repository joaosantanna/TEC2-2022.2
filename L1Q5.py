l = list()

while True:
    n = int(input('Digite um numero ( 0 ) para sair:'))
    if n == 0:
        break
    else:
        l.append(n)
l.sort()
print(l)
