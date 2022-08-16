#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite a base do número: "))
expoente = int(input("Digite o expoente do número: "))

potencia=1

for count in range(expoente):
    potencia *= base
    count += 1

print(base,"^",expoente,"=",potencia)



