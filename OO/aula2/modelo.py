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

    ## toString()   (JAVA)
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # O polimorfismo nada mais é do que implantar comportamentos próprios, mas herdando da minha "Classe Mãe".
        super().__init__(nome, ano)     # Chama o construtor da mãe
        self.duracao = duracao

    ### Override (JAVA)
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    ### Override    (JAVA)
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} Likes'


# Playlist herda de list, agora é iterável
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
tmep = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Filme('Demolidor', 2016, 2)
atlanta = Serie('Atlanta', 2018, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [ vingadores, atlanta, demolidor, tmep ]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)