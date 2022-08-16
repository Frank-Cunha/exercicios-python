from ponto_e_retangulo import Ponto
from ponto_e_retangulo import Retangulo

while True:
    largura_retangulo1 = int(input("Digite o valor da largura do retangulo: "))
    altura_retangulo1 = int(input("Digite o valor da altura do retangulo: "))

    retangulo1 = Retangulo(largura_retangulo1, altura_retangulo1)
    retangulo1.centro()
