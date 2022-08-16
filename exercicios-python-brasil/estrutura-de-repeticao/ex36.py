'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
while True:
    num = int(input("Montar tabuada de: "))
    valor_inicial = int(input("Começar por: "))
    valor_final = int(input("Terminar em: "))

    print("\nVou montar a tabuada de", num, "começando em", valor_inicial, "e terminando em", valor_final,": ")

    if valor_final < valor_inicial:
        print("Erro. Valor final menor que o valor inicial")
    else:
        for i in range(valor_inicial, valor_final + 1):
            print(num, "X", i, "=", num*i)
        break
    



