class Televisão:
    def __init__(self, min, max):  # self representa o objeto em si
        self.ligada = False
        self.canal = 2
        self.tamanho = 40
        self.marca = 'LG'
        self.cmin = min
        self.cmax = max
    def muda_canal_baixo(self):
        if(self.canal - 1 >= self.cmin):
            self.canal -= 1
    def muda_canal_cima(self):
        if(self.canal + 1 <= self.cmax):
            self.canal += 1


print('__________TV_Quarto__________')
tv_quarto = Televisão(1,99)    # Determina o primeiro e último canal da TV
for x in range(0,120):
    tv_quarto.muda_canal_cima()
print(tv_quarto.canal)

for x in range(0,120):
    tv_quarto.muda_canal_baixo()
print(tv_quarto.canal)


tv = Televisão(1,10)
print('__________TV__________')
print(tv.ligada)
print(tv.canal)
print(tv.tamanho)
print(tv.marca)
print(tv.cmin)
print(tv.cmax)

tv_sala = Televisão(0,0)
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.marca = 'Samsung'
tv_sala.tamanho = 45

print('__________TV_Sala__________')

print(tv_sala.ligada)
print(tv_sala.canal)
print(tv_sala.tamanho)
print(tv_sala.marca)

