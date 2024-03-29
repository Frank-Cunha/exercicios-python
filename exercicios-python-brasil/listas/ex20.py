'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''

salarios = []
cont = 0

print("Projeção de Gastos com Abono\n============================ \n")

while True:
    salarios.append(int(input("Salário: ")))
    if salarios[cont] == 0:
        salarios.pop()
        break
    cont += 1

total_abonos = 0
valor_minimo = 0
maior_abono = 0

print("\nSalário    - Abono ")
for i in salarios:
    abono = i*0.20
    if abono <= 100:
        abono = 100
        valor_minimo += 1
    total_abonos += abono
    if abono > maior_abono:
        maior_abono = abono

    print("R$ %.2f"% i,"- R$ %.2f"% abono)

print("\nForam processados", len(salarios), "colaboradores")
print("Total gasto com abonos: R$ %.2f"% total_abonos)
print("Valor mínimo pago a",valor_minimo,"colaboradores")
print("Maior valor de abono pago: R$ %.2f"% maior_abono)


