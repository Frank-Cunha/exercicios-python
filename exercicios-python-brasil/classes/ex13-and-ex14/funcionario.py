'''Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
'''

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def escreverNomeSalario(self):
        print("Nome do funcionário:", self.nome,"\nSalário do funcionário: R$", self.salario)

    def aumentarSalario(self, porcentualDeAumento):
        self.salario = self.salario + (self.salario * (porcentualDeAumento/100))
        print("Novo salário: R$", self.salario)
    

    