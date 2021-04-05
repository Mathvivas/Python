import re

PADRAO = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'

class Telefone:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número Incorreto!')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        # Código do País não é obrigatório
        resposta = re.findall(PADRAO, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        res = re.search(PADRAO, self.numero)
        if res.group(1) == None:
            numero_formatado = f'({res.group(2)}){res.group(3)}-{res.group(4)}'
        else:
            numero_formatado = f'+{res.group(1)}({res.group(2)}){res.group(3)}-{res.group(4)}'
        return numero_formatado