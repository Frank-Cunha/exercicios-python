area_pintada = float(input("Digite a quantidade de metros quadrados da área a ser pintada: "))
litros_neces = area_pintada/3
latas_neces = round(litros_neces/18) #Sempre rredondando o número para cima: round(num + 0.5). Sempre arredondar para baixo: round(num - 0.5)
preco_latas = latas_neces*80
print("Quantidades de latas de tinta a serem compradas: ", latas_neces)
print("Preço total: R$", preco_latas)