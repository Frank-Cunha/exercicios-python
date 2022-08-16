#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(5):
    print("Digite a idade da "+ str(i +1) +"a. pessoa: ", end="")
    idades.append(int(input()))
    print("Digite a altura da "+ str(i +1) +"a. pessoa em metros: ", end="")
    alturas.append(float(input()))

idades.reverse()
alturas.reverse()

print("")
for i in range(len(idades)):
    print("Idade da "+str(len(idades) - i)+"a. pessoa: ", idades[i])
    print("altura da "+str(len(alturas) - i)+"a. pessoa: ", alturas[i],"\n")
