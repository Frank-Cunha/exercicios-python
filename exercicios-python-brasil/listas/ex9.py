#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

a = []
soma = 0

for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    a.append(int(input()))
    soma += a[i]**2

print("Soma dos quadrados dos elementos do vetor:", soma)
