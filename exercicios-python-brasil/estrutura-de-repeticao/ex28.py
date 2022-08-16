#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds = int(input("Digite a quantidade de CDs da sua coleção: "))
valor_cds = []
soma = 0

for i in range(quantidade_cds):
    print("Digite o valor em R$ do "+ str(i+1) +"o. CD: ")
    valor_cds.append(float(input()))
    soma += valor_cds[i]

media = soma/quantidade_cds

print("\nValor total investido na coleção: R$"+ str(soma) +"\nValor médio gasto em cada CD: R$"+ str(media))
