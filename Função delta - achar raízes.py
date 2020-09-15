from math import sqrt

def delta(a, b, c):
    Delta = (b**2) - 4*a*c
    return Delta
    
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

print(delta(a, b, c))

if delta(a, b, c) < 0:
    print('Nenhuma raíz real')
elif delta(a, b, c) == 0:
    print('Uma raíz real')
else:
    print('Duas raízes reais')

x1 = (-b + sqrt(delta(a, b, c)))/(2*a)
x2 = (-b - sqrt(delta(a, b, c)))/(2*a)
print(x1)
print(x2)
