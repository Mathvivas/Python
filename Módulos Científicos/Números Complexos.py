import numpy as np

# Entrada dos Coeficientes
n = int(input('Grau n: '))
a = np.arange(n + 1)
for i in range(n + 1):
    a[i] = float(input('a%i: ' % (n-i)))

P = np.poly1d(a)
print(P)

# Lista de Reais e Complexos
raizes = P.roots
R = []
C = []
for raiz in raizes:
    if np.imag(raiz) == 0:
        R.append(np.real(raiz))
    else:
        C.append(raiz)
print('Raízes Reais Puras')
for c in R:
    print('%.4f' % c)
print('Raízes Complexas')
for c in C:
    print('%.4f %+.4f i' % (np.real(c), np.imag(c)))
