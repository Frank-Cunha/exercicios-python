ganho_hora = float(input("Digite quanto você ganha por hora: "))
horas_mes = int(input("Digite quantas horas você trabalha por mês: "))
ir = (ganho_hora*horas_mes)*0.11
inss = (ganho_hora*horas_mes)*0.08
sindicato = (ganho_hora*horas_mes)*0.05

print("+ Salário bruto: R$", ganho_hora*horas_mes)
print("- IR (11%): R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Liquido : R$", ganho_hora*horas_mes - (ir + inss + sindicato))
