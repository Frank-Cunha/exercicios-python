#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Digite um número inteiro: "))
fatores = 0
primos = []

for item in range(1, num +1):
    for i in range(1, item +1):
        if item%i == 0:
            fatores += 1
    if fatores == 2:
        primos.append(item)
    fatores = 0

print("Números primos entre 1 e", num, ":", primos)

