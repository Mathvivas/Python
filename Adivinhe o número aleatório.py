import random

print('===============O===============')
print('Adivinhe o número entre 1 e 9 (3 chances)')

i = 1
n = random.randint(1,9)

while i <= 3:
    c = int(input('%iº Chance: '  % (i)))
    if c == n:
        print('Você acertou!! O número é %i!' % (c))
        break
    else:
        print('Você errou!')
    i += 1
