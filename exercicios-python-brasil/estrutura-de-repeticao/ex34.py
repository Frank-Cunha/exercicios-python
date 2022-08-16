#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Digite um número inteiro: "))
fatores = 0

for i in range (1, num +1):
    if num%i == 0:
        fatores += 1

if fatores > 2:
    print("O número não é primo")
elif fatores == 2:
    print("O número é primo!")
else:
    print("Erro")