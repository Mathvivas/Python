from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento,):
        if ( self.cnpj_eh_valido(documento) ):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválida!")

    def __str__(self):
        return self.format_cnpj()

    def cnpj_eh_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
