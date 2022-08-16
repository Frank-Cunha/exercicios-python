#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

n1 = 1
n2 = 1

while True:
    print(n1)
    print(n2)
    n1 += n2
    n2 += n1
    if n1 > 500 or n2 > 500:
        print(n1)
        break