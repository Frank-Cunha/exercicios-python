'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

a = int(input("Informe o valor de a: "))
if a == 0:
    print("A igual a zero, Não é uma equação de segundo grau\nPROGRAMA ENCERRADO")
elif a != 0:
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: ")) 

    delta = b**2 - 4*a*c     #Formula de delta: Δ = b^2 – 4ac
    if delta < 0:
        print("Delta negativo, a equação não possui raizes reais\nPROGRAMA ENCERRADO")
    elif delta == 0:
        print("Delta igual a zero, a equação possui apenas uma raiz real: ")
        bhaskara = (-b + delta**0.5)/2*a        #Formula de Bhaskara: x = – b ± √∆/2a
        print(bhaskara)
    elif delta > 0:
        bhaskara1 = (-b + delta**0.5)/2*a
        bhaskara2 = (-b - delta**0.5)/2*a
        print("Raizes: ", bhaskara1, bhaskara2)
        



