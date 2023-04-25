class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[<< Código: {self._codigo} - Saldo: {self._saldo} >>]'




conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

contas = [conta1, conta2]

print(conta1 == conta2)

#A isinstance()função retorna Truese o objeto especificado for do tipo especificado, caso contrário False.

print(isinstance(ContaSalario(37), ContaSalario))

