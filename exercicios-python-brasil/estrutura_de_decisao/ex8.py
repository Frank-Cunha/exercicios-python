#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: R$"))
produto2 = float(input("Digite o preço do segundo produto: R$"))
produto3 = float(input("Digite o preço do terceiro produto: R$"))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto")
elif produto3 < produto1 and produto3 < produto2:
    print("Você deve comprar o terceiro produto")
else:
    print("Erro")