class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>> Código {self.codigo}, Saldo R$ {self.saldo} <<]'

conta_da_Raissa = ContaCorrente(123)
#print(conta_da_Raissa)

conta_da_Raissa.deposita(10000)
#print(conta_da_Raissa)

conta_do_Rafa = ContaCorrente(456)
conta_do_Rafa.deposita(15000)
#print(conta_do_Rafa)

contas = [conta_do_Rafa, conta_da_Raissa]
for conta in contas:
    print(conta)

print(contas[0])

conta_do_Rafa.deposita(5000)
print(contas[0])

print(conta_do_Rafa)

conta_da_Raissa.deposita(5000)
print(contas[1])
print(conta_da_Raissa)