'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''
cont = 0
notas = []

while True:
    print("Digite a "+ str(cont +1) +"a. nota: ", end="")
    notas.append(float(input()))
    if notas[cont] == -1:
        notas.pop()
        break
    cont += 1

print("\nQuantidade de valores lidos:", len(notas))

print("\nTodos os valores: "+ str(notas[0]), end="")
for i in range (1, len(notas)):
    print(", "+ str(notas[i]), end="")

notas.reverse()
print("\n\nValores em ordem inversa: ")
for i in notas:
    print(i)
notas.reverse()

print("\nSoma dos valores:", sum(notas))

media = sum(notas)/len(notas)
print("\nMédia dos valores: %.2f"% media)

acima_media = 0
for i in notas:
    if i > media:
        acima_media += 1
print("\nQuantidade de valores acima da média:", acima_media)

abaixo_7 = 0
for i in notas:
    if i < 7:
        abaixo_7 += 1
print("\nQuantidade de valores abaixo de sete:", abaixo_7)

print("\n\nPrograma encerrado")







