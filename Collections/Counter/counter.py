from collections import Counter

meu_texto = 'Bem vindo meu nome é Matheus eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'

aparicoes = Counter(meu_texto.split())
print(aparicoes)

# Frequência de Aparição
def analisa_frequencia_de_letras(texto):
    apa = Counter(texto.lower())       ## Conta cada letra
    total_de_caracteres = sum(apa.values())

    proporcoes = [ (letra, frequencia / total_de_caracteres) for letra, frequencia in apa.items() ]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100:.7f} %')


analisa_frequencia_de_letras(meu_texto)

