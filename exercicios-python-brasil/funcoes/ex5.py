'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

def somaImposto(taxaImposto, custo):
    return taxaImposto*custo/100

imposto = float(input("Digite a porcentagem de imposto sobre vendas: "))
custo_item = float(input("Digite o custo do item: R$"))

print("imposto sobre o item: R$", somaImposto(imposto, custo_item))
