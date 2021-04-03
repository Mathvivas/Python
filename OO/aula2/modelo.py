class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()       # _nome: Protected (JAVA)
        self.ano = ano
        self._likes = 0      # No momento de criação do filme, likes não é mencionado, pois não deve ser

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    ## toString()
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # O polimorfismo nada mais é do que implantar comportamentos próprios, mas herdando da minha "Classe Mãe".
        super().__init__(nome, ano)     # Chama o construtor da mãe
        self.duracao = duracao

    ### Override
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    ### Override
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes'


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2018, 2)
#print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

filmes_e_series = [ vingadores, atlanta ]

for programa in filmes_e_series:
    print(programa)