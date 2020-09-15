n = int(input('Digite o nº de projetos: '))
D = {}
L = []

i = 1
while i <= n:
    código = input('Digite o código do projeto: ')
    tempo = input('Digite o tempo de execução(horas): ')
    i += 1
    D[código] = tempo+'h'

print(D)

L = list(D.keys())
L.sort()
print(L)

for k in L:
    print(k, '---->', D[k])
