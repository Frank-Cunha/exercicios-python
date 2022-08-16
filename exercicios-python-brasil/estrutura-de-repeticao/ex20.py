#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

resposta = "S"

while resposta == "S":

    num = int(input("Digite o número que você deseja o fatorial: "))
    fatorial = 1

    if type(num) == int and num >= 0 and num < 16:
        for i in range(1,num + 1):
            fatorial *= i
        print(fatorial)
    else:
        print("Numero inválido. Somente permitido números inteiros positivos menores que 16")

    
    resposta = input("Deseja continuar? S/N ")