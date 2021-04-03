def jogar():
      print('_____________________________________')
      print('=== Bem Vindo ao Jogo da Forca ===')
      print('_____________________________________')

      palavra_secreta = 'banana'.lower()
      letras_acertadas = ['_' for letra in palavra_secreta]       # List Comprehensions
      enforcou = False
      acertou = False
      erros = 0

      while ( not enforcou and not acertou ):
            print(letras_acertadas)
            chute = input('Digite uma letra: ')
            chute = chute.strip().lower()               # Tira os espaços

            if ( chute in palavra_secreta ):
                  index = 0
                  for  letra in palavra_secreta:
                        if ( chute == letra ):
                              letras_acertadas[index] = letra
                        index += 1
            else:
                  erros += 1

            # Verifica se errou 6 vezes
            enforcou = erros == 6
            # Verifica se ainda existem '_' na lista
            acertou = '_' not in letras_acertadas


      if ( acertou ):
            print('\nVocê ganhou!')
      else:
            print('\nVocê perdeu!')
      print('\n____________Fim do Jogo____________')

if ( __name__ == "__main__" ):
      jogar()


### tupla:
# num =  (1, 2, 3, 4)  ->    imutável
### set:
# num = {12, 45, 35, 86} -> não aceita valores repetidos