'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class TV:
    def __init__(self, numero_canal=0):
        if (numero_canal <=100) and (numero_canal >= 0):
            self.numero_canal = numero_canal
        else:
            print("Número de canal inválido. ligando no canal 0...")
            self.numero_canal = 0

        self.volume = 20

    def aumentar_v(self, volume_aumentar):
        if (self.volume + volume_aumentar) <= 100:
            self.volume = self.volume + volume_aumentar
        else:
            print("Volume máximo é 100")
            self.volume = 100

    def diminuir_v(self, volume_diminuir):
        if (self.volume - volume_diminuir) >= 0:
            self.volume = self.volume - volume_diminuir
        else:
            print("Volume mínimo é 0")
            self.volume = 0

        