#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quantidade_turmas = int(input("Digite a quantidade de turmas: "))
quantidade_alunos = []
soma = 0

for i in range(1, quantidade_turmas +1):
    print("Digite a quantidade de alunos da "+ str(i) +"a. turma: ")
    quantidade_alunos.append(int(input()))
    while quantidade_alunos[i-1] > 40:
        print("Erro. Turma não pode ter mais de 40 alunos")
        del(quantidade_alunos[i-1])
        print("Digite novamente a quantidade de alunos da "+ str(i) +"a. turma: ")
        quantidade_alunos.append(int(input()))
        
    soma += quantidade_alunos[i-1]

media_alunos = soma/quantidade_turmas

print("Numero médio de alunos por turma: ", media_alunos)

