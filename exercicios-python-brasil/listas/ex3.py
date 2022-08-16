#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    print("Digite a "+str(i+1)+"a. nota: ", end="")
    notas.append(float(input()))

print("")
for i in range(len(notas)):
    print(str(i+1)+"a. nota: ", notas[i])

media = sum(notas)/len(notas)

print("Média: %.2f"% media)
