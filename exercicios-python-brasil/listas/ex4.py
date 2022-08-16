#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []
num_vogais = 0
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
    print("Digite o "+str(i+1)+"o. caractere: ", end="")
    caracteres.append((input()))
    if caracteres[i] in vogais:
        num_vogais += 1

print("Consoantes lidas:", len(caracteres) - num_vogais)

