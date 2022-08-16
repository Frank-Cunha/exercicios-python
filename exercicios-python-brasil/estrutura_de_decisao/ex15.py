'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
lado1 = float(input("Informe o valor do primeiro lado do triângulo: "))
lado2 = float(input("Informe o valor do segundo lado do triângulo: "))
lado3 = float(input("Informe o valor do terceiro lado do triângulo: "))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triângulo escaleno")
else:
    print("Triângulo inválido")