import numpy as np

def f(x):
    if 0 <= x <= 0.5:
        y = -x * (x - 1) + 2.5
    elif 0.5 <= x <= 1.35:
        y = 2.76
    elif 1.35 <= x <= 2.4:
        y = 2.76 * np.cos(0.45 * (x - 1.35))
    elif 2.4 <= x <= 5:
        y = 0.08 * (x - 2.4) * (x - 5.5) + 2.46
    elif 5 <= x <= 15:
        y = -0.025 * (x - 5) * (x - 12.5) + 2.35
    elif 15 <= x <= 18:
        y = 0.05 * (x - 15) * (x - 21) + 1.73
    return y
        
H = -1
while H < 0 or H > 18:
    H = int(input('H: '))

dx = 0.1
x = np.arange(0, H + dx, dx )
L = []
for c in x:
    L.append(f(c) ** 2)
y = np.array(L)
print(y)

V = np.pi * np.trapz(y, dx=dx)
print('Volume = ', V)
