'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''
import os

cont = 1
precos = []
preco_total = 0

while True:
    while True:
        print("Produto "+ str(cont)+ ": R$", end='') #end='' usado para fazer o input ficar na mesma linha do print
        precos.append(float(input()))
        if precos[cont-1] == 0:
            break
        preco_total += precos[cont-1]
        cont += 1
        
    print("Total: R${:0.2f}".format(preco_total))
    dinheiro = float(input("Dinheiro: R$"))
    print("Troco: R${:0.2f}".format(dinheiro - preco_total))
    cont = 1
    os.system('cls')
    

