import time

palavra = input('Digite uma palavra: ').lower().strip()
for x in range(100):
    print()             # Pula 100 linhas depois da palavra secreta

digitadas = []
acertos = []
erros = 0

while True:
    senha = ''
    for letra in palavra:
        if letra in acertos:
            senha += letra
        else:
            senha += '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!!')
        break
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já tentou essa letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    if erros == 1:
        print(' O ')
        
    linha2 = ''
    if erros == 2:
        linha2 = ' O \n |'
    elif erros == 3:
        linha2 = ' O \n/|'
    elif erros == 4:
        linha2 = ' O \n/|/'
    if erros == 5:
        linha2 += ' O \n/|/\n/'
    elif erros == 6:
        linha2 += " O \n/|/\n// \t \t ENFORCADO!"
        print('%s' % linha2)
        time.sleep(3)
        break
    print('%s' % linha2)    #Printa a linha de cada erro conforme vai acontecendo
    