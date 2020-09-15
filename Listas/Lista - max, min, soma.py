L = []
resp = "Sim"

while resp == "Sim":
    n = float(input("Digite um número: "))
    L.append(n)
    resp = input('Deseja digitar outro número? (Sim/Não): ').capitalize()
    
print(L)

i = len(L)

maxi = max(L)
meno = min(L)
soma = sum(L)

media = soma / i

input('O maior número digitado é %0.2f' % maxi)
input('O menor número digitado é %0.2f' % meno)
input('A média dos números digitados é %0.2f' % media)
