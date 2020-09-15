frase = input('Digite uma frase: ')
D = {}

for k in frase:
    D[k] = frase.count(k)
    
print(D)