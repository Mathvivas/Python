ímpares = open('Ímpares.txt', 'w')
pares = open('Pares.txt', 'w')
for n in range(0, 1000):
    if n % 2 == 0:
        pares.write('%d\n' % n)
    else:
        ímpares.write('%d\n' % n)
pares.close()
ímpares.close()
