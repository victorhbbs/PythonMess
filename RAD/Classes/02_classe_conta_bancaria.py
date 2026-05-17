class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            print("O valor do depósito precisa ser maior que zero.")
            return
        
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque precisa ser maior que zero.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria("Victor", 1000)

conta.exibir_saldo()

conta.depositar(50)
conta.sacar(30)
conta.sacar(500)

conta.exibir_saldo()