#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numeros = [0]
menor = 999999999
maior = 0
cont = 0
soma = 0
resposta = "S"

while resposta == "S":
    cont += 1
    numeros.append(int(input("Adicione um número: ")))
    print(numeros)

    if numeros[cont] <= 0 or numeros[cont] >= 1000:
        del(numeros[cont])
        print(numeros)
        print("Numero inválido. Somente permitido números entre 0 e 1000")
        cont -= 1
    else:
        soma += numeros[cont]
    
    
    if numeros[cont] < menor:
        menor = numeros[cont]
    if numeros[cont] > maior:
        maior = numeros[cont]

    resposta = input("Continuar? S/N ")

print("Menor valor: ", menor, "\nMaior valor: ", maior, "\nSoma dos valores: ", soma)
