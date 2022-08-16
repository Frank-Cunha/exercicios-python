#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []

for i in range(20):
    print("Digite o "+str(i+1)+"o. número: ", end="")
    numeros.append(int(input()))
    if numeros[i]%2 == 0:
        pares.append(numeros[i])
    elif numeros[i]%2 != 0:
        impares.append(numeros[i])

print("\nNúmeros lidos: "+str(numeros[0]), end="")
for i in range(1, len(numeros)):
    print(", "+str(numeros[i]), end="")

print("\nNúmeros pares: "+str(pares[0]), end="")
for i in range(1, len(pares)):
    print(", "+str(pares[i]), end="")

print("\nNúmeros impares: "+str(impares[0]), end="")
for i in range(1, len(impares)):
    print(", "+str(impares[i]), end="")