'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''
from datetime import date

data_atual = date.today()

salario_inicial = 1000
ano_salario_inicial = 1995
aumento = 0.015

for i in range(ano_salario_inicial +1 , data_atual.year +1):
    salario_atual = salario_inicial + (salario_inicial*aumento)
    print(i, salario_atual)
    aumento *= 2

