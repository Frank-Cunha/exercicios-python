#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenhar_retangulo(linhas, colunas):
    if linhas < 1 or linhas > 20 or str(linhas) == "":
        linhas = 1
    if colunas < 1 or colunas > 20 or str(linhas) == '':
        colunas = 1

    for i in range(colunas):
        print("-", end="")
    linha = "|"
    for i in range(colunas-2):
        linha = linha + " "
    linha = linha + "|"
    print()
    for i in range(linhas-2):
        print(linha)
    for i in range(colunas):
        print("-", end="")

linhas = int(input("Digite o número de linhas do retângulo: "))
colunas = int(input("Digite o número de colunas do retângulo: "))

desenhar_retangulo(linhas, colunas)