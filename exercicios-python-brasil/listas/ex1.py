#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    print("Digite o "+str(i+1)+"o. número: ", end="")
    numeros.append(int(input()))

print("")
for i in numeros:
    print(i)
