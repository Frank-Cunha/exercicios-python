'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio","Junho","Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print("Digite sua data de nascimento: ")
dia = input("Dia: ")
mes = input("Mês: ")
ano = input("Ano: ")

print("\nData de Nascimento: "+ f"{int(dia):02}"+"/"+f"{int(mes):02}"+"/"+ ano)
print("Você nasceu em "+ dia +" de "+meses[int(mes)-1]+" de "+ ano)

