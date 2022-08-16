#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []
alunos_baixos = 0

for i in range(30):
    print("Digite a idade do "+ str(i +1) +"o. aluno: ", end="")
    idades.append(int(input()))
    print("Digite a altura do "+ str(i +1) +"o. aluno: ", end="")
    alturas.append(float(input()))

media_altura = sum(alturas)/len(alturas)

for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_baixos += 1
print(idades, alturas)

print("\nAlunos com mais de 13 anos que possuem altura inferior à média dos alunos:", alunos_baixos)

