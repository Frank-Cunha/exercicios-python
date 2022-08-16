'''
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
'''

class bichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = (fome+saude)/2

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
    
    def Fome(self, fome_atual):
        self.fome = fome_atual
        self.humor = (self.fome+self.saude)/2

    def Saude(self, saude_atual):
        self.saude = saude_atual
        self.humor = (self.fome+self.saude)/2
    
    def Idade(self, idade_atual):
        self.idade = idade_atual

    def alimentar(self, comida_quantidade):
        self.fome = self.fome - comida_quantidade
    
    def brincar(self, brincar_tempo):
        self.humor = self.humor + brincar_tempo