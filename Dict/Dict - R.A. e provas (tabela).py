s = '16.96125-7\t8.5,4.5,7,6\n15.07896-3\t4,5,6,7\n16.06542-3\t7,8.5,7,7.5'

D = {}
L = []
L = s.split('\n')
L[0] = L[0].split('\t')
L[1] = L[1].split('\t')
L[2] = L[2].split('\t')

D = dict(L)
print(D)
for k in D.keys():
    D[k] =  D[k].split(',')
print(D)

print('%20s%5s%5s%5s%5s' % ('RA', 'P1', 'P2', 'P3', 'P4'))
for k in D.keys():
    print('%20s%5s%5s%5s%5s' % (k, D[k][0], D[k][1], D[k][2], D[k][3]))
    

L1 = []
for k in D.keys():
    L1.append(list(map(float, D[k]))) 
# Função map: serve para aplicarmos uma função a cada elemento de uma lista
print(L1)

# Cálculo da média
soma1 = sum(L1[0])
soma2 = sum(L1[1])
soma3 = sum(L1[2])

print('A média de 16.96125-7 é', (soma1/4))
print('A média de 15.07896-3 é', (soma2/4))
print('A média de 16.06542-3 é', (soma3/4))
    
    