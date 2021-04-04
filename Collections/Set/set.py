usuarios_data_science = [ 15, 23, 43, 56 ]
usuarios_machine_learning = [ 13, 23, 56, 42 ]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)       # usuários duplicados

print(set(assistiram))

# Conjunto (Set) não possui ordem
# Criando um Set -> {}

print({ 1, 2, 3, 1 })
print(type({ 1, 2, 3, 1 }))

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = { 15, 23, 43, 56 }
usuarios_machine_learning = { 13, 23, 56, 42 }

# União
print(usuarios_machine_learning | usuarios_data_science)

# Intersecção
print(usuarios_machine_learning & usuarios_data_science)

# Subtração
print(usuarios_machine_learning - usuarios_data_science)
print(usuarios_data_science - usuarios_machine_learning)

# Ou Exclusivo
print(usuarios_data_science ^ usuarios_machine_learning)

# Adição de Elementos
usuarios = { 1, 5, 76, 34, 52, 13, 17 }
usuarios.add(9)
print(usuarios)

# frozenset -> não permite modificar o set
frozen = frozenset(usuarios)
print(frozen)

