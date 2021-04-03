import random


def jogar():

    boas_vindas()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = esconder_palavra(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while ( not enforcou and not acertou ):
        print(letras_acertadas)

        chute = inicializar_chute()

        if ( chute in palavra_secreta ):
            marcar_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenhar_forca(erros)

        # Verifica se errou 7 vezes
        enforcou = erros == 7
        # Verifica se ainda existem '_' na lista
        acertou = '_' not in letras_acertadas


    if ( acertou ):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)
    print('\n____________Fim do Jogo____________')


def boas_vindas():
    print('_____________________________________')
    print('\tBem Vindo ao Jogo da Forca')
    print('_____________________________________\n')


def carregar_palavra_secreta():
    # with open("palavras.txt") as arquivo:
    #       for linha in arquivo:
    #             print(linha)

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())  # strip limpa o \n n final da palavra

    arquivo.close()

    numero = random.randrange(0, len(palavras))  # De zero até o len - 1
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta


def esconder_palavra(palavra_secreta):
    return ['_' for letra in palavra_secreta]       # List Comprehensions


def inicializar_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip().lower()  # Tira os espaços
    return chute


def marcar_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()


if ( __name__ == "__main__" ):
    jogar()


### tupla:
# num =  (1, 2, 3, 4)  ->    imutável
### set:
# num = {12, 45, 35, 86} -> não aceita valores repetidos