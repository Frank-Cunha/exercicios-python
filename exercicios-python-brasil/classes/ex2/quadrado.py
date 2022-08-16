'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self, valor_mudar):
        self.tamanho_do_lado = valor_mudar
    
    def valor_lado_area(self):
        self.area = self.tamanho_do_lado ** 2
        return self.tamanho_do_lado