'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
    
    def mudar_valor_lados(self, novo_LadoA, novo_LadoB):
        self.LadoA = novo_LadoA
        self.LadoB = novo_LadoB
    
    def retornar_lados(self):
        return self.LadoA, self.LadoB
    
    def calcular_area(self):
        self.area = self.LadoA * self.LadoB
        return self.area

    def calcular_perimetro(self):
        self.perimetro = (self.LadoA + self.LadoB) * 2
        return self.perimetro