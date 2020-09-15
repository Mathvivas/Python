def fração(num1, den1, num2, den2):
    fração1 = str(num1) + '\n' + (3 * '-') + '\n' + str(den1)
    fração2 = str(num2) + '\n' + '-' + '\n' + str(den2)
    return fração1 
    return fração2
num1 = int(input('Digite o numerador: '))
den1 = int(input('Digite o denominador: '))
num2 = int(input('Digite o numerador: '))
den2 = int(input('Digite o denominador: '))
maximo = str(max([num1, den1, num2, den2]))
print([num1, den1, num2, den2])
print(maximo)
print(len(maximo))

print(fração(num1, den1, num2, den2))
print(fração(num2, den2, num1, den1))