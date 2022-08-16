#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input("Digite o número correspondente ao dia da semana:\n 1 - Domingo\n 2 - Segunda\n 3 - Terça\n 4 - Quarta\n 5 - Quinta\n 6 - Sexta\n 7 - Sábado\n"))

if dia_semana == 1:
    print("Domingo!")
elif dia_semana == 2:
    print("Segunda!")
elif dia_semana == 3:
    print("Terça!")
elif dia_semana == 4:
    print("Quarta!")
elif dia_semana == 5:
    print("Quinta!")
elif dia_semana == 6:
    print("Sexta!")
elif dia_semana == 7:
    print("Sábado!")
else:
    print("Valor inválido")