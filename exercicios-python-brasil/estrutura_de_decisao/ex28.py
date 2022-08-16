'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tipo_carne = input("Qual o tipo de carne a ser comprada? F (para File Duplo) A (para Alcatra) P (para Picanha): ")
quantidade_carne = float(input("Digite a quantidade de carne desejada em kg: "))
cartao_tabajara = input("Compra feita no cartão Tabajara? S/N ")

if tipo_carne == "F":
    carne_selecionada = "File Duplo"
    if quantidade_carne <= 5:
        preco_carne = quantidade_carne*4.90
    elif quantidade_carne > 5:
        preco_carne = quantidade_carne*5.80
elif tipo_carne == "A":
    carne_selecionada = "Alcatra"
    if quantidade_carne <= 5:
        preco_carne = quantidade_carne*5.90
    elif quantidade_carne > 5:
        preco_carne = quantidade_carne*6.80
elif tipo_carne == "P":
    carne_selecionada = "Picanha"
    if quantidade_carne <= 5:
        preco_carne = quantidade_carne*6.90
    elif quantidade_carne > 5:
        preco_carne = quantidade_carne*7.80

if cartao_tabajara == "S":
    preco_total = preco_carne - (preco_carne*0.05)
    print("\nCupom Fiscal:\n\nTipo de carne: ", carne_selecionada,"\nQuantidade de carne:", quantidade_carne,"kg \nPreço total: R$%.2f"% preco_carne, "\nTipo de pagamento: Cartão Tabajara \nValor do desconto: 5%")
    print("Valor a pagar: R$%.2f"% preco_total)
else:
    preco_total = preco_carne
    print("\nCupom Fiscal:\n\nTipo de carne: ", carne_selecionada,"\nQuantidade de carne:", quantidade_carne,"kg\nPreço total: R$%.2f"% preco_carne, "\nTipo de pagamento: Dinheiro \nValor do desconto: 0%")
    print("Valor a pagar: R$%.2f"% preco_total)


