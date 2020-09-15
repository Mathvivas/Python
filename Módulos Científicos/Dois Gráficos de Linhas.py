import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5.15)



plt.subplot(2, 1, 1)    # 2 linhas, 1 coluna, 1º Gráfico
plt.title("Deslocamento")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid()

y = 30+20*t-5*t**2
plt.plot(t, y)


plt.subplot(2, 1, 2)   # 2 linhas, 1 coluna, 2º Gráfico
plt.title("Estudo sobre Velocidade")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid()

y = 20-10*t
plt.plot(t, y, 'r',  2, 0, 'go')


plt.tight_layout()
plt.show()