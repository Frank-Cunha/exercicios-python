'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
valor_hora = int(input("Valor da sua hora: R$"))
horas_mes = int(input("Horas trabalhadas no mês: "))
salario_bruto = valor_hora*horas_mes

if salario_bruto <= 900:
    print("Salário Bruto: (", valor_hora,"*", horas_mes, ")       : R$", salario_bruto)
    print("(-) IR (isento)                 : R$ 00, 00 ")
    print("(-) INSS ( 10%)                 : R$", salario_bruto*0.10)
    print("FGTS (11%)                      : R$", salario_bruto*0.11)
    print("Total de descontos              : R$", (salario_bruto*0.10)+(salario_bruto*0.11))
    print("Salário Liquido                 : R$", salario_bruto - (salario_bruto*0.10 + salario_bruto*0.11))
elif salario_bruto <= 1500:
    print("Salário Bruto: (", valor_hora,"*", horas_mes, ")    : R$", salario_bruto)
    print("(-) IR (5%)                     : R$", salario_bruto*0.05)
    print("(-) INSS ( 10%)                 : R$", salario_bruto*0.10)
    print("FGTS (11%)                      : R$", salario_bruto*0.11)
    print("Total de descontos              : R$", (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.05))
    print("Salário Liquido                 : R$", salario_bruto - (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.05))
elif salario_bruto <= 2500:
    print("Salário Bruto: (", valor_hora,"*", horas_mes, ")     : R$", salario_bruto)
    print("(-) IR (10%)                    : R$", salario_bruto*0.10)
    print("(-) INSS ( 10%)                 : R$", salario_bruto*0.10)
    print("FGTS (11%)                      : R$", salario_bruto*0.11)
    print("Total de descontos              : R$", (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.10))
    print("Salário Liquido                 : R$", salario_bruto - (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.10))
elif salario_bruto > 2500:
    print("Salário Bruto: (", valor_hora,"*", horas_mes, ")      : R$", salario_bruto)
    print("(-) IR (20%)                    : R$", salario_bruto*0.20)
    print("(-) INSS ( 10%)                 : R$", salario_bruto*0.10)  
    print("FGTS (11%)                      : R$", salario_bruto*0.11)
    print("Total de descontos              : R$", (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.20))
    print("Salário Liquido                 : R$", salario_bruto - (salario_bruto*0.10 + salario_bruto*0.11 + salario_bruto*0.20))