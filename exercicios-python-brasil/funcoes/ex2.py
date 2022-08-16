'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

def printar(n):
    for i in range(1,n + 1):
        print(n - (n-i), " ", end="")


numero = int(input(("Digite um número: ")))

printar(numero)