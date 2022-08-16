#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
multiplicacao = 1

for i in range(5):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    numeros.append(int(input()))

soma = sum(numeros)
for i in numeros:
    multiplicacao *= i

print("\nSoma dos números:", soma, "\nMultiplicação dos números: ", multiplicacao, "\nOs números: "+ str(numeros[0]), end="")

for i in range (1, len(numeros)):
    print(", "+ str(numeros[i]), end="")




