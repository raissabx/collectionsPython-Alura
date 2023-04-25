class Conta:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[<< Código: {self.codigo} - Saldo: {self.saldo} <<]'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3

print(Conta(88))

conta16 = ContaCorrente(16)
conta16.deposita(100)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(100)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()
    print(conta)



