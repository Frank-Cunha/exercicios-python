#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Informe um dia do mês: "))
mes = int(input("Informe um mês: "))
ano = int(input("Informe um ano: "))

if dia <= 31 and mes <= 12 and ano >= 0:
    print("A data " + str(dia) + "/" + str(mes) + "/"+ str(ano)+ " é válida.")
else: 
    print("Data inválida")

