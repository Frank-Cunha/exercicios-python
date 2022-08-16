#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []
soma = 0
cont = 0

while True:
    print("Digite a "+ str(cont+1) +"a. temperatura em °C: ", end="")
    temperaturas.append(float(input()))
    soma += temperaturas[cont]
    resposta = input("Continuar? S/N ")
    if resposta == "S":
        cont += 1
    else:
        break

media = soma/len(temperaturas)

print("\nMenor temperatura: "+ str(min(temperaturas)) +"°C\nMaior temperatura: "+ str(max(temperaturas)) +"°C\nMédia de temperaturas: "+ str(media) +"°C")




    