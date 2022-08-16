area_pintada = float(input("Digite a quantidade de metros quadrados da área a ser pintada: "))
litros_neces = area_pintada/6
latas_neces = round(litros_neces/18 + 0.5)
galoes_neces = round(litros_neces/3.6 + 0.5)

print("Comprando apenas latas de 18 litros seriam necessárias", latas_neces, "latas de tinta ao preço de R$", latas_neces*80)
print("Comprando apenas galões de 3.6 litros seriam necessários", galoes_neces, "latas de tinta ao preço de R$", galoes_neces*25)


