import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 5, 5)
print(x)

y = x ** 3 - 2 * x ** 2 - 5 * x + 6

plt.title("Título do Gráfico")
plt.plot(x, y)
plt.show()