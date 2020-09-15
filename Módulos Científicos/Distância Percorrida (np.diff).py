import numpy as np

x = np.array([0, -178, -802, -1024, -935, -712, -612, -612, -590, -590, -623,
              -724, -724, -690, -590])

y = np.array([0, 78, 668, 1358, 1514, 1681, 2082, 2160, 2171, 2193, 2238, 2338,
              2371, 2416, 2416])

# Distância ----> d² = dx² + dy²
dx = np.diff(x)
dy = np.diff(y)

D = sum(np.sqrt(dx ** 2 + dy ** 2))
print('A distância percorrida por carro é %0.2f metros ' % D)

# Distância por Drone

Ddrone = np.sqrt((x[-1] - x[0]) ** 2 + (y[-1] - y[0]) ** 2)
print('A distância percorrida pelo Drone é %0.2f metros' % Ddrone)
