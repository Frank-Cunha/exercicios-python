'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

intervalo_valores = [list(range(200,300)), list(range(300,400)), list(range(400,500)), list(range(500,600)), list(range(600,700)), list(range(700,800)), list(range(800,900)), list(range(900,1000))]
vendedores_salarios = []
cont = 0

while True:
    print("Digite as vendas brutas do "+ str(cont +1) +"o. vendedor: R$", end="")
    vendas = (int(input()))
    vendedores_salarios.append(200 + (vendas*0.09))
    if vendas == 0:
        vendedores_salarios.pop()
        break
    cont += 1

cont = 0
for i in vendedores_salarios:
    for item in intervalo_valores:
        if i in item:
            intervalo = cont + 1
        cont += 1
        
print(intervalo)



