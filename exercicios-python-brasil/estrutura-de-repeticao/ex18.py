#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = [0]
menor = 999999999
maior = 0
cont = 0
soma = 0
resposta = "S"

while resposta == "S":
    cont += 1
    numeros.append(int(input("Adicione um número: ")))
    if numeros[cont] < menor:
        menor = numeros[cont]
    if numeros[cont] > maior:
        maior = numeros[cont]
    soma += numeros[cont]
    resposta = input("Continuar? S/N ")

print("Menor valor: ", menor, "\nMaior valor: ", maior, "\nSoma dos valores: ", soma)

    

