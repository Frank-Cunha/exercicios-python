'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idadeAcrescentar):
        if self.idade < 21:
            if (self.idade + idadeAcrescentar) >= 21:
                idadecrescer = 21 - self.idade
                self.altura = self.altura + (idadecrescer * 0.005)

            elif (self.idade + idadeAcrescentar) < 21:
                idadecrescer = idadeAcrescentar
                self.altura = self.altura + (idadecrescer * 0.005)

        self.idade = self.idade + idadeAcrescentar        

    def engordar(self, pesoAcrescentar):
        self.peso = self.peso + pesoAcrescentar

    def emagrecer(self, pesoPerdido):
        self.peso = self.peso - pesoPerdido

    def crescer(self, alturaGanha):
        self.altura = self.altura + alturaGanha