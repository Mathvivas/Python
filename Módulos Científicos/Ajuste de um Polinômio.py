import numpy as np
import matplotlib.pyplot as plt

def R2(x, y, P):
    SQres = sum((y - P(x))**2)
    SQtot = sum((y - np.average(y))**2)
    return 1 - SQres / SQtot
n = int(input('Quantos Pontos?: '))
x = np.arange(n)
y = np.arange(n)
for i in range(n):
    x[i] = float(input('Digite x%i: ' % i ))
    y[i] = float(input('Digite y%i: ' % i ))

ordem = int(input('Ordem do polinômio de ajuste: '))
P = np.poly1d(np.polyfit(x, y, ordem))
print()
print('Polinômio de Ajuste: ', P)
print('R²: ', R2(x, y, P))
plt.plot(x, y, 'rs')
x2 = np.linspace(min(x),max(x))
plt.plot(x2, P(x2))
plt.show()
