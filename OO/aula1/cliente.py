class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):             # cliente.nome
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):      # cliente.nome = novo_nome
        print('Chamando o setter nome()')
        self.__nome = novo_nome