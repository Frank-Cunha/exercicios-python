'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
'''
artigos = 1.99

for i in range(1, 51):
    print(i ,"- R$ {:0.2f}".format(i*artigos))
    
    

 #Usado {:0.2f}".format() para formatar o número para aparecer sempre duas casas decimais depois da vírgula. Site de onde tirei o método: https://qastack.com.br/programming/20457038/how-to-round-to-2-decimals-with-python#:~:text=Basta%20usar%20a%20formata%C3%A7%C3%A3o%20com,arredondar%20para%202%20casas%20decimais.&text=Voc%C3%AA%20pode%20usar%20o%20operador,string%20do%20python%20%22%25%22.
