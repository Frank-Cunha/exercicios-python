#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0

while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota > 10 or nota < 0:
        print("Valor inválido")
    else: 
        print ("Valor válido")
        break
    

