import numpy as np
import matplotlib.pyplot as plt

categ = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
valores = [19, 47, 35, 8, 33, 45]

iBarra = np.arange(len(valores))
print(iBarra)
larg = 0.9

plt.ylabel('Pratos Vendidos')
plt.xticks(iBarra, categ)

#plt.xticks(iBarra + larg/2, categ)

plt.bar(iBarra, valores, width = larg, color = 'g')
plt.show()