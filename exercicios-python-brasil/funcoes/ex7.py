'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
quantidade_prest = 0
valor_tot_prest = 0

def valorPagamento(prestacao,atraso_dias):
    if atraso_dias == 0:
        return prestacao
    else:
        return prestacao + (0.03*prestacao) + (((atraso_dias/100)/10)*prestacao)

while True:
    valor_prestação = float(input("Digite o valor da prestação: R$"))
    if valor_prestação == 0:
        break
    dias_atraso = int(input("Digite a quantidade de dias de atraso: "))

    quantidade_prest += 1
    valor_tot_prest += valorPagamento(valor_prestação,dias_atraso)

    print("Valor a ser pago na prestação: R$", valorPagamento(valor_prestação,dias_atraso))

print("\nRelatório do dia:\n\nQuantidades de prestações do dia:", quantidade_prest,"\nValor total das prestações: R$",valor_tot_prest)