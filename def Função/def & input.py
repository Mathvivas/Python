def tempo(horas, minutos, segundos):
    horário = horas+'h'+minutos+'min'+segundos+'s'
    return horário

horas = str(input('Digite as horas: ' ))
minutos = str(input('Digite os minutos: '))
segundos = str(input('Digite os segundos: '))
print(tempo(horas, minutos, segundos))
    