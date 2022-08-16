'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
'''

class Carro:

    def __init__(self, km_litro, combustivel=0):
        self.km_litro = km_litro
        self.combustivel = combustivel

    def adicionarGasolina(self, gasolina):
        self.combustivel = self.combustivel + gasolina
    
    def andar(self, distancia):
        distancia_litros = distancia/self.km_litro
        self.combustivel = self.combustivel - distancia_litros
        print(distancia, "km percorridos","\nlitros de gasolina gastos: %.2f"% distancia_litros)
    
    def obterGasolina(self):
        print("Gasolina restante: %.2f"% self.combustivel,"litros")



