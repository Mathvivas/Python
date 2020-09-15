import numpy as np

x = np.array( [12.5, 26.9, 56.7, 72.0] )
y = np.array( [45.8, 47.7, 50.0, 52.0] )

P = np.polyfit(x, y, 2) # ajusta os pontos em uma reta (1) ou curva (2,3,...)
print(P)
A = np.poly1d(P)
print(A)