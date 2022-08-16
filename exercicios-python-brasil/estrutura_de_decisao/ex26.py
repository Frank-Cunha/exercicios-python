'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
combustivel = input("Qual o combustível você deseja abastecer? G (Para gasolina) A (Para álcool) ")
if combustivel != "A" and combustivel != "G":
    print("Erro")
else:
    litros = int(input("Quantos litros? "))

if combustivel == "G":
    if litros <= 20:
        preco_desconto = litros*2.50 - (litros*2.50*0.04)
        print("Valor a ser pago: R$", preco_desconto)
    elif litros > 20:
        preco_desconto = litros*2.50 - (litros*2.50*0.06)
        print("Valor a ser pago: R$", preco_desconto)
elif combustivel == "A":
    if litros <= 20:
        preco_desconto = litros*1.90 - (litros*1.90*0.03)
        print("Valor a ser pago: R$", preco_desconto)
    elif litros > 20:
        preco_desconto = litros*1.90 - (litros*1.90*0.05)
        print("Valor a ser pago: R$", preco_desconto)

    