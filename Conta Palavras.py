s = "Instituto MauÃ¡ de Tecnologia"
contaespaco  = s.count(" ")
print ('A frase possui %i palavras' % (contaespaco+1))

print('\n\n\t\tOutro Método')

frase = input('Digite uma frase: ').lower()
palavra = input('Digite uma palavra: ').lower()

Lista = frase.split()
print(Lista)

print('A palavra apareceu %i vez(es)' %Lista.count(palavra))

 