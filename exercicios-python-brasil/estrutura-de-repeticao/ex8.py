#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma_numeros = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    soma_numeros = soma_numeros + numero

media_numeros = soma_numeros/len(range(5))

print("Soma dos números: ", soma_numeros, "\nMédia dos números: ",media_numeros)

