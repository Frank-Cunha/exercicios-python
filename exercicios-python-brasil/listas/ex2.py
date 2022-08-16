#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
    print("Digite o "+str(i+1)+"o. número: ", end="")
    numeros.append(int(input()))

numeros.reverse()

for i in numeros:
    print(i)