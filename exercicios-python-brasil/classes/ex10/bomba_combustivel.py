'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class bombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valorAbastecer):
        print("Quantidade de litros colocada: %.2f"% (valorAbastecer/self.valorLitro))
        self.quantidadeCombustivel = self.quantidadeCombustivel - (valorAbastecer/self.valorLitro)
    
    def abastecerPorLitro(self, quantidadeLitros):
        print("Valor a ser pago por", quantidadeLitros, "litros de combustível: R$", quantidadeLitros* self.valorLitro)
        self.quantidadeCombustivel = self.quantidadeCombustivel - quantidadeLitros

    def alterarValor(self, valorLitro_alterado):
        self.valorLitro = valorLitro_alterado

    def alterarCombustivel(self, combustivel_alterar):
        self.tipoCombustivel = combustivel_alterar
    
    def alterarQuantidadedeCombustivel(self, quantidadeCombustivel_alterar):
        self.quantidadeCombustivel = quantidadeCombustivel_alterar
