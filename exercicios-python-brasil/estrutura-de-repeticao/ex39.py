#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

numero_alunos = []
altura_alunos= []

for i in range(10):
    print("Digite a número do "+ str(i+1)+"o. aluno: ", end="")
    numero_alunos.append(input())
    print("Digite a altura em metros do "+ str(i+1)+"o. aluno: ", end="")
    altura_alunos.append(float(input()))

aluno_alto = altura_alunos.index(max(altura_alunos))
aluno_baixo = altura_alunos.index(min(altura_alunos))

print("\nNúmero e altura do aluno mais alto: ", numero_alunos[aluno_alto], ",", max(altura_alunos),"m")
print("Número e altura do aluno mais baixo: ", numero_alunos[aluno_baixo], ",", min(altura_alunos),"m")


