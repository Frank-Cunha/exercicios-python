#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número inteiro: "))
fatores = []
primos = []
divisoes = 0

for num in range(1, n):
    for i in range(1, num + 1):
        divisoes += 1
        if num%i == 0:
            fatores.append(i)

    if len(fatores) == 2:
        primos.append(num)    

    fatores = []

print("Números primos: ", primos, "\nNúmero de divisões executadas: ", divisoes)

