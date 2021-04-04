idades = [ 39, 30, 22, 18 ]

print(len(idades))

idades.append(15)
idades.remove(30)

idades.insert(0, 56)

idades.extend([27, 35, 24])
print(idades)

#### List Comprehension
idades_no_ano_que_vem = [ (idade + 1) for idade in idades ]

print(idades_no_ano_que_vem)

print([ idade for idade in idades if idade > 21 ])

# for i in range(len(idades)):
#     print(i, idades[i], sep="\t")

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades): # unpacking da tupla
    print(indice, "--", idade)