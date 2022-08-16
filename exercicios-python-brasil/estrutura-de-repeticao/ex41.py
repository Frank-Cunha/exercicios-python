'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

valor_divida = float(input("Digite o valor da divida: R$ "))
quantidade_parecelas = [3, 6, 9, 12]
juros_inicial = 0.10
incremento = 0

print("\nValor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela\nR$ "+ str(int(valor_divida))+",00     0                   1                       R$ "+str(int(valor_divida))+",00")

for i in quantidade_parecelas:
    print("R$ "+ str(int(valor_divida + valor_divida*(juros_inicial + incremento)))+",00    ", int(valor_divida*(juros_inicial + incremento)), "               ", i, "                      R$ "+ str(int((valor_divida + valor_divida*(juros_inicial + incremento))/i))+",00")

    incremento += 0.05
    

    



