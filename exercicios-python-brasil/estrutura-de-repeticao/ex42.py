#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

cont = 0
numeros = []
numeros_0_25 = 0
numeros_26_50 = 0
numeros_51_75 = 0
numeros_76_100 = 0

while True:
    print("Digite o "+str(cont+1)+"o. número: ", end="")
    numeros.append(int(input()))
    if numeros[cont] < 0:
        break
    else:
        if numeros[cont] >= 0 and numeros[cont] <= 25:
            numeros_0_25 += 1
        elif numeros[cont] >= 26 and numeros[cont] <= 50:
            numeros_26_50 += 1
        elif numeros[cont] >= 51 and numeros[cont] <= 75:
            numeros_51_75 += 1
        elif numeros[cont] >= 76 and numeros[cont] <= 100:
            numeros_76_100 += 1
    cont += 1

print("Numeros entre o intervalo [0-25]:", numeros_0_25,"\nNumeros entre o intervalo [26-50]:", numeros_26_50, "\nNumeros entre o intervalo [51-75]:", numeros_51_75, "\nNumeros entre o intervalo [76-100]:", numeros_76_100)
