n = int(input('Digite a quantidade de itens da lista: '))

L = []
i = 1

while i <= n:
    valor = float(input('Valor' + str(i) + '= '))
    L.append(valor)
    i += 1
    
x = input('(c)rescente ou não?: ')

if x == 'c':
    L.sort()
else:
    L.sort(reverse=True)

print(L)
