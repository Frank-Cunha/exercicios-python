#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def conversor_data(dia,mes,ano):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro","Outubro", "Novembro", "Dezembro"]
    if dia > 31 or mes > 12:
        print("\nNULL, data inválida")
    else:
        print("\n"+str(dia)+" de "+meses[mes-1],"de", ano)

print("Digite uma data no formato DD/MM/AAAA: ")
dia = int((input("Dia: ")))
mes = int((input("Mês: ")))
ano = (input("Ano: "))
print("Data: "+f"{dia:02}"+"/"+f"{mes:02}"+"/"+ano)

conversor_data(dia, mes, ano)



