#Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
resposta = "S"
soma_notas = 0

while resposta == "S":
    notas.append(float(input("Digite a nota: ")))
    resposta = input("Adicionar mais notas? S/N ")

for i in notas:
    soma_notas += i

media = soma_notas/len(notas)

print("Média aritmética das notas: ", media)

