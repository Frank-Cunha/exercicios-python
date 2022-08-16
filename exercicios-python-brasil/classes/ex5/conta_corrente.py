"Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0): #No (saldo=0) foi definido um parâmetro default caso não seja emitido nenhum argumento saldo. solução retirada de: https://stackoverflow.com/questions/15535655/optional-arguments-in-initializer-of-python-class
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def aterarNome(self, nome_alterar):
        self.nome_correntista = nome_alterar

    def deposito(self, deposito):
        self.saldo = self.saldo + deposito
        print("Saldo após o depósito: R$", self.saldo)
    
    def saque(self, saque):
        if saque > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - saque
            print("Saldo após o saque: R$", self.saldo)