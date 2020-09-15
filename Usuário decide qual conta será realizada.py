a = str(input('Digite um valor: '))
b = str(input('Digite um segundo valor: '))

operação = input('Digite a operação desejada (*, +, -, /): ')

conta = a + operação + b 
print(conta)

a = float(a)
b = float(b)

if operação == '*':
    print(a*b)
elif operação == '+':
    print(a+b)
elif operação == '-':
    print(a-b)
else:
    print(a/b)
