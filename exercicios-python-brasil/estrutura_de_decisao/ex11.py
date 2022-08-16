'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input("Digite o salário do combrador: R$"))

if salario <= 280:
    print("Salário antes do reajuste: R$", salario, "\naumento de 20%\nvalor do aumento: R$", salario*0.20, "\nNovo salário: R$", salario + (salario*0.20))
elif salario > 280 and salario <= 700:
    print("Salário antes do reajuste: R$", salario, "\naumento de 15%\nvalor do aumento: R$", salario*0.15, "\nNovo salário: R$", salario + (salario*0.15))
elif salario > 700 and salario <= 1500:
    print("Salário antes do reajuste: R$", salario, "\naumento de 10%\nvalor do aumento: R$", salario*0.10, "\nNovo salário: R$", salario + (salario*0.10))
elif salario > 1500:
    print("Salário antes do reajuste: R$", salario, "\naumento de 5%\nvalor do aumento: R$", salario*0.05, "\nNovo salário: R$", salario + (salario*0.05))