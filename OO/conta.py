class Conta:
    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero      # __: Privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__titular} é {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def __verificar_saque(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if ( self.__verificar_saque(valor) ):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limite!')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # def get_saldo(self):
    #     return self.__saldo

    @property
    def saldo(self):
        return self.__saldo

    # def get_titular(self):
    #     return self.__titular

    @property
    def titular(self):
        return self.__titular

    # def get_limite(self):
    #     return self.__limite

    @property
    def limite(self):
        return self.__limite

    # def set_limite(self, novo_limite):
    #     self.__limite = novo_limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    ## Método Estático (da Classe)
    ## Conta.codigo_banco()
    @staticmethod
    def codigos_bancos():
        return { 'BB': '001', 'Caixa': '104', 'Bradesco': '237' }