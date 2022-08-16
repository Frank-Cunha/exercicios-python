'''Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
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
    