'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

num = int(input("Digite o número que você deseja o fatorial: "))
fatorial = 1
print(str(num) +"! = ", num,  end="")

for i in range(1,num + 1):
    if i != num:
        print(" .", num-i, end="")
    fatorial *= i

print(" =", fatorial)