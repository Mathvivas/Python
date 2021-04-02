import random

print('__________________________________')
print('Bem vindo ao jogo de Adivinhação!')
print('__________________________________')

op = 's'

while ( op == 's' ):
    tentativas = 3
    numero_secreto = random.randint(1, 10)          # Números aleatórios de 1 a 10

    while ( tentativas != 0 ):
        chute = int(input('\nDigite um número entre 1 e 10: '))

        if ( chute == numero_secreto ):
            print('\nVocê acertou!')
            break
        elif ( chute < 1 or chute > 10 ):
            print(f'\nValor está fora do desejado! Erro não será descontado. Tentativas restantes: {tentativas}')
        elif ( chute != numero_secreto ):
            tentativas -= 1
            print(f'\nVocê errou! Tentativas restantes: {tentativas}')
            if ( numero_secreto > chute ):
                print('\nTente mais alto!')
            else:
                print('\nTente mais baixo!')

    op = input('\nDeseja jogar o jogo novamente (s/n): ')