a = int(input('Digite um valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))

if a + b > c:
    print('É Triangulo')
elif a + c > b:
    print('É Triangulo')
elif b + c > a:
    print('É Triangulo')
else:
    print('Não é triangulo')

if a == b == c:
    print('Equilátero')
elif a == b or a == c or b == c:
    print('Isósceles')
else:
    print('Escaleno')
    