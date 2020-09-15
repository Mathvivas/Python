import numpy as np
import matplotlib.pyplot as plt

xr1 = np.linspace(-5,1)
xp = np.linspace(1,8)
xr2 = np.linspace(8,15)

yp = np.poly1d( [-1,10,0] )  # cria o polinômio da parábola
print(yp)
dyp = yp.deriv() # calcula a derivada da parábola

m1 = dyp(min(xp)) # coeficiente angular da derivada (= reta)
b1 = yp(min(xp)) - ( m1 * (min(xp)) ) # coeficiente linear 
y1 = np.poly1d( [m1,b1] )  # cria a reta 1
print('Coeficiente angular da reta 1:', m1)
print('Coeficiente linear da reta 1:', b1)

m2 = dyp(max(xp))
b2 = yp(max(xp)) -( m2 * (max(xp)) )
y2 = np.poly1d( [m2,b2] )  # cria a reta 2
print('Coeficiente angular da reta 2:', m2)
print('Coeficiente linear da reta 2:', b2)

plt.plot(xp,yp(xp), 'b')   # desenha a curva azul
plt.plot(xr1,y1(xr1), 'b') # desenha a primeira reta azul
plt.plot(xr2,y2(xr2), 'b') # desenha a segunda reta azul
plt.plot(min(xp),yp(min(xp)),'go', max(xp),yp(max(xp)),'go')  # desenha os 
                                                            # pontos de tangência
plt.show() 

