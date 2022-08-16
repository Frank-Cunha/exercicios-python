#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = 0

if num1 < num2:
    for i in range(num1,num2):
        print(i)
        soma = soma + i
elif num2 < num1: 
    for i in range(num2,num1):
        print(i)
        soma = soma + i

print("Soma dos números: ", soma)