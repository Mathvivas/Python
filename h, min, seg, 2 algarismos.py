def tempo(horas, minutos, segundos):
    horário = str(horas) + 'h' + str(minutos) + 'min' + str(segundos) + 'seg'
    return horário

horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

s = (segundos % 60)
m = (minutos + (segundos // 60)) % 60
h = (horas + (minutos // 60)) % 24

print('%02ih %02im %02is' % (h, m, s))

