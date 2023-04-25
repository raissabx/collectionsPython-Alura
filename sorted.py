from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>> Código: {self._codigo} - Saldo: R$ {self._saldo} <<]'

conta_Raissa = ContaSalario(30)
conta_Raissa.deposita(330)

conta_Rafael = ContaSalario(26)
conta_Rafael.deposita(300)

contas = [conta_Raissa, conta_Rafael]
#print(conta_Raissa)
#print(conta_Rafael)

#for conta in sorted(contas, key=attrgetter('_saldo')):
    #print(conta)

conta_Pandora = ContaSalario(1)
conta_Pandora.deposita(10)
conta_Miguel = ContaSalario(2)
conta_Miguel.deposita(10)

contas2 = [conta_Raissa, conta_Rafael, conta_Miguel, conta_Pandora]

print(conta_Raissa <= conta_Rafael)
