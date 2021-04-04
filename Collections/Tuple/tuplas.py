# Imutáveis

guilherme = ('Guilherme', 37, 1981)
paulo = ('Paulo', 38, 1979)
daniela = ('Daniela', 31, 1987)

conta_do_gui = (15, 1000)
print(conta_do_gui)

# Para modificar
def depositar(conta):
    novo_saldo = conta[1] + 200
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_gui = depositar(conta_do_gui)
print(conta_do_gui)


usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(paulo)
print(usuarios)
print(usuarios[0][0])