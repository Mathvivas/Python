from validate_docbr import CNPJ
from cpf import Cpf
from cnpj import Cnpj

class Documento:
    @staticmethod
    def criar_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError('Quantidade de Dígitos Inválida!')

