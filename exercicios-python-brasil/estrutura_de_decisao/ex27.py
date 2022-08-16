'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
morangos_kg = float(input("Escreva a quantidade em kg de morangos adquiridos: "))
macas_kg = float(input("Escreva a quantidade em kg de maçãs adquiridos: "))

if morangos_kg <= 5:
    preco_morangos = morangos_kg*2.5
elif morangos_kg > 5:
    preco_morangos = morangos_kg*2.20

if macas_kg <= 5:
    preco_macas = macas_kg*1.80
elif macas_kg > 5:
    preco_macas = macas_kg*1.50

if (morangos_kg + macas_kg > 8) or (preco_morangos + preco_macas > 25):
    preco_total = preco_morangos + preco_macas - ((preco_morangos + preco_macas)*0.10)
    print("Valor total a ser pago: R$%.2f"% preco_total )
else:
    preco_total = preco_macas + preco_morangos
    print("Valor total a ser pago: R$%.2f"% preco_total)



    
