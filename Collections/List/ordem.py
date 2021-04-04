from operator import attrgetter
from functools import total_ordering    # Para fazer todos os tipos de comparação

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):        # Equals
        if ( type(other) != ContaSalario ):
            return False

        return self._codigo == other._codigo and self._codigo == other._codigo

    def __lt__(self, other):        # lesser than
        if ( self._saldo != other._saldo ):
            return self._saldo < other._saldo

        return self._codigo < other._codigo

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>> Código {self._codigo} Saldo {self._saldo} <<]'


idades = [ 15, 87, 32, 65, 56, 22, 49, 37 ]

# Ordena, mas idades permanece como era
print(sorted(idades))
# O contrário do inserido
print(list(reversed(idades)))   # Força o retorno em lista

print(sorted(idades, reverse=True))

# Ordena idades e substitui
idades.sort()
print(idades)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.depositar(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.depositar(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.depositar(500)

contas = [ conta_do_paulo, conta_da_daniela, conta_do_guilherme]

### Ordena primeiro pelo saldo, depois pelo código
# for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
#     print(conta)

print(conta_do_guilherme < conta_da_daniela)

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme >= conta_do_paulo)