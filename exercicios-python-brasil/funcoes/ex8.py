#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidade_digitos(num):
    return len(str(num))

numero = int(input("Digite um número inteiro: "))

print("Quantidade de digitos do número:", quantidade_digitos(numero))