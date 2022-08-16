#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos_notas = []
notas = []
media_maior7 = 0

for item in range(10):
    for i in range(4):
        print("Digite a "+ str(i +1) +("a. nota do "+ str(item + 1)+ "o. aluno: "), end="")
        notas.append(float(input()))
    print("")
    media = sum(notas)/len(notas)
    alunos_notas.append(media)
    notas = []

for i in alunos_notas:
    if i >= 7:
        media_maior7 += 1

print("Quantidade de alunos com nota maior ou igual a 7.0:", media_maior7)




        


