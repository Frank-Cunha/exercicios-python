'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
import math

valor_saque = int(input("Valor de saque: "))

if valor_saque < 10 and valor_saque > 600:
    print("Valor inválido")
else:
    notas_100 = math.floor(valor_saque/100)
    notas_50 = math.floor((valor_saque - notas_100*100)/50)
    notas_10 = math.floor((valor_saque - notas_100*100 - notas_50*50)/10)
    notas_5 = math.floor((valor_saque - notas_100*100 - notas_50*50 - notas_10*10)/5)
    notas_1 = math.floor((valor_saque - notas_100*100 - notas_50*50 - notas_10*10 - notas_5*5)/1)

    print("Para sacar a quantida de", valor_saque, "reais, serão fornecidas: \nnotas 100 reais: ", notas_100, "\nnotas 50 reais: ", notas_50, "\nnotas 10 reais: ", notas_10, "\nnotas 5 reais: ", notas_5, "\nnotas 1 real: ", notas_1)