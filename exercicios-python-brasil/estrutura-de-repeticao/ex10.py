#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    for i in range(num1,num2):
        print(i)
elif num2 < num1: 
    for i in range(num2,num1):
        print(i)
