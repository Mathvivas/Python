import random
for x in range(10):         # Printa 10 números
    print(random.randint(1,100)) # Números aleatórios de 1 a 100
    print()
    print('______________________________')
    print('random')
    print(random.random())  # Sem parâmetros / Retorna valores entre 0 e 1
    print()
    print('______________________________')
    print('uniform')
    print(random.uniform(15,30)) # Valores de ponto flutuante dentro de uma faixa
    print()
    print('______________________________')
    print('sample')

print(random.sample(range(1,101), 6)) # (1,101) - amostra; (6) - elementos a retonar
print()
print('______________________________')
print('shuffle')

a = list(range(1,11))
random.shuffle(a)    # Embaralha os elementos de uma lista
print(a)
