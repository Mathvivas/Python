# Um modo de definir um dict
#####
# aparicoes = dict(Guilherme = 2, cachorro = 1)
#####

aparicoes = {
    'Guilherme' : 1,
    'cachorro' : 2,
    'nome' : 2,
    'vindo' : 1
}

# Valor da Chave
print(aparicoes['Guilherme'])

# Procura uma chave, se não existir retorna o valor mencionado
print(aparicoes.get('xpto', 0))
print(aparicoes.get('cachorro', 0))

# Adição de Valores
aparicoes["Carlos"] = 1

# Modificação de Valores
aparicoes["Carlos"] = 2

# Deletar Valores
del aparicoes['vindo']
print(aparicoes)

# Iteração de Chaves
for elemento in aparicoes:
    print(elemento)

# for elemento in aparicoes.keys():
#     print(elemento)

# Iteração de Valores
for elemento in aparicoes.values():
    print(elemento)

# Iteração de Items
for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, valor, sep=' = ')
