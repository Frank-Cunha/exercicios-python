#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numero = []
pares = 0
impares = 0

for i in range(10):
    numero.append(int(input("Digite um número inteiro: ")))
    
    if numero[i]%2 == 0:
        pares += 1
    elif numero[i]%2 != 0:
        impares += 1

print("Quantidade de números pares: ", pares, "\nQuantidade de números impares: ", impares)