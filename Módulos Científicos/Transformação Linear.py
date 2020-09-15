# Transformação Linear ----- M = T^-1 . R . T (produto escalar @ )

import numpy as np

teta = float(input('Digite o ângulo teta (graus): '))
teta = np.radians(teta)

dx = float(input('Delta x: '))
dy = float(input('Delta y: '))

T = np.identity(3)
T[0, 2] = -dx
T[1, 2] = -dy

R = np.identity(3)
R[0, 0] = np.cos(teta)
R[0, 1] = -np.sin(teta)
R[1, 0] = np.sin(teta)
R[1, 1] = np.cos(teta)

M = np.linalg.inv(T) @ R @ T 
print(M)