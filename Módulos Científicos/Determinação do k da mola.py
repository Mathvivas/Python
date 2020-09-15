import numpy as np

m = np.array( [ 6, 10, 16, 20, 24, 30, 34, 38] ) * 1e-3 # g → kg
L = np.array( [15, 16, 17, 21, 21, 26, 28, 29] ) * 1e-2 # cm → m
F = 9.81 * m

P = np.poly1d(np.polyfit(L, F, 1))
print("Equação ajustada:", P)

# coeficiente angular de uma reta (y = mx + b) = m 

k = P[1]   # coeficiente angular do polinômio
print('k = %.3f N/m' % k)

