#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura_meses = []

for i in range(len(meses)):
    print("Digite a temperatura média de "+ meses[i] +": ", end="")
    temperatura_meses.append(int(input()))

media_anual = sum(temperatura_meses)/len(temperatura_meses)

print("\nTemperaturas acima da média anual: \n")

for i in temperatura_meses:
    if i > media_anual:
        print(meses[temperatura_meses.index(i)]+" - "+ str(i)+"°C")