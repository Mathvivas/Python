print('Vamos fazer um quiz!!')
name = input('Digite o seu nome: ').capitalize()

print('Oii!', name, ', tudo bem?')
x = input('Então...quer saber o que o Matheus acha de você? (S/N): ').capitalize()
if x.startswith('S'):
    print('Ele te acha sensacional! Divertida, legal...')
else:
    print('Isso é programado, sem problemas, posso te dizer aqui mesmo: Ele te acha maravilhosa!!')
    